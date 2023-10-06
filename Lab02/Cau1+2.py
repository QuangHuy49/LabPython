# Bài 1
from datetime import datetime
import locale
locale.setlocale(locale.LC_COLLATE, 'vi_VN')

class SinhVien:
    truong = "Đại học Đà Lạt"

    def __init__(self, maSo: int, hoten: str, ngaySinh: datetime) -> None:
        self.__maSo = maSo
        self.__hoten = hoten
        self.__ngaySinh = ngaySinh

    @property
    def maSo(self):
        return self.__maSo

    @maSo.setter
    def maSo(self, maSo):
        if self.LaMaSoHopLe(maSo):
            self.__maSo = maSo

    @property
    def hoTen(self):
        return self.__hoten

    @hoTen.setter
    def hoTen(self, hoTen: str):
        self.__hoten = hoTen

    @property
    def ngaySinh(self):
        return self.__ngaySinh

    @staticmethod 
    # Để không cần truyền self
    # static method không có quyền truy cập vào cls hoặc self
    def LaMaSoHopLe(maso: int):
        return len(str(maso)) == 7

    @classmethod
    # Các class method không cần một thể hiện của class
    def doiTenTruong(self, tenMoi):
        self.truong = tenMoi

    def __str__(self) -> str:
        return f"{self.__maSo}\t{self.__hoten}\t{self.__ngaySinh}"

    def xuat(self):
        print(f"{self.__maSo}\t{self.__hoten}\t{self.__ngaySinh}") 

class DanhSachSV:
    def __init__(self) -> None:
        self.dssv = []

    def ThemSinhVien(self, sv: SinhVien):
        self.dssv.append(sv)

    def xuat(self):
        for sv in self.dssv:
            print(sv)

    def TimSVTheoMssv(self, mssv: int):
        return [ sv for sv in self.dssv if sv.maSo == mssv ]

    def TimVTSVTheoMssv(self, mssv: int):
        for i in range(len(self.dssv)):
            if self.dssv[i].mssv == mssv:
                return i
        return -1

    def xoaSVTheoMssv(self, maSo: int) -> bool:
        vt = self.TimVTSVTheoMssv(maSo)
        if vt != -1:
            del self.dssv[vt]
            return True
        else:
            return False

    def timSVTheoTen(self, ten: str):
        return [ sv for sv in self.dssv if sv.hoTen.split(" ")[-1] == ten ]

    def timSVSinhTruocNgay(self, ngay: datetime):
        return [ sv for sv in self.dssv if sv.ngaySinh < ngay ]

    def DocTuFile(self, filename: str):
        path = "C:\\Users\SangTK\Downloads" + "\\" + filename
        f = open(path, "r",  encoding="utf8")
        for line in f:
            arr = [sv.strip() for sv in line.split(",")] 
            sv = SinhVien(arr[0], arr[1],  datetime.strptime(arr[2],'%d/%m/%Y'))
            self.ThemSinhVien(sv)
        print("Đã đọc xong dữ liệu từ file!")
        f.close()

    def DieuKienSapXep(self, sv: SinhVien):
        return locale.strxfrm(sv.hoTen.split(" ")[-1])

    def SapXepTangDanTheoTen(self):
        self.dssv.sort(key = self.DieuKienSapXep)

    def SapXepGiamDanTheoTen(self):
        self.dssv.sort(reverse=True , key = self.DieuKienSapXep)


# sv1 = SinhVien(1234567, "Nam Cao",  datetime(2002, 6, 1))
# sv1 = SinhVien(2014400, "Thái Thị Thanh Trúc", datetime.strptime("1/7/2002",'%d/%m/%Y'))
# sv2 = SinhVien(2014401, "Đỗ Đại Nam", datetime.strptime("2/3/2008",'%d/%m/%Y'))
# sv3 = SinhVien(2014402, "Trần Đình Minh Nhật", datetime.strptime("9/6/2009",'%d/%m/%Y'))
# sv4 = SinhVien(2014403, "Nguyễn Thành Đạt", datetime.strptime("29/2/2012",'%d/%m/%Y'))
# sv5 = SinhVien(2014404, "Quảng Văn Sương", datetime.strptime("19/6/2015",'%d/%m/%Y'))
# sv6 = SinhVien(2014405, "Nguyễn Nhật Nam", datetime.strptime("3/10/2003",'%d/%m/%Y'))
# sv7 = SinhVien(2014406, "Đồng Ngân Quỳnh", datetime.strptime("31/5/2002",'%d/%m/%Y'))

# arrSV = [sv1, sv2, sv3, sv4, sv5, sv6, sv7]
# dssv = DanhSachSV()
# for sv in arrSV:
#     dssv.ThemSinhVien(sv)

# print("Danh sach sinh vien:")
# dssv.xuat()

# def XuatKQ(arrSV):
#     print("\nKet qua:")
#     for x in arrSV:
#         x.xuat()

# Tìm sinh viên theo tên
# mang = dssv.timSVTheoTen("Nam")

# Tìm sinh viên có ngày sinh trước 5/5/2010 
# mang = dssv.timSVSinhTruocNgay(datetime.strptime("5/5/2010",'%d/%m/%Y'))

# Bài 2
# Đọc từ file
dssv = DanhSachSV()
dssv.DocTuFile("SinhVien.txt")
print("Danh sách hiện tại:")
dssv.xuat()

# Sắp xêp danh sách tăng giảm theo tên
dssv.SapXepTangDanTheoTen()
print("\nSắp xêp danh sách tăng dần theo tên:")
dssv.xuat()

# Sắp xêp danh sách tăng giảm theo tên
dssv.SapXepGiamDanTheoTen()
print("\nSắp xêp danh sách giảm dần theo tên:")
dssv.xuat()





