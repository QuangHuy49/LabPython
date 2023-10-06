from SinhVien import SinhVien
from datetime import datetime

class SinhVienChinhQuy(SinhVien):
    def __init__(self, maSo: int, hoten: str, ngaySinh: datetime, diemRL: int) -> None:
        super().__init__(maSo, hoten, ngaySinh)
        self.diemRL = diemRL

    def __str__(self) -> str:
        return super().__str__() + f"\t{self.diemRL}"