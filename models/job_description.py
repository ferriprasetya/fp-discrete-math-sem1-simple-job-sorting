from models.job_score import SkorPekerjaan


class DeskripsiPekerjaan:
    def __init__(
        self,
        judul_pekerjaan: str,
        deskripsi_pekerjaan: str,
        persyaratan_pendidikan: list[str],
        persyaratan_pengalaman: float,
        keterampilan_dibutuhkan: list[str],
        gaji: float,
        lokasi: str,
        syarat_ipk: float,
        skor_kecocokan: SkorPekerjaan = None,
    ):
        """
        inisialisasi deskripsi pekerjaan
        """
        self.judul_pekerjaan = judul_pekerjaan
        self.deskripsi_pekerjaan = deskripsi_pekerjaan
        self.persyaratan_pendidikan = persyaratan_pendidikan
        self.persyaratan_pengalaman = persyaratan_pengalaman
        self.keterampilan_dibutuhkan = keterampilan_dibutuhkan
        self.gaji = gaji
        self.lokasi = lokasi
        self.syarat_ipk = syarat_ipk
        self.skor_kecocokan = skor_kecocokan
