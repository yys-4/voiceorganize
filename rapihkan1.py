import speech_recognition as sr
import os
import shutil
from datetime import datetime

# --- PENGATURAN PENTING ---
# ⚠️ UBAH ALAMAT FOLDER DI BAWAH INI SESUAI DENGAN KOMPUTER ANDA
# Contoh Windows: FOLDER_INDUK = r"C:\Users\NamaAnda\Downloads"
# Contoh macOS/Linux: FOLDER_INDUK = "/Users/NamaAnda/Downloads"
FOLDER_INDUK = r"D:\Ayyas\Transit"  # <--- GANTI BAGIAN INI


# Fungsi untuk mendengarkan perintah suara dalam Bahasa Indonesia
def dengarkan_perintah():
    """Mendengarkan input mikrofon dan mengubahnya menjadi teks."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ucapkan perintah Anda...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        perintah = r.recognize_google(audio, language="id-ID").lower()
        print(f'Anda mengatakan: "{perintah}"')
        return perintah
    except (sr.UnknownValueError, sr.RequestError):
        print("Maaf, perintah tidak dapat dikenali. Coba lagi.")
        return ""


# Fungsi utama untuk merapikan folder
def rapikan_folder_berdasarkan_tanggal():
    """Merapikan file berdasarkan bulan modifikasi dan formatnya."""

    if not os.path.isdir(FOLDER_INDUK):
        print(
            f"Error: Folder '{FOLDER_INDUK}' tidak ditemukan. Mohon periksa kembali path Anda."
        )
        return

    # Definisikan kategori folder berdasarkan ekstensi file
    KATEGORI = {
        "Gambar": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
        "Video": [".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv"],
        "Dokumen": [
            ".pdf",
            ".docx",
            ".doc",
            ".xlsx",
            ".xls",
            ".pptx",
            ".ppt",
            ".txt",
            ".csv",
        ],
        "Musik": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
        "Arsip": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Aplikasi": [".exe", ".msi"],
    }

    # Definisikan nama bulan dalam Bahasa Indonesia dengan awalan angka agar urut
    NAMA_BULAN = {
        1: "01. Januari",
        2: "02. Februari",
        3: "03. Maret",
        4: "04. April",
        5: "05. Mei",
        6: "06. Juni",
        7: "07. Juli",
        8: "08. Agustus",
        9: "09. September",
        10: "10. Oktober",
        11: "11. November",
        12: "12. Desember",
    }

    print(f"\nMemulai proses merapikan folder: {FOLDER_INDUK}")

    for nama_file in os.listdir(FOLDER_INDUK):
        path_file = os.path.join(FOLDER_INDUK, nama_file)

        if not os.path.isfile(path_file):
            continue

        # 1. TENTUKAN FOLDER BULAN
        timestamp_modifikasi = os.path.getmtime(path_file)
        tanggal_modifikasi = datetime.fromtimestamp(timestamp_modifikasi)
        nomor_bulan = tanggal_modifikasi.month
        nama_folder_bulan = NAMA_BULAN.get(nomor_bulan, "Bulan Tidak Diketahui")

        # 2. TENTUKAN FOLDER KATEGORI FORMAT
        ekstensi = os.path.splitext(nama_file)[1].lower()
        nama_folder_kategori = "Lainnya"
        for nama_kategori, daftar_ekstensi in KATEGORI.items():
            if ekstensi in daftar_ekstensi:
                nama_folder_kategori = nama_kategori
                break

        # 3. BUAT FOLDER & PINDAHKAN FILE
        path_tujuan_akhir = os.path.join(
            FOLDER_INDUK, nama_folder_bulan, nama_folder_kategori
        )
        os.makedirs(path_tujuan_akhir, exist_ok=True)
        shutil.move(path_file, os.path.join(path_tujuan_akhir, nama_file))
        print(
            f"-> Memindahkan '{nama_file}' ke '{nama_folder_bulan}/{nama_folder_kategori}'"
        )

    print("\n✅ Proses merapikan folder berdasarkan bulan dan format telah selesai.")


# --- PROGRAM UTAMA ---
if __name__ == "__main__":
    perintah_user = dengarkan_perintah()

    # Cukup cek apakah kata "rapikan" ada dalam perintah
    if "rapikan" in perintah_user:
        rapikan_folder_berdasarkan_tanggal()
    else:
        print("Perintah 'rapikan' tidak terdeteksi.")
