import os
import json
import argparse
from pathlib import Path
from validate_audio import validate_audio_files, sha256_of_file, print_summary

def generate_audio_index(folder_path: str):
    index = {}
    missing_files, naming_violations, content_duplicates = validate_audio_files(
        folder_path, ignore_empty_surahs=True
    )

    all_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    for f in all_files:
        path = Path(folder_path) / f
        if f in naming_violations:
            continue
        if any(f in files for files in missing_files.values()):
            continue
        if any(f in files for files in content_duplicates.values()):
            continue
        surah_num, ayah_num = int(f[:3]), int(f[3:6])
        if surah_num not in index:
            index[surah_num] = {}
        index[surah_num][ayah_num] = {
            "filename": f,
            "path": str(path.as_posix()),
            "size_bytes": os.path.getsize(path),
            "sha256": sha256_of_file(path)
        }

    return index, missing_files, naming_violations, content_duplicates

def save_index(index: dict, output_file: str):
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate JSON index for Qur'an audio files (validated).")
    parser.add_argument("-f", "--folder", default="./abdul-wadood-haneef", help="Path to audio folder")
    args = parser.parse_args()

    audio_index, missing, violations, duplicates = generate_audio_index(args.folder)
    save_index(audio_index, "audio_index.json")

    print(f"Audio index generated: audio_index.json")
    if not missing and not violations and not duplicates:
        print("All files are valid and included in the index.")
    else:
        print("The following files were excluded from the index for the reasons below:\n")
        print_summary(missing, violations, duplicates)
