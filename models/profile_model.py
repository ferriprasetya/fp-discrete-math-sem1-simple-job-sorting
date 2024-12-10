profile = dict(
    nama="",
    usia=0,
    jurusan="",
    ipk=0.0,
    pengalaman_kerja=0,
    keterampilan=[],
    harapan_gaji=0,
)


def set_profile(nama, usia, jurusan, ipk, pengalaman_kerja, keterampilan, harapan_gaji):
    global profile
    profile["nama"] = nama
    profile["usia"] = usia
    profile["jurusan"] = jurusan
    profile["ipk"] = ipk
    profile["pengalaman_kerja"] = pengalaman_kerja
    profile["keterampilan"] = keterampilan
    profile["harapan_gaji"] = harapan_gaji

    return profile
