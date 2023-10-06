from enum import Enum
import functools
import math

class PhanSo:
    def __init__(self, tu = 0, mau = 1) -> None:
        self.__tu = tu
        self.__mau = mau

    @property
    def tu(self):
        return self.__tu

    @tu.setter
    def tu(self, value):
        self.__tu = value

    @property
    def mau(self):
        return self.__mau

    @mau.setter
    def mau(self, value):
        if self.laMauSoHopLe(value):
            self.__mau = value

    @staticmethod
    def laMauSoHopLe(value: int):
        return value != 0

    def KiemTraPSAm(self):
        if self.tu / self.mau < 0:
            return True
        return False

    # def UocChungLonNhat(self, a: int, b: int):
    #     if b == 0:
    #         return a
    #     return self.UocChungLonNhat(b, a % b)
        
    # def BoiChungNhoNhat(self, a: int, b: int):
    #     return (a*b)/self.UocChungLonNhat(a,b)

    def DangThapPhan(self):
        return self.__tu / self.__mau 

    def rutGon(self):
        # greatest common divisor: Ước chung lớn nhất
        # least common multiple: bội chung nhỏ nhất
        ucln = math.gcd(self.tu, self.mau)
        # int chia int ra float
        # // chia lấy phần nguyên
        self.tu = self.tu // ucln
        self.mau = self.mau // ucln

    def __add__(self, other):
        kq = PhanSo()
        kq.tu = self.tu * other.mau + other.tu * self.mau
        kq.mau = self.mau * other.mau
        kq.rutGon()
        return kq

    def __sub__(self, other):
        kq = PhanSo()
        kq.tu = self.tu * other.mau - other.tu * self.mau
        kq.mau = self.mau * other.mau
        kq.rutGon()
        return kq

    def __mul__(self, other):
        kq = PhanSo()
        kq.tu = self.tu * other.tu
        kq.mau = self.mau * other.mau
        kq.rutGon()
        return kq

    def __truediv__(self, other):
        kq = PhanSo()
        kq.tu = self.tu * other.mau
        kq.mau = self.mau * other.tu
        kq.rutGon()
        return kq

    def __str__(self) -> str:
        return f"{self.__tu }/{ self.__mau}"

class DanhSachPhanSo:
    def __init__(self) -> None:
        self.ds = []

    def ThemPhanSo(self, ps: PhanSo):
        self.ds.append(ps)

    def Xuat(self):
        count = 0
        for x in self.ds:
            if count == 6:
                print("\n")
                count = 0
            print(x, end = "\t")
            count += 1

    def DocTuFile(self, filename: str):
        path = "Desktop\\2014483_DoQuocSang_Lab02\Data" + "\\" + filename
        f = open(path, "r",  encoding="utf8")
        for line in f:
            arr = [int(value.strip()) for value in line.split("/")] 
            ps = PhanSo(arr[0], arr[1])
            self.ThemPhanSo(ps)
        print("\nĐã đọc xong dữ liệu từ file!")
        f.close()

    def DanhSachDangThapPhan(self):
        return [ps.DangThapPhan() for ps in self.ds]

    def DemPSAm(self):
        return len([x for x in self.ds if x.KiemTraPSAm()])

    def TimPhanSoDuongNhoNhat(self):
        min_value = min([ps.DangThapPhan() for ps in self.ds if not ps.KiemTraPSAm()])
        for ps in self.ds:
            if  ps.DangThapPhan() == min_value:
                return ps
        return -1
        # return [ps for ps in self.ds if ps.DangThapPhan() == min_value]

    def TimVTPhanSo(self, ps : str):
        arr = ps.strip().split("/")
        arr = [int(item) for item in arr]
        value = PhanSo(arr[0],arr[1])
        vt = []
        for i in range(0,len(self.ds)):
            if self.ds[i].DangThapPhan() == value.DangThapPhan():
                vt.append(i)
        return vt

    def TongPSAm(self):
        sum = PhanSo()
        arr = [ps for ps in self.ds if ps.KiemTraPSAm()]
        for ps in arr:
            sum += ps
        return sum

    def XoaPS(self, ps: PhanSo):
        arr = self.TimVTPhanSo(ps)
        if not arr:
            return False
        for vt in arr:
            del self.ds[vt]
        return True

    def XoaPSTheoTu(self, tu: str):
        value = int(tu)
        kq = False
        for ps in self.ds:
            if ps.tu == value:
                self.ds.remove(ps)
                kq = True
        return kq

    def SapXepTang(self, func):
        self.ds.sort(key = func)
        # self.ds.sort(key = lambda x: x.DangThapPhan())
        # sorted trả về mảng

    def SapXepGiam(self, func):
        self.ds.sort(key = func, reverse=True)

    # Cách cơ bản
    # def SXTang(self):
    #     for i in range(0, len(self.ds)):
    #         for j in range(i+1, len(self.ds)):
    #             if self.ds[i].DangThapPhan() > self.ds[j].DangThapPhan():
    #                 self.ds[i], self.ds[j] = self.ds[j], self.ds[i]


# a = PhanSo()
# b = PhanSo(3,5)
# a.tu = 2
# a.mau = 10
# print(f"{a} + {b} = {a+b}")
# print(f"{a} - {b} = {a-b}")
# print(f"{a} * {b} = {a*b}")
# print(f"{a} / {b} = {a/b}")

ds = DanhSachPhanSo()
ds.DocTuFile("PhanSo.txt")
print("Danh sách phân số hiện tại:")
ds.Xuat()
print()

def XuatKQ(kq):
    if(kq == []):
        print("<Không có kết quả>")
    for x in kq:
        print(x, end = "\t")
    print()

# 1. Đếm số phân số âm trong mảng
# print(f"Có { ds.DemPSAm()} phân số âm trong mảng hiện tại")

# 2. Tìm phân số dương nhỏ nhất
# print("Phân số dương nhỏ nhất là: ", ds.TimPhanSoDuongNhoNhat())

# 3. Tìm tất cả vị trí của phân số x trong 
# ps = input("Nhập phân số cần tìm: ")
# kq = ds.TimVTPhanSo(ps)
# print(f"Vị trí của phân số {ps} trong mảng là:", end = " ")
# XuatKQ(kq)

# 4. Tổng tất cả các phân số âm trong mảng
# print("Tổng của tất cả phân số âm trong mảng là: ", ds.TongPSAm())

# 5. Xóa phân số x trong mảng
# ps = input("Nhập phân số cần xóa: ")
# kq = ds.XoaPS(ps)
# if kq:
#     print("Xóa thành công!")
#     print(f"Mảng hiện tại sau khi xóa {ps}:")
#     ds.Xuat()
#     print()
# else:
#     print("Xóa thất bại!")

# 6. Xóa tất cả phân số có tử là x
# tu = input("Nhập tử số cần xóa: ")
# kq = ds.XoaPSTheoTu(tu)
# if kq:
#     print("Xóa thành công!")
#     print(f"Mảng hiện tại sau khi xóa các phân số có tử là {tu}:")
#     ds.Xuat()
#     print()
# else:
#     print("Xóa thất bại!")

# 7. Sắp xếp phân số theo chiều tăng, giảm; tăng theo mẫu, tử, giảm theo mẫu tử.
# 7.1 Sắp xếp phân số theo chiều tăng
# def GiaTri(value : PhanSo):
#     return value.DangThapPhan()

# ds.SapXepTang(GiaTri)
# print(f"Mảng hiện tại sau khi sắp xếp theo chiều tăng:")
# ds.Xuat()
# print()

# 7.2 Sắp xếp phân số theo chiều giảm
# def GiaTri(value : PhanSo):
#     return value.DangThapPhan()

# ds.SapXepGiam(GiaTri)
# print(f"Mảng hiện tại sau khi sắp xếp theo chiều giảm:")
# ds.Xuat()
# print()

# 7.3 Sắp xếp phân số theo chiều tăng mẫu
# def MauSo(value : PhanSo):
#     return value.mau

# ds.SapXepTang(MauSo)
# print(f"Mảng hiện tại sau khi sắp xếp theo chiều tăng của mẫu:")
# ds.Xuat()
# print()

# 7.4 Sắp xếp phân số theo chiều giảm mẫu
# def MauSo(value : PhanSo):
#     return value.mau

# ds.SapXepGiam(MauSo)
# print(f"Mảng hiện tại sau khi sắp xếp theo chiều giảm của mẫu:")
# ds.Xuat()
# print()

# 7.5 Sắp xếp phân số theo chiều tăng tử
# def TuSo(value : PhanSo):
#     return value.tu

# ds.SapXepTang(TuSo)
# print(f"Mảng hiện tại sau khi sắp xếp theo chiều tăng của tử:")
# ds.Xuat()
# print()

# 7.6 Sắp xếp phân số theo chiều giảm tử
# def TuSo(value : PhanSo):
#     return value.tu

# ds.SapXepGiam(TuSo)
# print(f"Mảng hiện tại sau khi sắp xếp theo chiều giảm của tử:")
# ds.Xuat()
# print()
