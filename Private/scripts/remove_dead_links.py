import os
import glob
import re

# --- 設定 ---
script_path = os.path.realpath(__file__)
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(script_path)))
target_dirs = [os.path.join(base_dir, "World", "Characters"), os.path.join(base_dir, "World", "Linage")]

print(f"デッドリンクのクリーンアップを開始します... 対象ディレクトリ: {', '.join(target_dirs)}")

# --- 検索対象ファイルの準備 ---
markdown_files = []
for d in target_dirs:
    markdown_files.extend(glob.glob(os.path.join(d, "**", "*.md"), recursive=True))

print(f"{len(markdown_files)} 個のマークダウンファイルをチェックします。")

# --- メイン処理 ---
update_count = 0
# 正規表現: [[リンク先]] または [[リンク先|表示名]]
# グループ1: リンク先, グループ3: 表示名 (オプショナル)
pattern = re.compile(r'\[\[([^\]|]+)(\|([^\]]+))?\]\]')

for filepath in markdown_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            original_content = f.read()
    except Exception as e:
        print(f"ERROR: ファイルを読み込めませんでした: {filepath} - {e}")
        continue

    modified_content = original_content
    replacements = []

    for match in pattern.finditer(original_content):
        full_link = match.group(0)
        link_target = match.group(1)
        display_name = match.group(3) # 表示名はグループ3
        
        # リンク先のファイルパスを構築 (.md がついていないと仮定)
        potential_path = os.path.join(base_dir, link_target + ".md")
        
        # ファイルが存在しない場合、デッドリンクと判断
        if not os.path.exists(potential_path):
            # 置換後のテキストを決定
            if display_name:
                replacement_text = display_name
            else:
                replacement_text = link_target # 表示名がなければリンク先テキストを残す
            replacements.append((full_link, replacement_text))

    if replacements:
        update_count += 1
        print(f"UPDATE: {filepath} のデッドリンクをテキストに変換します:")
        for old, new in replacements:
            print(f"  - 「{old}」 -> 「{new}」")
            modified_content = modified_content.replace(old, new)
        
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(modified_content)
        except Exception as e:
            print(f"ERROR: ファイルを書き込めませんでした: {filepath} - {e}")

print(f"\n処理が完了しました！ {update_count} 個のファイルを更新しました。")