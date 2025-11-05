import os
import re
import argparse

# Dictionary with the number of ayahs in each surah
SURAH_AYAHS = {
    1: 7, 2: 286, 3: 200, 4: 176, 5: 120, 6: 165, 7: 206, 8: 75,
    9: 129, 10: 109, 11: 123, 12: 111, 13: 43, 14: 52, 15: 99, 16: 128,
    17: 111, 18: 110, 19: 98, 20: 135, 21: 112, 22: 78, 23: 118, 24: 64,
    25: 77, 26: 227, 27: 93, 28: 88, 29: 69, 30: 60, 31: 34, 32: 30,
    33: 73, 34: 54, 35: 45, 36: 83, 37: 182, 38: 88, 39: 75, 40: 85,
    41: 54, 42: 53, 43: 89, 44: 59, 45: 37, 46: 35, 47: 38, 48: 29,
    49: 18, 50: 45, 51: 60, 52: 49, 53: 62, 54: 55, 55: 78, 56: 96,
    57: 29, 58: 22, 59: 24, 60: 13, 61: 14, 62: 11, 63: 11, 64: 18,
    65: 12, 66: 12, 67: 30, 68: 52, 69: 52, 70: 44, 71: 28, 72: 28,
    73: 20, 74: 56, 75: 40, 76: 31, 77: 50, 78: 40, 79: 46, 80: 42,
    81: 29, 82: 19, 83: 36, 84: 25, 85: 22, 86: 17, 87: 19, 88: 26,
    89: 30, 90: 20, 91: 15, 92: 21, 93: 11, 94: 8, 95: 8, 96: 19,
    97: 5, 98: 8, 99: 8, 100: 11, 101: 11, 102: 8, 103: 3, 104: 9,
    105: 5, 106: 4, 107: 7, 108: 3, 109: 6, 110: 3, 111: 5, 112: 4,
    113: 5, 114: 6
}

def validate_audio_files(folder_path: str, ignore_empty_surahs: bool = False):
    """
    Check audio files for existence and correct naming.
    Returns:
      missing_files: dict of missing files per surah
      naming_violations: list of files that violate naming rules
    ignore_empty_surahs: if True, skip surahs with no files at all
    """
    missing_files = {}
    naming_violations = []

    pattern = re.compile(r'^(\d{3})(\d{3})\.mp3$')
    all_files = os.listdir(folder_path)

    # Check naming violations
    for f in all_files:
        match = pattern.match(f)
        if not match:
            naming_violations.append(f)
            continue
        surah_num, ayah_num = int(match.group(1)), int(match.group(2))
        if surah_num not in SURAH_AYAHS or ayah_num < 1 or ayah_num > SURAH_AYAHS[surah_num]:
            naming_violations.append(f)

    # Check missing files
    for surah, ayah_count in SURAH_AYAHS.items():
        files_in_surah = [f for f in all_files if f.startswith(f"{surah:03d}")]
        if ignore_empty_surahs and not files_in_surah:
            continue
        missing = [
            f"{surah:03d}{ayah:03d}.mp3"
            for ayah in range(1, ayah_count + 1)
            if f"{surah:03d}{ayah:03d}.mp3" not in all_files
            or os.path.getsize(os.path.join(folder_path, f"{surah:03d}{ayah:03d}.mp3")) == 0
        ]
        if missing:
            missing_files[surah] = missing

    return missing_files, naming_violations

def print_summary(missing_files: dict, naming_violations: list):
    """
    Print summary of missing files and naming violations.
    """
    if not missing_files and not naming_violations:
        print("All files are present and correctly named.")
        return

    if missing_files:
        print("Missing files per surah:")
        for surah, files in sorted(missing_files.items()):
            print(f"Surah {surah} ({len(files)} missing):")
            print(", ".join(files))
            print("-"*40)

    if naming_violations:
        print("\nFiles with naming violations:")
        print(", ".join(naming_violations))
        print("-"*40)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate Qur'an audio files.")
    parser.add_argument(
        "-f", "--folder",
        default="./abdul-wadood-haneef",
        help="Path to the audio folder (default: ./abdul-wadood-haneef)"
    )
    parser.add_argument(
        "-ies", "--ignore_empty_surahs",
        type=lambda x: x.lower() in ("true", "1", "yes"),
        default=False,
        help="Ignore surahs with no files at all (default: False)"
    )
    args = parser.parse_args()

    missing, violations = validate_audio_files(args.folder, ignore_empty_surahs=args.ignore_empty_surahs)
    print_summary(missing, violations)
