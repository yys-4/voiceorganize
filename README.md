# 🗣️ Voice-Activated File Organizer

Tired of a messy downloads folder? Use your voice to tidy it up!

This project contains a collection of Python scripts that automatically organize files in a specified folder based on your voice commands. Simply speak, and let the script sort everything into neat, labeled folders.

Choose from three different versions, from a simple organizer to an advanced one that sorts files by date and category.

## ✨ Features

-   **Voice-Activated**: Simply say the magic words to start the organization process.
-   **📂 Automatic Categorization**: Sorts files into logical folders like `Images`, `Videos`, `Documents`, etc.
-   **🗓️ Advanced Sorting (Optional)**: The advanced script can create subfolders based on the month and year the file was modified.
-   **🇮🇩 Indonesian Language Support**: Includes versions that understand Indonesian commands ("*rapikan unduhan*").
-   **⚙️ Customizable**: Easily set your own target folder.
-   **✅ Lightweight**: No complex setup, just a simple Python script.

---

##  Scripts Overview

This repository includes three different scripts. Choose the one that best suits your needs!

### 1. `organizer.py` (Basic)

-   **Language**: English 🇬🇧
-   **Command**: `"organize downloads"`
-   **Functionality**: Sorts files into two basic categories: `Images` and `Docs`. A great starting point.

### 2. `rapihkan.py` (Intermediate)

-   **Language**: Indonesian 🇮🇩
-   **Command**: `"rapikan unduhan"`
-   **Functionality**: Sorts files into a wide range of categories: `Gambar` (Images), `Video`, `Dokumen`, `Musik`, `Arsip` (Archives), `Aplikasi` (Executables), and `Lainnya` (Others).

### 3. `rapihkan1.py` (Advanced)

-   **Language**: Indonesian 🇮🇩
-   **Command**: `"rapikan"`
-   **Functionality**: The most powerful script. It creates a two-level folder structure. First, it creates folders for the month the file was modified (e.g., `01. Januari`, `02. Februari`). Then, inside each month folder, it categorizes the files just like `rapihkan.py`.

---

## 🚀 How to Use

Follow these steps to get started:

### 1. Prerequisites

-   You must have **Python 3** installed on your computer.
-   You need a working **microphone**.

### 2. Choose Your Script

Decide which of the three scripts (`organizer.py`, `rapihkan.py`, or `rapihkan1.py`) you want to use.

### 3. Configure the Folder Path

This is the most important step! You must tell the script which folder you want to organize.

Open your chosen script file in a text editor and find the line that specifies the folder path. **Change the path to match the folder on your computer.**

-   For `organizer.py`:
    ```python
    # Find this line:
    folder = r"C:\Users\ASUS\Downloads"
    # Change it to your target folder, for example:
    folder = r"C:\Users\YourName\Downloads"
    ```

-   For `rapihkan.py`:
    ```python
    # Find this line:
    FOLDER_UNDUHAN = r"D:\Ayyas" # <--- GANTI BAGIAN INI
    # Change it to your target folder, for example:
    FOLDER_UNDUHAN = r"C:\Users\YourName\Downloads"
    ```

-   For `rapihkan1.py`:
    ```python
    # Find this line:
    FOLDER_INDUK = r"D:\Ayyas\Transit" # <--- GANTI BAGIAN INI
    # Change it to your target folder, for example:
    FOLDER_INDUK = r"C:\Users\YourName\Downloads"
    ```
    > **Note:** For macOS or Linux, the path format will be different, e.g., `/Users/YourName/Downloads`.

### 4. Install Dependencies

Open your terminal or command prompt and navigate to the project directory. Install the required Python libraries using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```
> This will install `SpeechRecognition` and `PyAudio`. If you have issues with `PyAudio` on your system, you may need to install it manually. Please refer to the [PyAudio documentation](https://people.csail.mit.edu/hubert/pyaudio/) for system-specific installation instructions.

### 5. Run the Script

In your terminal, run the script you chose:

```bash
python organizer.py
```
or
```bash
python rapihkan.py
```
or
```bash
python rapihkan1.py
```

### 6. Give the Voice Command

The script will print a message like `"Say something..."` or `"Ucapkan perintah Anda..."`. When you see this, speak the corresponding command clearly into your microphone:
-   For `organizer.py`: **"organize downloads"**
-   For `rapihkan.py`: **"rapikan unduhan"**
-   For `rapihkan1.py`: **"rapikan"**

The script will then start organizing the files and print its progress.

---

Enjoy your newly organized folder! 🎉
