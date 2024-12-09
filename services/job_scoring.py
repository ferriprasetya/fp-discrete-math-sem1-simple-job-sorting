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


def hitung_skor_kecocokan_pekerjaan(profil_fresh_graduate, deskripsi_pekerjaan):
    skor_kecocokan = {
        "skor_jurusan": 0,
        "skor_ipk": 0,
        "skor_pengalaman_kerja": 0,
        "skor_keterampilan": 0,
        "skor_gaji": 0,
        "skor_keseluruhan": 0,
    }

    # Skor jurusan
    skor_kecocokan["skor_jurusan"] = SM(
        None,
        profil_fresh_graduate["jurusan"],
        deskripsi_pekerjaan["persyaratan_pendidikan"],
    ).ratio()
    skor_kecocokan["skor_keseluruhan"] += skor_kecocokan["skor_jurusan"] * 0.2

    # Skor IPK
    skor_kecocokan["skor_ipk"] = hitung_kecocokan_angka(
        deskripsi_pekerjaan["syarat_ipk"], profil_fresh_graduate["ipk"]
    )
    skor_kecocokan["skor_keseluruhan"] += skor_kecocokan["skor_ipk"] * 0.15

    # Skor pengalaman kerja
    skor_kecocokan["skor_pengalaman_kerja"] = hitung_kecocokan_angka(
        deskripsi_pekerjaan["persyaratan_pengalaman"],
        profil_fresh_graduate["pengalaman_kerja"],
    )
    skor_kecocokan["skor_keseluruhan"] += skor_kecocokan["skor_pengalaman_kerja"] * 0.15

    # Skor keterampilan
    keterampilan_sesuai = set(profil_fresh_graduate["keterampilan"]) & set(
        deskripsi_pekerjaan["keterampilan_dibutuhkan"]
    )
    skor_kecocokan["skor_keterampilan"] = len(keterampilan_sesuai) / len(
        deskripsi_pekerjaan["keterampilan_dibutuhkan"]
    )
    skor_kecocokan["skor_keseluruhan"] += (0.20 * len(keterampilan_sesuai)) / len(
        deskripsi_pekerjaan["keterampilan_dibutuhkan"]
    )

    # Skor gaji
    skor_kecocokan["skor_gaji"] = hitung_kecocokan_angka(
        profil_fresh_graduate["harapan_gaji"], deskripsi_pekerjaan["gaji"], 1000000
    )
    skor_kecocokan["skor_keseluruhan"] += skor_kecocokan["skor_gaji"] * 0.10

    deskripsi_pekerjaan["skor_kecocokan"] = skor_kecocokan
    return skor_kecocokan
