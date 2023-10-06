''' IMPORTS '''
from tkinter import *
import tkinter.ttk as ttk
import re # regular expression

''' INIT '''
root = Tk()
root.title('Đăng ký học phần')
root.geometry('600x450')
root.configure(bg= 'light green')

''' FUNCTIONS '''

def resetErrorMessage():
   errorMessage.set('')

# kiểm tra giá trị truyền vào có phải là số không
def isDigit(value):
   return str.isdigit(str(value))

# kiểm tra field có rỗng không ?
def checkFieldEmpty(value):
   return value == ''

# kiểm tra hợp lệ MSSV
def validateMSSVField(value):
   if checkFieldEmpty(value):
      errorMessage.set('Mã số sinh viên không được để trống!')
      return False
   elif isDigit(value) == False:
      errorMessage.set('Mã số sinh viên chỉ chấp nhận ký tự số!')
      return False
   elif len(value) != 7:
      errorMessage.set('Mã số sinh viên phải đúng 7 ký số!')
      return False
   else:
      resetErrorMessage()
      return True
   
# kiểm tra hợp lệ họ tên
def validateHoTenField(value):
   if checkFieldEmpty(value):
      errorMessage.set('Họ tên sinh viên không được để trống!')
      return False
   else:
      resetErrorMessage()
      return True

# kiểm tra hợp lệ SĐT
def validatePhoneField(value):
   if checkFieldEmpty(value):
      errorMessage.set('Số điện thoại không được để trống!')
      return False
   elif isDigit(value) == False:
      errorMessage.set('Số điện thoại chỉ chấp nhận ký tự số!')
      return False
   elif len(value) != 10:
      errorMessage.set('Số điện thoại phải đúng 10 ký số!')
      return False
   else:
      resetErrorMessage()
      return True
         
# kiểm tra hợp lệ email
def validateEmail(value):
   regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
   if checkFieldEmpty(value):
      errorMessage.set('Email không được để trống!')
      return False
   elif re.match(regex, value):
      resetErrorMessage()
      return True
   else:
      errorMessage.set('Email không hợp lệ!')
      return False
         
# kiểm tra hợp lệ học kỳ
def validateHocKy(value):
   if checkFieldEmpty(value):
      errorMessage.set('Học kỳ không được để trống!')
      return False
   elif value != '1' and value != '2' and value != '3':
      errorMessage.set('Học kỳ chỉ chấp nhận (1 hoặc 2 hoặc 3)!')
      return False
   else:
      resetErrorMessage()
      return True

# kiểm tra hợp lệ ngày sinh
def validateNgaySinh(value):
   regex = r'\b[0-9]{2}\/[0-9]{2}\/[0-9]{4}\b'
   if checkFieldEmpty(value):
      errorMessage.set('Ngày sinh không được để trống!')
      return False
   elif re.match(regex, value):
      resetErrorMessage()
      return True
   else:
      errorMessage.set('Ngày sinh không đúng định dạng (dd/mm/yyyy)!')
      return False
      

# kiểm tra hợp lệ năm học
def validateNamHoc(value):
   i = namHocArray.index(value)
   print(i)

# xử lý click nút đăng ký
def handleRegisterBtn():
   validateMSSVField(mssvEntry.get())
   
# xử lý click nút thoát
def handleExitBtn():
   exit()
   
''' VARIABLES '''
errorMessage = StringVar()
namHocArray = ['2022-2023', '2023-2024', '2024-2025']
   
''' RENDER '''

# title
title = Label(root, text= "THÔNG TIN ĐĂNG KÝ HỌC PHẦN", font= (24), fg= 'red', bg= 'light green')
title.place(x= 130, y= 20)

# field
mssvLabel = Label(root, text= 'Mã số sinh viên', bg= 'light green')
mssvLabel.place(x= 10, y= 60)
mssvEntry = Entry(root, width= 50, validate= 'focusout', validatecommand= lambda: validateMSSVField(mssvEntry.get()))
mssvEntry.place(x= 130, y= 60)

# field
hoTenLabel = Label(root, text= 'Họ tên', bg= 'light green')
hoTenLabel.place(x= 10, y= 90)
hoTenEntry = Entry(root, width= 50, validate= 'focusout', validatecommand= lambda: validateHoTenField(hoTenEntry.get()))
hoTenEntry.place(x= 130, y= 90)

# field
ngaySinhLabel = Label(root, text= 'Ngày sinh', bg= 'light green')
ngaySinhLabel.place(x= 10, y= 120)
ngaySinhEntry = Entry(root, width= 50, validate= 'focusout', validatecommand= lambda: validateNgaySinh(ngaySinhEntry.get()))
ngaySinhEntry.place(x= 130, y= 120)

# field
emailLabel = Label(root, text= 'Email', bg= 'light green')
emailLabel.place(x= 10, y= 150)
emailEntry = Entry(root, width= 50, validate= 'focusout', validatecommand= lambda: validateEmail(emailEntry.get()))
emailEntry.place(x= 130, y= 150)

# field
sdtLabel = Label(root, text= 'Số điện thoại', bg= 'light green')
sdtLabel.place(x= 10, y= 180)
sdtEntry = Entry(root, width= 50, validate= 'focusout', validatecommand= lambda: validatePhoneField(sdtEntry.get()))
sdtEntry.place(x= 130, y= 180)

# field
hocKyLabel = Label(root, text= 'Học kỳ', bg= 'light green')
hocKyLabel.place(x= 10, y= 210)
hocKyEntry = Entry(root, width= 50, validate= 'focusout', validatecommand= lambda: validateHocKy(hocKyEntry.get()))
hocKyEntry.place(x= 130, y= 210)

# field
namHocLabel = Label(root, text= 'Năm học', bg= 'light green')
namHocLabel.place(x= 10, y= 240)
namHocComboBox = ttk.Combobox(root)
namHocComboBox['state'] = 'readonly'
namHocComboBox['values'] = namHocArray
# namHocComboBox.bind('<<ComboboxSelected>>', lambda e: print(namHocComboBox.current()))
namHocComboBox.place(x= 130, y= 240)

# field
chonMonHocLabel = Label(root, text= 'Chọn môn học', bg= 'light green')
chonMonHocLabel.place(x= 10, y= 270)

# checkbox
pythonCheckBtn = Checkbutton(root, text= 'Lập trình Python', bg= 'light green')
pythonCheckBtn.place(x= 130, y= 270)
javaCheckBtn = Checkbutton(root, text= 'Lập trình Java', bg= 'light green')
javaCheckBtn.place(x= 300, y= 270)
cnpmCheckBtn = Checkbutton(root, text= 'Công nghệ phần mềm', back= 'light green')
cnpmCheckBtn.place(x= 130, y= 300)
webCheckBtn = Checkbutton(root, text= 'Phát triển ứng dụng web', bg= 'light green')
webCheckBtn.place(x= 300, y= 300)

# error
errorLabel = Label(root, textvariable= errorMessage, fg= 'red', bg= 'light green')
errorLabel.place(x= 130, y= 350)

# buttons
registerBtn = Button(root, text= 'Đăng ký', bg= 'lime', command= handleRegisterBtn)
registerBtn.place(x= 130, y= 400)
exitBtn = Button(root, text= 'Thoát', bg= 'lime', command= handleExitBtn)
exitBtn.place(x= 240, y= 400)

root.mainloop()
