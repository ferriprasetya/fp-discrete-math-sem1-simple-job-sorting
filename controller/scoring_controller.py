from services import job_scoring


def scoring(profile, pekerjaan):
    try:
        return job_scoring.hitung_skor_kecocokan_pekerjaan(profile, pekerjaan)
    except Exception as e:
        print("Terjadi kesalahan saat menghitung skor kecocokan pekerjaan!")
        exit(1)
