import os

data_mahasiswa = [
    {"id": "01", "nama": "raiya", "nilai": 85},
    {"id": "02", "nama": "iqbal", "nilai": 70}
]


def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')


def tampilkan_data():
    bersihkan_layar()
    print("=== DAFTAR NILAI MAHASISWA ===")
    if not data_mahasiswa:
        print("Data masih kosong.")
    else:
        print("-" * 35)
        print("ID    | Nama           | Nilai")
        print("-" * 35)
        for mhs in data_mahasiswa:
            print(mhs['id'].ljust(5), "|",
                  mhs['nama'].ljust(14), "|", mhs['nilai'])
        print("-" * 35)


def tambah_data():
    print("\n--- Tambah Data Baru ---")
    nim = input("Masukkan nomor absen: ")
    nama = input("Masukkan Nama: ")
    try:
        nilai = int(input("Masukkan Nilai (0-100): "))
        data_mahasiswa.append({"id": nim, "nama": nama, "nilai": nilai})
        print("Data berhasil ditambahkan!")
    except ValueError:
        print("Gagal! Nilai harus berupa angka.")


def edit_data():
    tampilkan_data()
    target_id = input("\nMasukkan no absen mahasiswa yang akan diedit: ")
    ketemu = False
    for mhs in data_mahasiswa:
        if mhs['id'] == target_id:
            print("Data lama:", mhs)
            mhs['nama'] = input("Masukkan Nama baru: ")
            try:
                mhs['nilai'] = int(input("Masukkan Nilai baru: "))
                print("Data berhasil diperbarui!")
            except ValueError:
                print("Input nilai salah, perubahan nilai dibatalkan.")
            ketemu = True
            break
    if not ketemu:
        print("ID tidak ditemukan.")


def hapus_data():
    tampilkan_data()
    target_id = input("\nMasukkan no absen mahasiswa yang akan dihapus: ")
    global data_mahasiswa
    panjang_awal = len(data_mahasiswa)
    data_mahasiswa = [mhs for mhs in data_mahasiswa if mhs['id'] != target_id]

    if len(data_mahasiswa) < panjang_awal:
        print("Data berhasil dihapus.")
    else:
        print("ID tidak ditemukan.")


while True:
    print("\nMENU UTAMA:")
    print("1. Lihat Data")
    print("2. Tambah Data")
    print("3. Edit Data")
    print("4. Hapus Data")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == '1':
        tampilkan_data()
    elif pilihan == '2':
        tambah_data()
    elif pilihan == '3':
        edit_data()
    elif pilihan == '4':
        hapus_data()
    elif pilihan == '5':
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")
