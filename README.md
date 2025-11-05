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

**Audio file naming convention:**

Each audio file is named as `00X00X.mp3`, where:

* The **first three digits** represent the **surah number**.
* The **last three digits** represent the **ayah number**.

| File Name   | Surah | Ayah |
|------------|-------|------|
| 002003.mp3 | 2     | 3    |
| 002004.mp3 | 2     | 4    |
| 114001.mp3 | 114   | 1    |

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

A script `validate_audio.py` is provided to **verify the integrity and naming of all audio files**.

### Running the script

```bash
python validate_audio.py -f ./abdul-wadood-haneef -ies True
```

**Arguments:**

* `-f ./abdul-wadood-haneef` or `--folder ./abdul-wadood-haneef` – Path to the folder containing audio files. 
* `-ies True` or `-ies False` – Whether to **ignore surahs with no files**:

  * `True` → Skip empty surahs (useful if the project is still under progress).
  * `False` → Count all missing ayahs, including surahs with no files.

---

### Output Explanation

The script generates **two main outputs**:

1. **Missing Files per Surah**

   * Lists all ayahs that are **expected but not present** or have **file size 0**.
   * Example:

     ```
     Surah 2 (3 missing):
     002003.mp3, 002004.mp3, 002005.mp3
     ----------------------------------------
     ```

2. **Files with Naming Violations**

   * Lists files that **do not follow the correct naming convention** `XXXYYY.mp3`
   * Includes files with **invalid surah or ayah numbers**.
   * Example:

     ```
     Files with naming violations:
     00203.mp3, 002-004.mp3, 115001.mp3
     ----------------------------------------
     ```

> This allows you to quickly identify missing audio and correct naming issues before further processing.

---

## Contributing

Contributions are welcome!
If you would like to contribute, please **contact me via email**: 📧 [adamhamri9@proton.me](mailto:adamhamri9@proton.me)

---

## Acknowledgment

This project is a personal effort to organize the Qur’an **verse by verse** with the corresponding audio of Abdul-Wadood Haneef.
May Allah accept it and grant benefit to anyone who uses it.
