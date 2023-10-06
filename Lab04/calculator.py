from tkinter import *

# Init root
root = Tk()
root.title('Calculator')

bieuThuc = "" 
textEntry = StringVar()

# xử lý khi nhấn vào các nút số hoặc phép tính
def handlePress(value):
  global bieuThuc
  bieuThuc += str(value)
  textEntry.set(bieuThuc)
  
# xử lý biểu thức khi nhấn nút "="
def handleResult():
  kq = eval(bieuThuc)
  print(kq)
  textEntry.set(f"{bieuThuc} = {kq}")
  
def handleClear():
  global bieuThuc
  bieuThuc = ""
  textEntry.set("")
  
def handleBack():
  global bieuThuc
  bieuThuc = bieuThuc[:-1]
  textEntry.set(bieuThuc)

def closeProgram():
  root.quit()

resultEntry = Entry(root, font= (24), textvariable= textEntry)
resultEntry.grid(row= 0, columnspan= 4, ipadx= 50)

clsButton = Button(root, text= 'Cls', height= 1, width= 10, command= handleClear)
clsButton.grid(row= 1, column= 0)

backButton = Button(root, text= 'Back', height= 1, width= 10, command= handleBack)
backButton.grid(row= 1, column= 1)

spaceButton = Button(root, text= '', height= 1, width= 10)
spaceButton.grid(row= 1, column= 2)

closeButton = Button(root, text= 'Close', height= 1, width= 10, command= closeProgram)
closeButton.grid(row= 1, column= 3)

button7 = Button(root, text= '7', height= 1, width= 10, command= lambda: handlePress(7))
button7.grid(row= 2, column= 0)

button8 = Button(root, text= '8', height= 1, width= 10, command= lambda: handlePress(8))
button8.grid(row= 2, column= 1)

button9 = Button(root, text= '9', height= 1, width= 10, command= lambda: handlePress(9))
button9.grid(row= 2, column= 2)

buttonDiv = Button(root, text= '/', height= 1, width= 10, command= lambda: handlePress('/'))
buttonDiv.grid(row= 2, column= 3)

button4 = Button(root, text= '4', height= 1, width= 10, command= lambda: handlePress(4))
button4.grid(row= 3, column= 0)

button5 = Button(root, text= '5', height= 1, width= 10, command= lambda: handlePress(5))
button5.grid(row= 3, column= 1)

button6 = Button(root, text= '6', height= 1, width= 10, command= lambda: handlePress(6))
button6.grid(row= 3, column= 2)

buttonMul = Button(root, text= '*', height= 1, width= 10, command= lambda: handlePress('*'))
buttonMul.grid(row= 3, column= 3)

button1 = Button(root, text= '1', height= 1, width= 10, command= lambda: handlePress(1))
button1.grid(row= 4, column= 0)

button2 = Button(root, text= '2', height= 1, width= 10, command= lambda: handlePress(2))
button2.grid(row= 4, column= 1)

button3 = Button(root, text= '3', height= 1, width= 10, command= lambda: handlePress(3))
button3.grid(row= 4, column= 2)

buttonSub = Button(root, text= '-', height= 1, width= 10, command= lambda: handlePress('-'))
buttonSub.grid(row= 4, column= 3)

button0 = Button(root, text= '0', height= 1, width= 10, command= lambda: handlePress(0))
button0.grid(row= 5, column= 0)

buttonDot = Button(root, text= '.', height= 1, width= 10, command= lambda: handlePress('.'))
buttonDot.grid(row= 5, column= 1)

buttonEqual = Button(root, text= '=', height= 1, width= 10, command= handleResult)
buttonEqual.grid(row= 5, column= 2)

buttonAdd = Button(root, text= '+', height= 1, width= 10, command= lambda: handlePress('+'))
buttonAdd.grid(row= 5, column= 3)

# Run
root.mainloop()
