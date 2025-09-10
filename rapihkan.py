import speech_recognition as sr
import os
import shutil

FOLDER_UNDUHAN = r"D:\Ayyas"  # <--- GANTI BAGIAN INI


# Fungsi untuk mendengarkan perintah suara dalam Bahasa Indonesia
def dengarkan_perintah():
    """Mendengarkan input mikrofon dan mengubahnya menjadi teks menggunakan Google API."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ucapkan perintah Anda...")
        # Menyesuaikan dengan suara bising di sekitar
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        # Mengenali suara menggunakan Google Speech Recognition dengan bahasa Indonesia ('id-ID')
        perintah = r.recognize_google(audio, language="id-ID").lower()
        print(f'Anda mengatakan: "{perintah}"')
        return perintah
    except sr.UnknownValueError:
        print("Maaf, saya tidak mengerti apa yang Anda katakan.")
        return ""
    except sr.RequestError:
        print("Maaf, terjadi masalah dengan layanan pengenalan suara.")
        return ""


# Fungsi utama untuk merapikan folder unduhan
def rapikan_folder_unduhan():
    """Merapikan file di folder unduhan berdasarkan ekstensinya ke dalam subfolder."""

    # Cek apakah folder yang dituju ada
    if not os.path.isdir(FOLDER_UNDUHAN):
        print(
            f"Error: Folder '{FOLDER_UNDUHAN}' tidak ditemukan. Mohon periksa kembali path Anda."
        )
        return

    # Definisikan kategori folder dan ekstensi filenya
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

    print(f"\nMemulai proses merapikan folder: {FOLDER_UNDUHAN}")

    # Iterasi melalui setiap file di dalam folder unduhan
    for nama_file in os.listdir(FOLDER_UNDUHAN):
        path_file = os.path.join(FOLDER_UNDUHAN, nama_file)

        # Lewati jika item adalah folder, bukan file
        if not os.path.isfile(path_file):
            continue

        # Dapatkan ekstensi file
        ekstensi = os.path.splitext(nama_file)[1].lower()

        # Tentukan folder tujuan berdasarkan ekstensi
        folder_tujuan = "Lainnya"  # Folder default jika tidak ada di kategori
        for nama_kategori, daftar_ekstensi in KATEGORI.items():
            if ekstensi in daftar_ekstensi:
                folder_tujuan = nama_kategori
                break

        # Buat path folder tujuan
        path_folder_tujuan = os.path.join(FOLDER_UNDUHAN, folder_tujuan)

        # Buat folder kategori jika belum ada
        os.makedirs(path_folder_tujuan, exist_ok=True)

        # Pindahkan file ke folder yang sesuai
        shutil.move(path_file, os.path.join(path_folder_tujuan, nama_file))
        print(f"-> Memindahkan '{nama_file}' ke folder '{folder_tujuan}'")

    print("\n✅ Proses merapikan folder Unduhan telah selesai.")


# --- PROGRAM UTAMA ---
if __name__ == "__main__":
    perintah_user = dengarkan_perintah()

    # Kata kunci untuk memicu aksi (dalam Bahasa Indonesia)
    if "rapikan" in perintah_user and "unduhan" in perintah_user:
        rapikan_folder_unduhan()
    else:
        print(
            "Perintah untuk merapikan tidak terdeteksi. Coba ucapkan 'rapikan folder unduhan'."
        )
