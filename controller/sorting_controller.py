from services import job_sorting


def sorting(profile, pekerjaan, preferensi):
    try:
        return job_sorting.merge_sort_pekerjaan(
            pekerjaan_list=pekerjaan, profil=profile, preferensi=preferensi
        )
    except Exception as e:
        print("Terjadi kesalahan saat mengurutkan pekerjaan!")
        exit(1)
