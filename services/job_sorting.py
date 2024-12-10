from controller import scoring_controller


def merge_sort_pekerjaan(
    pekerjaan_list: list[dict],
    profil: dict,
    preferensi: str = "skor_keseluruhan",
):
    if len(pekerjaan_list) <= 1:
        return pekerjaan_list

    mid = len(pekerjaan_list) // 2
    left = merge_sort_pekerjaan(pekerjaan_list[:mid], profil, preferensi)
    right = merge_sort_pekerjaan(pekerjaan_list[mid:], profil, preferensi)

    return merge(left, right, profil, preferensi)


def merge(
    left: list[dict],
    right: list[dict],
    profil: dict,
    preferensi: str,
):
    sorted_list = []
    while left and right:
        left_score = scoring_controller.scoring(profil, left[0])[preferensi]
        right_score = scoring_controller.scoring(profil, right[0])[preferensi]

        if left_score >= right_score:  # Descending order (highest score first)
            sorted_list.append(left.pop(0))
        else:
            sorted_list.append(right.pop(0))

    # Append remaining items
    sorted_list.extend(left)
    sorted_list.extend(right)
    return sorted_list
