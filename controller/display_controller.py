from services import display_sorted_job as dsj


def display(job_list):
    try:
        dsj.tampilkan_urutan_list_pekerjaan(job_list)
    except Exception as e:
        print("Terjadi Kesalahan saat akan menampilkan hasil!")
        exit(1)
