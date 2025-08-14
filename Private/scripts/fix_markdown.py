import os
import re
import sys

def fix_markdown_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            original_content = f.read()

        # Rule MD030: Only one space after list markers (e.g. "*   item" -> "* item")
        processed_content = re.sub(r'^(\s*[\*\-]\s)\s+', r'\1', original_content, flags=re.MULTILINE)

        # Rule MD032 (for headings): Add blank line after heading if it's missing
        processed_content = re.sub(r'^(#+ .*)\n([^\n])', r'\1\n\n\2', processed_content, flags=re.MULTILINE)

        if original_content != processed_content:
            print(f"  -> Fixing {filepath}")
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(processed_content)

    except Exception as e:
        print(f"Error processing {filepath}: {e}")


def process_directory(directory):
    print(f"\nSearching for .md files in '{directory}'...")
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".md"):
                filepath = os.path.join(root, filename)
                fix_markdown_file(filepath)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for target_dir in sys.argv[1:]:
            if os.path.isdir(target_dir):
                process_directory(target_dir)
            else:
                print(f"Error: Directory '{target_dir}' not found.")
        print("\nDone!")
    else:
        print("Usage: python fix_markdown.py <directory_path_1> [<directory_path_2>...]")
