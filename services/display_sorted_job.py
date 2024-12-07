import pandas as pd
import locale

from models.job_description import DeskripsiPekerjaan
from utils.format_score_to_percent import format_to_percent

def tampilkan_urutan_list_pekerjaan(pekerjaan_list: list[DeskripsiPekerjaan]):
    """
    Convert a list of DeskripsiPekerjaan objects to a pandas DataFrame and print it as a table.
    """
    # Prepare data for the DataFrame

    locale.setlocale(locale.LC_ALL, "id_ID.UTF-8")
    data = [
        {
            "Judul Pekerjaan": job.judul_pekerjaan,
            "Deskripsi": job.deskripsi_pekerjaan,
            "Pendidikan": job.persyaratan_pendidikan,
            "Pengalaman (Tahun)": job.persyaratan_pengalaman,
            "Keterampilan": ", ".join(job.keterampilan_dibutuhkan),
            "Gaji (Rupiah)": locale.currency(job.gaji, grouping=True),
            "Lokasi": job.lokasi,
            "Syarat IPK": job.syarat_ipk,
            "Kecocokan IPK": format_to_percent(job.skor_kecocokan.skor_ipk),
            "Kecocokan Jurusan": format_to_percent(job.skor_kecocokan.skor_jurusan),
            "Kecocokan Pengalaman Kerja": format_to_percent(
                job.skor_kecocokan.skor_pengalaman_kerja
            ),
            "Kecocokan Keterampilan": format_to_percent(
                job.skor_kecocokan.skor_keterampilan
            ),
            "Kecocokan Gaji": format_to_percent(job.skor_kecocokan.skor_gaji),
            "Kecocokan Keseluruhan": format_to_percent(
                job.skor_kecocokan.skor_keseluruhan
            ),
        }
        for job in pekerjaan_list
    ]

    # Create the DataFrame
    pd.set_option("display.width", 100)
    df = pd.DataFrame(data)

    # Print the DataFrame
    print(df)
