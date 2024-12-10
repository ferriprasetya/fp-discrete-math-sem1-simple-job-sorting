import pandas as pd
from tkinter import Tk, filedialog


def upload_list_pekerjaan_excel():
    # Menampilkan dialog untuk memilih file
    root = Tk()
    root.withdraw()  # Menyembunyikan jendela utama
    file_path = filedialog.askopenfilename(
        title="Pilih file Excel",
        filetypes=(("Excel Files", "*.xlsx"), ("All Files", "*.*")),
    )

    if file_path:
        try:
            # Membaca file Excel
            df = pd.read_excel(file_path)

            # Konversi DataFrame ke list of dictionaries
            job_list = df.to_dict(orient="records")

            # Mengubah string keterampilan menjadi list
            for job in job_list:
                if isinstance(job.get("keterampilan_dibutuhkan"), str):
                    job["keterampilan_dibutuhkan"] = job[
                        "keterampilan_dibutuhkan"
                    ].split(", ")
            return job_list
        except Exception as e:
            raise Exception("Error!!! Format file Excel tidak valid!")
    else:
        raise Exception("Error!!! File tidak ditemukan!")
