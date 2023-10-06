# Bài 1
from datetime import datetime
import locale
locale.setlocale(locale.LC_COLLATE, 'vi_VN')

class SinhVien:
    truong = "Đại học Đà Lạt"

    def __init__(self, maSo: int, hoten: str, ngaySinh: datetime) -> None:
        self._maSo = maSo
        self._hoten = hoten
        self._ngaySinh = ngaySinh

    @property
    def hoTen(self):
        return self._hoten

    @hoTen.setter
    def hoTen(self, hoTen: str):
        self._hoten = hoTen 

    @property
    def mssv(self):
        return self._maSo

    @mssv.setter
    def mssv(self, ms: int):
        if self.ktMsHopLe(ms):
            self._maSo = ms

    @property
    def ngaySinh(self):
        return self._ngaySinh

    @staticmethod 
    def ktMsHopLe(mssv: int):
        return len(str(mssv)) == 7

    def __str__(self) -> str:
        return f"{self._maSo}\t{self._hoten}\t{self._ngaySinh}"