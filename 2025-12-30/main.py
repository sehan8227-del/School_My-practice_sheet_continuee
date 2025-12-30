import tkinter as tk
#왜굳이 TK라는 메서드를 호출했을까?
root = tk.Tk()
# ? 왜 매개 변수자리에 = 할당 연산자가 있는거지?
label = tk.Label(root, text= "Hello World!")

label.pack(pady=20)

root.mainloop()
