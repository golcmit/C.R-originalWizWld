import os
import glob

# --- 設定 ---
script_path = os.path.realpath(__file__)
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(script_path)))
characters_dir = os.path.join(base_dir, "World", "Characters")
line_threshold = 5

print(f"{line_threshold}行未満のシンプルなprofile.mdを探します...")

# --- 検索 ---
profile_files = glob.glob(os.path.join(characters_dir, "*", "profile.md"))

simple_files_to_report = []

for filepath in profile_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            # ファイルを行に分割してリスト化
            lines = f.readlines()
            # 行数を数える
            num_lines = len(lines)
            
            if num_lines < line_threshold:
                # ファイルパスと行数をタプルで保存
                simple_files_to_report.append((filepath, num_lines))
    except Exception as e:
        print(f"ERROR: ファイル処理中にエラー: {filepath} - {e}")

# --- 結果表示 ---
if simple_files_to_report:
    print("\n以下のファイルがシンプルだと判断されました：")
    for f_path, l_count in simple_files_to_report:
        print(f"{f_path} ({l_count}行)")
else:
    print("\nシンプルなファイルは見つかりませんでした。")
