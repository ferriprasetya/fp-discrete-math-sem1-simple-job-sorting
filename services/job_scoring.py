def hitung_kecocokan_angka(angka_harapan, angka_pembanding, toleransi=1.0):
    # Cek jika angka pembanding dan harapan sama atau lebih
    if angka_pembanding >= angka_harapan:
        return 1

    # jarak angka pembanding dengan harapan
    gap = abs(angka_harapan - angka_pembanding)

    if toleransi == 0:
        return angka_harapan / angka_pembanding

    # Menghitung persentase berdasarkan jarak dan toleransi
    if gap > toleransi:
        angka_percentage = (
            0.5 - ((gap - toleransi) / gap) * 0.5
        )  # apabila lebih dari toleransi, akan selalu di bawah 50%
    else:
        angka_percentage = (
            0.5 + ((toleransi - gap) / toleransi) * 0.5
        )  # apabila kurang dari toleransi, akan selalu di atas 50%
    return angka_percentage


from difflib import SequenceMatcher as SM

from models.job_description import DeskripsiPekerjaan
from models.job_score import SkorPekerjaan
from models.profile import ProfilFreshGraduate


def hitung_skor_kecocokan_pekerjaan(
    profil_fresh_graduate: ProfilFreshGraduate, deskripsi_pekerjaan: DeskripsiPekerjaan
):
    skor_kecocokan = SkorPekerjaan(0, 0, 0, 0, 0, 0)

    skor_kecocokan.skor_jurusan = SM(
        None, profil_fresh_graduate.jurusan, deskripsi_pekerjaan.persyaratan_pendidikan
    ).ratio()
    # Max skor untuk jurusan = 20%
    skor_kecocokan.skor_keseluruhan += skor_kecocokan.skor_jurusan * 0.2

    skor_kecocokan.skor_ipk = hitung_kecocokan_angka(
        deskripsi_pekerjaan.syarat_ipk, profil_fresh_graduate.ipk
    )
    # Max skor untuk ipk = 15%
    skor_kecocokan.skor_keseluruhan += skor_kecocokan.skor_ipk * 0.15

    skor_kecocokan.skor_pengalaman_kerja += hitung_kecocokan_angka(
        deskripsi_pekerjaan.persyaratan_pengalaman,
        profil_fresh_graduate.pengalaman_kerja,
    )
    # Max skor untuk pengalaman kerja = 15%
    skor_kecocokan.skor_keseluruhan += skor_kecocokan.skor_pengalaman_kerja * 0.15

    keterampilan_sesuai = set(profil_fresh_graduate.keterampilan) & set(
        deskripsi_pekerjaan.keterampilan_dibutuhkan
    )
    skor_kecocokan.skor_keterampilan = len(keterampilan_sesuai) / len(
        deskripsi_pekerjaan.keterampilan_dibutuhkan
    )
    # Max skor untuk keterampilan = 20%
    skor_kecocokan.skor_keseluruhan += (0.20 * len(keterampilan_sesuai)) / len(
        deskripsi_pekerjaan.keterampilan_dibutuhkan
    )

    skor_kecocokan.skor_gaji = hitung_kecocokan_angka(
        profil_fresh_graduate.harapan_gaji, deskripsi_pekerjaan.gaji, 1000000
    )
    # Max skor untuk gaji = 10%
    skor_kecocokan.skor_keseluruhan += skor_kecocokan.skor_gaji * 0.10

    skor_kecocokan.skor_pengalaman_kerja += hitung_kecocokan_angka(
        deskripsi_pekerjaan.persyaratan_pengalaman,
        profil_fresh_graduate.pengalaman_kerja,
    )

    deskripsi_pekerjaan.skor_kecocokan = skor_kecocokan

    return skor_kecocokan
