# Example usage
from services.display_sorted_job import tampilkan_urutan_list_pekerjaan
from services.job_sorting import merge_sort_pekerjaan

profil1 = {
    "nama": "John Doe",
    "usia": 23,
    "jurusan": "ilmu komputer",
    "ipk": 3.9,
    "pengalaman_kerja": 2,
    "keterampilan": ["python", "sql", "tableau"],
    "harapan_gaji": 7000000,
}

pekerjaan1 = [
    {
        "judul_pekerjaan": "software engineer",
        "deskripsi_pekerjaan": "mengembangkan dan memelihara aplikasi perangkat lunak",
        "persyaratan_pendidikan": "ilmu komputer",
        "persyaratan_pengalaman": 1,
        "keterampilan_dibutuhkan": ["python", "java", "sql"],
        "gaji": 6500000,
        "lokasi": "Surabaya, Jawa Timur",
        "syarat_ipk": 3.0,
    },
    {
        "judul_pekerjaan": "data analyst",
        "deskripsi_pekerjaan": "menganalisis data dan memberikan wawasan",
        "persyaratan_pendidikan": "statistik",
        "persyaratan_pengalaman": 1,
        "keterampilan_dibutuhkan": ["sql", "tableau", "python"],
        "gaji": 7500000,
        "lokasi": "Jakarta, DKI Jakarta",
        "syarat_ipk": 3.5,
    },
    {
        "judul_pekerjaan": "marketing coordinator",
        "deskripsi_pekerjaan": "mendukung kampanye pemasaran",
        "persyaratan_pendidikan": "bisnis",
        "persyaratan_pengalaman": 0,
        "keterampilan_dibutuhkan": [
            "desain grafis",
            "media sosial",
            "microsoft office",
        ],
        "gaji": 5000000,
        "lokasi": "Bandung, Jawa Barat",
        "syarat_ipk": 3.5,
    },
]

# Sort pekerjaan1 based on total percentage match
sorted_pekerjaan = merge_sort_pekerjaan(
    pekerjaan_list=pekerjaan1, profil=profil1, preferensi="skor_keseluruhan"
)

tampilkan_urutan_list_pekerjaan(sorted_pekerjaan)
