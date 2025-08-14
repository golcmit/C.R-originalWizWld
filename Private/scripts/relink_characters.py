import os
import glob
import re

# --- 設定 ---
# スクリプトの場所を基準にプロジェクトのルートディレクトリを自動的に決定
script_path = os.path.realpath(__file__)
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(script_path)))
print(f"プロジェクトディレクトリを '{base_dir}' として認識しました。")

characters_dir = os.path.join(base_dir, "World", "Characters")

# 1. 置換対象となるキャラクター名のリストを作成
if not os.path.isdir(characters_dir):
    print(f"ERROR: キャラクターディレクトリが見つかりません: {characters_dir}")
    exit()

character_names = [d for d in os.listdir(characters_dir) if os.path.isdir(os.path.join(characters_dir, d))]
print(f"{len(character_names)} 人のキャラクターをリンク置換対象として認識しました。")

# 2. プロジェクト内の全マークダウンファイルを検索
all_markdown_files = glob.glob(os.path.join(base_dir, "**", "*.md"), recursive=True)

# 除外するディレクトリのパスを定義
submodule_paths = [os.path.join(base_dir, "Novel_projects"), os.path.join(base_dir, "Database/Sruighlea")]
obsidian_path = os.path.join(base_dir, ".obsidian")
script_dir = os.path.join(base_dir, "Private", "scripts")

filtered_files = []
for f in all_markdown_files:
    is_excluded = any(f.startswith(p) for p in submodule_paths + [obsidian_path, script_dir])
    if not is_excluded:
        filtered_files.append(f)

print(f"{len(filtered_files)} 個のマークダウンファイルをチェックします。")

# 3. 各ファイルに対して置換処理を実行
update_count = 0
for filepath in filtered_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            original_content = f.read()
    except Exception as e:
        print(f"ERROR: ファイルを読み込めませんでした: {filepath} - {e}")
        continue

    modified_content = original_content
    
    for char_name in character_names:
        # 新しいWikilinkのパスを定義
        new_wikilink_path = f"World/Characters/{char_name}/profile"
        
        # --- ここからが重要 ---
        # 以前のファイル名を推測する
        # 例: "Alexandra Fungsyun" -> "Alexandra_Fungsyun.md", "AlexandraFungsyun.md" など
        # ここではスペースをアンダースコアに置換するパターンを想定
        old_filename_guess = char_name.replace(' ', '_') + '.md'
        escaped_old_filename = re.escape(old_filename_guess)

        # Markdownリンク `[表示テキスト](...旧ファイル名...)` を探す正規表現
        # `[^\]]+` は ] 以外の1文字以上 = 表示テキスト
        # `[^)]*?` は ) 以外の0文字以上（最短一致）= パス内のプレフィックス
        # `[^\)]*` は ) 以外の0文字以上 = パス内のサフィックス（もしあれば）
        pattern = re.compile(
            r'\[([^\]]+)\]'  # グループ1: 表示テキストをキャプチャ [表示テキスト]
            r'\('             # パスの開始 `(`
            r'[^)]*?'         # パス内のファイル名の前の部分（例: ./, ../, etc.）
            + escaped_old_filename +
            r'[^\)]*'         # パス内のファイル名の後の部分（もしあれば）
            r'\)'             # パスの終了 `)`
        )
        
        # 置換後の文字列を定義
        # `\1` はキャプチャした表示テキストを指す
        replacement_wikilink = fr'[[{new_wikilink_path}|\1]]'
        
        # 置換を実行
        modified_content = pattern.sub(replacement_wikilink, modified_content)

    # 内容に変更があった場合のみ書き込み
    if modified_content != original_content:
        print(f"UPDATE: リンクを更新しました: {filepath}")
        update_count += 1
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(modified_content)
        except Exception as e:
            print(f"ERROR: ファイルを書き込めませんでした: {filepath} - {e}")

print(f"\nリンクの再接続処理が完了しました！ {update_count} 個のファイルを更新しました。")