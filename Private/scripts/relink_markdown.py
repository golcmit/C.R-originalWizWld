import os
import glob
import re

# --- 設定 ---
base_dir = "/mnt/c/Users/uhei2/novels/HogWarts"
world_dir = os.path.join(base_dir, "World")

# 1. World内の全マークダウンファイルを検索
markdown_files = glob.glob(os.path.join(world_dir, "**", "*.md"), recursive=True)
print(f"{len(markdown_files)} 個のマークダウンファイルをチェックします。")

# 2. 各ファイルに対して置換処理を実行
update_count = 0
for filepath in markdown_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            original_content = f.read()
    except Exception as e:
        print(f"ERROR: ファイルを読み込めませんでした: {filepath} - {e}")
        continue

    modified_content = original_content
    
    # [表示名](パス.md) の形式のリンクを検索
    # パスに './' や '../' が含まれる相対パスのみを対象とする
    # 角括弧の中で]をリテラルとして使う場合、エスケープは不要
    pattern = re.compile(r'[[^\\]+](((?:\\./|\\..\\/)[^)]+\.md))')
    
    replacements = []
    for match in pattern.finditer(original_content):
        full_match_text = match.group(0)
        display_name = match.group(1)
        relative_path = match.group(2)
        
        try:
            link_source_dir = os.path.dirname(filepath)
            absolute_link_target_path = os.path.normpath(os.path.join(link_source_dir, relative_path))
            vault_relative_path = os.path.relpath(absolute_link_target_path, base_dir)
            link_target_without_ext, _ = os.path.splitext(vault_relative_path)
            new_link = f"[[{link_target_without_ext}|{display_name}]]"
            replacements.append((full_match_text, new_link))
        except Exception as e:
            print(f"WARN: パス解決に失敗しました: {filepath} の中の {relative_path} - {e}")
            continue
    if replacements:
        update_count += 1
        temp_content = modified_content
        for old, new in replacements:
            temp_content = temp_content.replace(old, new, 1)
        modified_content = temp_content

    if modified_content != original_content:
        print(f"UPDATE: リンクを更新しました: {filepath}")
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(modified_content)
        except Exception as e:
            print(f"ERROR: ファイルを書き込めませんでした: {filepath} - {e}")

print(f"\nリンクの再接続処理が完了しました！ {update_count} 個のファイルを更新しました。")
