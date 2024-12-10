# Example usage
from controller import display_controller, excel_controller, sorting_controller
from models.profile_model import set_profile


def main_view():
    # Input profil user
    print("Masukkan informasi profil Anda:")

    nama = input("Nama: ")
    usia = int(input("Usia: "))
    jurusan = input("Jurusan: ")
    ipk = float(input("IPK: "))
    pengalaman_kerja = int(input("Pengalaman kerja (dalam tahun): "))
    keterampilan = input(
        "Keterampilan (pisahkan dengan koma, contoh: python, sql, tableau): "
    ).split(", ")
    harapan_gaji = int(input("Harapan gaji (dalam Rupiah): "))

    # Menyimpan data ke dalam dictionary
    profile_user = set_profile(
        nama=nama,
        usia=usia,
        jurusan=jurusan,
        ipk=ipk,
        pengalaman_kerja=pengalaman_kerja,
        keterampilan=keterampilan,
        harapan_gaji=harapan_gaji,
    )

    # Input file list pekerjaan
    list_pekerjaan = excel_controller.upload_list_pekerjaan()

    # Input preferensi sorting
    list_preferensi_sorting = [
        ("Skor Keseluruhan", "skor_keseluruhan"),
        ("Skor IPK", "skor_ipk"),
        ("Skor Jurusan", "skor_jurusan"),
        ("Skor Pengalaman Kerja", "skor_pengalaman_kerja"),
        ("Skor Keterampilan", "skor_keterampilan"),
        ("Skor Gaji", "skor_gaji"),
    ]

    print("Pilih preferensi pengurutan pekerjaan berdasarkan:")
    for i in range(len(list_preferensi_sorting)):
        print(f"{i + 1}. {list_preferensi_sorting[i][0]}")

    nomor_preferensi = int(input("Masukkan nomor preferensi: ")) - 1

    preferensi_sorting = list_preferensi_sorting[nomor_preferensi][1]

    # Sort pekerjaan1 based on total percentage match
    sorted_pekerjaan = sorting_controller.sorting(
        pekerjaan=list_pekerjaan, profile=profile_user, preferensi=preferensi_sorting
    )

    display_controller.display(sorted_pekerjaan)
