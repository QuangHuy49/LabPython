from datetime import datetime

from SinhVien import SinhVien
from SinhVienChinhQuy import SinhVienChinhQuy
from SinhVienPhiChinhQuy import SinhVienPhiCQ
from DanhSachSinhVien import DanhSachSV

sv1 = SinhVienChinhQuy(2014401, "Quảng Văn Sương", datetime.strptime("02/07/2002", "%d/%m/%Y"), 88)
sv2 = SinhVienChinhQuy(2014402, "Nguyễn Thành Đạt", datetime.strptime("09/12/1999", "%d/%m/%Y"), 62)
sv3 = SinhVienPhiCQ(2014403, "Mai Hoàng Hải", datetime.strptime("02/10/2002", "%d/%m/%Y"), "Cao đẳng", 2)
sv4 = SinhVienPhiCQ(2014404, "Nguyễn Văn Lợi", datetime.strptime("27/02/1998", "%d/%m/%Y"), "Trung cấp", 3)
sv5 = SinhVienChinhQuy(2014405, "Trần Đình Minh Nhật", datetime.strptime("31/05/2000", "%d/%m/%Y"), 75)
sv6 = SinhVienChinhQuy(2014406, "Đồng Ngân Quỳnh", datetime.strptime("31/05/1998", "%d/%m/%Y"), 98)
sv7 = SinhVienPhiCQ(2014407, "Phạm Đình Công", datetime.strptime("12/12/1999", "%d/%m/%Y"), "Trung cấp", 3)
sv8 = SinhVienPhiCQ(2014408, "Nguyễn Lê Duy", datetime.strptime("09/08/1998", "%d/%m/%Y"), "Cao đẳng", 2)
sv9 = SinhVienPhiCQ(2014409, "Thái Thị Thanh Trúc", datetime.strptime("12/05/1999", "%d/%m/%Y"), "Trung cấp", 3)

dssv = DanhSachSV()
dssv.themSV(sv1)
dssv.themSV(sv2)
dssv.themSV(sv3)
dssv.themSV(sv4)
dssv.themSV(sv5)
dssv.themSV(sv6)
dssv.themSV(sv7)
dssv.themSV(sv8)
dssv.themSV(sv9)

print("Danh sách sinh viên hiện tại:")
dssv.xuat()
print()

def XuatKQ(kq):
    if(kq == []):
        print("<Không có kết quả>")
    for sv in kq:
        print(sv)
    print()

# 1/ Tìm vị trí sinh viên theo mã số
# ms = 2014405
# vt = dssv.timSVTheoMs(ms)
# print(f"Sinh viên có mã số {ms} ở vị trí thứ {vt + 1} trong danh sách")

# 2/ Danh sách sinh viên theo loại
# kq = dssv.timSvTheoLoai("chinhquy")
# print("Danh sách sinh viên theo loại:")
# for sv in kq:
#     print(sv)

# 3/ Tìm sinh viên có điểm rèn luyện từ 80 trở lên
# kq = dssv.timSVTheoDiemRL()
# print("Các sinh viên có điểm rèn luyện từ 80 trở lên:")
# XuatKQ(kq)

# 4/ Tìm sinh viên có trình độ cao đẳng sinh trước 15/8/1999
kq = dssv.timSVTheoNgaySinh()
print("Các sinh viên có có trình độ cao đẳng sinh trước 15/8/1999:")
XuatKQ(kq)
