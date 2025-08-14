
import os
import glob
import shutil

# --- 設定 ---
base_dir = "/mnt/c/Users/uhei2/novels/HogWarts"
characters_base_dir = os.path.join(base_dir, "World", "Characters")
visuals_base_dir = os.path.join(base_dir, "Private", "image_script", "Visual", "Character_Visual_Scripts")

# --- 実行 ---
print("キャラクター情報の整理を開始します...")

# キャラクタープロファイルファイルを取得
# サブディレクトリ（一族）の中にファイルがあることを想定
profile_files = glob.glob(os.path.join(characters_base_dir, "*", "*.md"))

# もしサブディレクトリに見つからなければ、Characters直下も探す
if not profile_files:
    profile_files = glob.glob(os.path.join(characters_base_dir, "*.md"))

print(f"{len(profile_files)} 件のキャラクターファイルが見つかりました。")

for profile_path in profile_files:
    if not os.path.isfile(profile_path):
        continue

    file_name = os.path.basename(profile_path)
    character_name = os.path.splitext(file_name)[0]
    
    # 新しいキャラクターディレクトリを作成
    new_character_dir = os.path.join(characters_base_dir, character_name)
    if not os.path.exists(new_character_dir):
        print(f"CREATE: ディレクトリ {new_character_dir} を作成します。")
        os.makedirs(new_character_dir, exist_ok=True)
    
    # プロファイルファイルを移動 & リネーム
    new_profile_path = os.path.join(new_character_dir, "profile.md")
    print(f"MOVE: {profile_path} -> {new_profile_path}")
    shutil.move(profile_path, new_profile_path)
    
    # 対応する外見設定ファイルを探す
    visual_file_path = os.path.join(visuals_base_dir, file_name)
    if os.path.exists(visual_file_path):
        new_visual_path = os.path.join(new_character_dir, "visual.md")
        print(f"MOVE: {visual_file_path} -> {new_visual_path}")
        shutil.move(visual_file_path, new_visual_path)
    else:
        print(f"INFO: {character_name} の外見設定ファイルは見つかりませんでした。")

print("\n空になった可能性のある一族ディレクトリを削除します...")

# `World/Characters/*` を検索し、それがディレクトリであり、かつ中身が空であるものを削除
for item in glob.glob(os.path.join(characters_base_dir, '*')):
    if os.path.isdir(item):
        # 中にファイルやサブディレクトリがないか確認
        if not os.listdir(item):
            try:
                os.rmdir(item)
                print(f"DELETE: 空のディレクトリ {item} を削除しました。")
            except OSError as e:
                print(f"ERROR: {item} の削除中にエラーが発生しました: {e}")
        else:
            print(f"INFO: ディレクトリ {item} は空ではないため、削除しませんでした。")


print("\n整理が完了しました！")
