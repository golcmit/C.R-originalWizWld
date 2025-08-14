import os
import glob
import re

# --- 設定 ---
script_path = os.path.realpath(__file__)
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(script_path)))
target_dirs = [os.path.join(base_dir, "World", "Characters"), os.path.join(base_dir, "World", "Linage")]

print(f"デッドリンクの検索を開始します... 対象ディレクトリ: {', '.join(target_dirs)}")

# --- 検索対象ファイルの準備 ---
markdown_files = []
for d in target_dirs:
    markdown_files.extend(glob.glob(os.path.join(d, "**", "*.md"), recursive=True))

print(f"{len(markdown_files)} 個のマークダウンファイルをチェックします。")

# --- メイン処理 ---
update_count = 0
# 正規表現: [[リンク先]] または [[リンク先|表示名]]
# リンク先には '|' と ']' が含まれないようにする
pattern = re.compile(r'(\[\[([^\]|]+)(?:\|[^]]+)?\]\])')

for filepath in markdown_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            original_content = f.read()
    except Exception as e:
        print(f"ERROR: ファイルを読み込めませんでした: {filepath} - {e}")
        continue

    dead_links = []
    for match in pattern.finditer(original_content):
        full_link = match.group(1)
        link_target = match.group(2)
        
        # リンク先のファイルパスを構築 (.md がついていないと仮定)
        potential_path = os.path.join(base_dir, link_target + ".md")
        
        # ファイルが存在しない場合、デッドリンクと判断
        if not os.path.exists(potential_path):
            dead_links.append(full_link)

    if dead_links:
        update_count += 1
        modified_content = original_content
        print(f"UPDATE: {filepath} から以下のデッドリンクを削除します:")
        for link in dead_links:
            print(f"  - {link}")
            # リンクを空文字に置換
            modified_content = modified_content.replace(link, "")
        
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(modified_content)
        except Exception as e:
            print(f"ERROR: ファイルを書き込めませんでした: {filepath} - {e}")

print(f"\n処理が完了しました！ {update_count} 個のファイルを更新しました。")
