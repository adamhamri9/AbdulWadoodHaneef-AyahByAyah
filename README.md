# AbdulWadoodHaneef – Qur’an Verse By Verse Audio

This repository contains my work on **dividing the Qur’an into individual verses (Verse By Verse)** and organizing the corresponding **audio files for each verse** recited by Abdul-Wadood Haneef.

---

## Reflection

Working on this task reminds me of the immense effort required just to divide and align text and audio. It deepens my appreciation of the greatness of Allah who revealed it, and of the extraordinary patience of the Prophet ﷺ.

If organizing preserved text and sound is demanding, imagine the endurance required to receive, memorize, and convey it under the most challenging circumstances.

---

## Personal Note

During the course of this project, I faced **some health challenges** and had to undergo a medical procedure, which caused a temporary pause in my work for about a month. Alhamdulillah, I have now **resumed my efforts**.

---

## Project Structure

* `README.md` – This documentation file.  
* `abdul-wadood-haneef/` – Folder containing audio files divided **verse by verse**.  
* `validate_audio.py` – Script to verify audio files.  
* `generate_audio_index.py` – Script to generate structured JSON index for valid audio files.

**Audio file naming convention:**

Each audio file is named as `00X00X.mp3`, where:

* The **first three digits** represent the **surah number**.
* The **last three digits** represent the **ayah number**.

| File Name   | Surah | Ayah |
|-------------|--------|------|
| 002003.mp3  | 2      | 3    |
| 002004.mp3  | 2      | 4    |
| 114001.mp3  | 114    | 1    |

*(More files will be added as the project progresses.)*

---

## Usage

1. Clone the repository:

```bash
git clone https://github.com/adamhamri9/AbdulWadoodHaneef-AyahByAyah
````

2. Navigate to the audio folder:

```bash
cd AbdulWadoodHaneef-AyahByAyah/abdul-wadood-haneef
```

3. Use the files as needed for listening, personal study, or further technical processing.

---

## Audio Validation Script

A script `validate_audio.py` is provided to **verify the integrity and naming of all audio files**, as well as **detect content duplicates** (files with identical audio content).

### Running the script

```bash
python validate_audio.py -f ./abdul-wadood-haneef -ies True
```

**Arguments:**

* `-f ./abdul-wadood-haneef` or `--folder ./abdul-wadood-haneef` – Path to the folder containing audio files.
* `-ies True` or `-ies False` – Whether to **ignore surahs with no files**:

  * `True` → Skip empty surahs (useful if the project is still under progress).
  * `False` → Count all missing ayahs, including surahs with no files.

### Output Explanation

The script generates **three main outputs**:

1. **Missing Files per Surah**

   * Lists all ayahs that are **expected but not present** or have **file size 0**.
   * Example:

     ```
     Surah 2 (3 missing):
     002003.mp3, 002004.mp3, 002005.mp3
     ----------------------------------------
     ```

2. **Files with Naming Violations**

   * Lists files that **do not follow the correct naming convention** `XXXYYY.mp3`.
   * Includes files with **invalid surah or ayah numbers**.
   * Example:

     ```
     Files with naming violations:
     00203.mp3, 002-004.mp3, 115001.mp3
     ----------------------------------------
     ```

3. **Content-Duplicate Files**

   * Lists groups of files that have **identical audio content** based on SHA256 hash.
   * Example:

     ```
     Content-duplicate groups (same SHA256):
     Hash: 5393a91179de0b9667926155f2184083fcbe712c7b484a5319868d66ad51a422 -> 2 files
       004043 - Copy.mp3
       004043.mp3
     ------------------------------
     ```

> This allows you to quickly identify missing, incorrectly named, or duplicated audio files before further processing.

---

## Audio Index Generator

A script `generate_audio_index.py` is included to **create a structured JSON index** of all valid audio files, automatically **excluding any missing, misnamed, or duplicated files**.

### Running the script

```bash
python generate_audio_index.py -f ./abdul-wadood-haneef -u https://mycdn.com/audio/
```

**Arguments:**

* `-f ./abdul-wadood-haneef` or `--folder ./abdul-wadood-haneef` – Path to the folder containing audio files.
* `-u https://mycdn.com/audio/` or `--url-prefix https://mycdn.com/audio/` – Optional prefix or base URL for the audio files.

  * If not provided, the script defaults to `./` for local file paths.

---

### Output

The script generates a single file: **`audio_index.json`**, structured as follows:

```json
{
  "1:1": {
    "surah_number": 1,
    "ayah_number": 1,
    "audio_url": "./001001.mp3",
    "duration": 5.23,
    "segments": []
  },
  "1:2": {
    "surah_number": 1,
    "ayah_number": 2,
    "audio_url": "./001002.mp3",
    "duration": 4.85,
    "segments": []
  }
}
```

**Field Descriptions:**

| Field          | Description                                                             |
| -------------- | ----------------------------------------------------------------------- |
| `surah_number` | The surah number (1–114).                                               |
| `ayah_number`  | The verse number within the surah.                                      |
| `audio_url`    | Path or URL to the verse audio (uses provided prefix or `./`).          |
| `duration`     | Duration of the audio in seconds (float, may be `null` if unreadable).  |
| `segments`     | Currently empty – reserved for per-word timing data in future versions. |

---

### Console Summary

When executed, the script prints a brief summary:

```bash
Audio index generated: audio_index.json
All files are valid and included in the index.
```

If invalid files are detected:

```bash
Audio index generated: audio_index.json
The following files were excluded from the index for the reasons below:

- Missing or zero-size files
- Invalid filenames
- Duplicate content detected
```

This ensures that the JSON index only contains **valid, unique, and usable** audio entries, ready for use in applications or APIs.

---

## Contributing

Contributions are welcome!
If you would like to contribute, please **contact me via email**: [adamhamri9@proton.me](mailto:adamhamri9@proton.me)

---

## Notices

* **Source of Recordings:**  
  The full-surah audio recordings originate from the [qul.tarteel.ai](https://qul.tarteel.ai/resources/recitation/410) platform.

* **Segmentation Process:**  
  The verse-by-verse audio files found in this repository were **derived from those full-surah recordings** through a segmentation process intended to make the recitations easier to reference and study.

* **Intent:**  
  The work presented here is shared as part of an **independent, non-profit effort** that aims to support Qur’an-related projects and facilitate technical or educational exploration.

* **Copyright Disclaimer:**  
  No ownership is claimed over the original recordings.  
  All rights remain with their **rightful owners** — **Sheikh Abdul-Wadood Haneef** and/or the **original production company** from which the recitations were sourced.  
  The segmented verse-level audio files are a **derived technical format** based on publicly available materials.

* **Legal Note:**  
  This repository is provided for transparency and public benefit.  
  Any copyright holder may request modification or removal of specific content, and such requests will be respected.


