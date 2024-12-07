from models.job_description import DeskripsiPekerjaan
from models.profile import ProfilFreshGraduate
from services.job_scoring import hitung_skor_kecocokan_pekerjaan


def merge_sort_pekerjaan(
    pekerjaan_list: list[DeskripsiPekerjaan],
    profil: ProfilFreshGraduate,
    preferensi: str = "skor_keseluruhan",
):
    """
    Mengurutkan daftar pekerjaan berdasarkan preferensi pengguna menggunakan merge sort.
    """
    if len(pekerjaan_list) <= 1:
        return pekerjaan_list

    mid = len(pekerjaan_list) // 2
    left = merge_sort_pekerjaan(pekerjaan_list[:mid], profil, preferensi)
    right = merge_sort_pekerjaan(pekerjaan_list[mid:], profil, preferensi)

    return merge(left, right, profil, preferensi)


def merge(
    left: list[DeskripsiPekerjaan],
    right: list[DeskripsiPekerjaan],
    profil: ProfilFreshGraduate,
    preferensi: str,
):
    """
    Menggabungkan dua sublist berdasarkan preferensi pengguna.
    """
    sorted_list = []
    while left and right:
        left_score = hitung_skor_kecocokan_pekerjaan(profil, left[0])[preferensi]
        right_score = hitung_skor_kecocokan_pekerjaan(profil, right[0])[preferensi]

        if left_score >= right_score:  # Descending order (highest score first)
            sorted_list.append(left.pop(0))
        else:
            sorted_list.append(right.pop(0))

    # Append remaining items
    sorted_list.extend(left)
    sorted_list.extend(right)
    return sorted_list
