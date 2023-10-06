# from SinhVienChinhQuy import SinhVienChinhQuy
# from SinhVienPhiChinhQuy import SinhVienPhiCQ
# from SinhVien import SinhVien
# from datetime import datetime

# class DanhSachSV:
#     def __init__(self) -> None:
#         self.dssv = []

#     def themSV(self, sv: SinhVien):
#         self.dssv.append(sv)

#     def xuat(self):
#         for sv in self.dssv:
#             print(sv)

#     def timSVTheoMs(self, ms: int):
#         for i in range(len(self.dssv)):
#             if self.dssv[i].mssv == ms:
#                 return i
#         else:
#             return -1

#     def timSvTheoLoai(self, loai: str):
#         if loai == "chinhquy":
#             return [sv for sv in self.dssv if isinstance(sv, SinhVienChinhQuy)]
#         return [sv for sv in self.dssv if isinstance(sv, SinhVienPhiCQ)]

#     # Tìm sinh viên có điểm luyện từ 80 trở lên
#     def timSVTheoDiemRL(self):
#         return [sv for sv in self.dssv if isinstance(sv, SinhVienChinhQuy) and sv.diemRL >= 80]

#     #  Tìm sinh viên có trình độ cao đẳng sinh trước 15/9/1999
#     def timSVTheoNgaySinh(self):
#         return [sv for sv in self.dssv if isinstance(sv, SinhVienPhiCQ) and sv.trinhDo == "Cao đẳng" and sv.ngaySinh < datetime.strptime("15/08/1999", "%d/%m/%Y")]

# print()
# var= "James Bond"
# print(var[::-1])
# print(var[4::-1])
# print()


x = -21

print (~~~~x)