class SkorPekerjaan:
    def __init__(
        self,
        skor_jurusan: int,
        skor_ipk: int,
        skor_pengalaman_kerja: int,
        skor_keterampilan: int,
        skor_gaji: int,
        skor_keseluruhan: int,
    ):
        """
        inisialisasi skor tiap parameter
        """
        self.skor_jurusan = skor_jurusan
        self.skor_ipk = skor_ipk
        self.skor_pengalaman_kerja = skor_pengalaman_kerja
        self.skor_keterampilan = skor_keterampilan
        self.skor_gaji = skor_gaji
        self.skor_keseluruhan = skor_keseluruhan

    def __getitem__(self, item):
        return self.__dict__[item]
