from cmath import sinh
from sys import int_info
from SinhVien import SinhVien
from datetime import datetime

class SinhVienPhiCQ(SinhVien):
    def __init__(self, maSo: int, hoten: str, ngaySinh: datetime, trinhdo: str, tgdt: int) -> None:
        super().__init__(maSo, hoten, ngaySinh)
        self.thoiGianDaoTao = tgdt
        self.trinhDo = trinhdo

    def __str__(self) -> str:
        return super().__str__() + f"\t{self.trinhDo}\t{self.thoiGianDaoTao}"