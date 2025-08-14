import os
import glob

# --- 設定 ---
script_path = os.path.realpath(__file__)
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(script_path)))
characters_dir = os.path.join(base_dir, "World", "Characters")
content_line_threshold = 1 # この行数以下をシンプルとみなす

print(f"見出しと空行を除いて、内容が{content_line_threshold}行以下のファイルを探します...")

# --- 検索 ---
profile_files = glob.glob(os.path.join(characters_dir, "*", "profile.md"))

found_files = False
for filepath in profile_files:
    meaningful_lines = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                stripped_line = line.strip()
                if stripped_line and not stripped_line.startswith('#'):
                    meaningful_lines.append(stripped_line)
    except Exception as e:
        print(f"ERROR: ファイル処理中にエラー: {filepath} - {e}")
        continue

    if len(meaningful_lines) <= content_line_threshold:
        if not found_files:
            print("\n--- シンプルだと判断されたファイル ---")
            found_files = True
        
        print(f"\nファイル: {filepath}")
        if meaningful_lines:
            for content_line in meaningful_lines:
                 print(f"内容: {content_line}")
        else:
            print("内容: (実質的に空)")

if not found_files:
    print("\nシンプルなファイルは見つかりませんでした。")
