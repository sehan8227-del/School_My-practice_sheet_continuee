import tkinter as tk
from tkinter import messagebox

# 데이터를 저장할 리스트 (임시 데이터베이스)
recipes = []

# [저장] 버튼을 눌렀을 때 실행되는 함수 (Create)
def add_recipe():
    category = entry_category.get() # 항목 입력창에서 가져오기
    title = entry_title.get()       # 제목 입력창에서 가져오기
    content = entry_content.get()   # 내용 입력창에서 가져오기

    if category and title and content:
        recipe = f"[{category}] {title} - {content}"
        recipes.append(recipe)
        update_listbox()            # 목록 새로고침
        
        # 입력창 비우기
        entry_category.delete(0, tk.END)
        entry_title.delete(0, tk.END)
        entry_content.delete(0, tk.END)
    else:
        messagebox.showwarning("경고", "모든 칸을 채워주세요!")

# [조회] 목록을 업데이트하는 함수 (Read)
def update_listbox():
    listbox.delete(0, tk.END)  # 기존 목록 지우기
    for r in recipes:
        listbox.insert(tk.END, r)

# 1. 메인 창 생성
root = tk.Tk()
root.title("돈스타브 레시피 관리자")
root.geometry("400x500")

# 2. 입력 부분 (항목, 제목, 내용)
tk.Label(root, text="항목 (예: 요리, 도구)").pack(pady=5)
entry_category = tk.Entry(root, width=40)
entry_category.pack()

tk.Label(root, text="제목 (예: 미트볼)").pack(pady=5)
entry_title = tk.Entry(root, width=40)
entry_title.pack()

tk.Label(root, text="내용 (예: 고기1+얼음3)").pack(pady=5)
entry_content = tk.Entry(root, width=40)
entry_content.pack()

# 3. 버튼
btn_add = tk.Button(root, text="레시피 저장", command=add_recipe, bg="#e67e22", fg="white")
btn_add.pack(pady=20)

# 4. 조회 부분 (리스트박스)
tk.Label(root, text="--- 저장된 레시피 목록 (조회) ---").pack()
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

# 실행
root.mainloop()