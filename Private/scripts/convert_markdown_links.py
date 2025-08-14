import os
import glob
import re

# --- 設定 ---
script_path = os.path.realpath(__file__)
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(script_path)))
print(f"プロジェクトディレクトリを '{base_dir}' として認識しました。")

# --- 検索対象ファイルの準備 ---
all_markdown_files = glob.glob(os.path.join(base_dir, "**", "*.md"), recursive=True)

# 除外するディレクトリのパスを定義
submodule_paths = [os.path.join(base_dir, "Novel_projects"), os.path.join(base_dir, "Database/Sruighlea")]
# ★★★ ここの変数名を修正しました ★★★
obsidian_path = os.path.join(base_dir, ".obsidian") 
script_dir = os.path.join(base_dir, "Private", "scripts")

filtered_files = []
for f in all_markdown_files:
    # 呼び出し側の変数名も修正
    is_excluded = any(f.startswith(p) for p in submodule_paths + [obsidian_path, script_dir])
    if not is_excluded:
        filtered_files.append(f)

print(f"{len(filtered_files)} 個のマークダウンファイルをチェックします。")

# --- メイン処理 ---
update_count = 0
# 正規表現: [表示名](相対パス.md) を探す
# パスは './' または '../' で始まるものに限定
pattern = re.compile(
    r'\[([^\]]+)\]\(((?:\./|\.\./)[^)]+\.md)\)'
)

for filepath in filtered_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            original_content = f.read()
    except Exception as e:
        print(f"ERROR: ファイルを読み込めませんでした: {filepath} - {e}")
        continue

    modified_content = original_content
    replacements = []

    # 変更箇所を先にすべてリストアップする
    for match in pattern.finditer(original_content):
        full_match_text = match.group(0) # 置換対象の文字列全体 e.g. [text](./path/to/file.md)
        display_name = match.group(1)    # 表示名 e.g. text
        relative_path = match.group(2)   # 相対パス e.g. ./path/to/file.md
        
        try:
            # リンク元ファイルのディレクトリを取得
            link_source_dir = os.path.dirname(filepath)
            # リンク先の絶対パスを計算
            absolute_link_target_path = os.path.normpath(os.path.join(link_source_dir, relative_path))
            # プロジェクトルートからの相対パスに変換（これがWikiリンクのパスになる）
            vault_relative_path = os.path.relpath(absolute_link_target_path, base_dir)
            # 拡張子 ".md" を取り除く
            link_target_without_ext, _ = os.path.splitext(vault_relative_path)
            
            # 新しいWikiリンク形式を作成
            new_link = f"[[{link_target_without_ext}|{display_name}]]"
            replacements.append((full_match_text, new_link))
        except Exception as e:
            print(f"WARN: パス解決に失敗しました: {filepath} の中の {relative_path} - {e}")
            continue
    
    # リストアップした変更をまとめて適用する
    if replacements:
        update_count += 1
        print(f"UPDATE: リンクを更新しました: {filepath}")
        for old, new in replacements:
            # 複数同じリンクがあっても1つずつ置換するために count=1 を指定
            modified_content = modified_content.replace(old, new, 1)

        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(modified_content)
        except Exception as e:
            print(f"ERROR: ファイルを書き込めませんでした: {filepath} - {e}")

print(f"\nリンクの再接続処理が完了しました！ {update_count} 個のファイルを更新しました。")