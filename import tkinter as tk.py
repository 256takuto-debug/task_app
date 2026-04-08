import tkinter as tk
import json

# メインウィンドウ
root = tk.Tk()
root.title("タスク管理アプリ")
root.geometry("400x400")  # サイズ指定
root.configure(bg="#f0f0f0")  # 背景色
# 入力欄
input_frame = tk.Frame(root, bg="#f0f0f0")
input_frame.pack(pady=10)

entry = tk.Entry(input_frame, width=25, font=("Arial", 12))
entry.pack(side=tk.LEFT, padx=5)
date_entry = tk.Entry(input_frame, width=15, font=("Arial", 12))
date_entry.pack(side=tk.LEFT, padx=5)
date_entry.insert(0, "2026-04-10")  # 初期値
# フレームの色の設定
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)
# リスト表示
task_listbox = tk.Listbox(root, width=40, height=10, font=("Arial", 12))
task_listbox.pack(pady=10)

# タスク追加
def add_task():
    task = entry.get()
    date = date_entry.get()
    
    if task:
        task_with_date = f"{task}（{date}）"
        task_listbox.insert(tk.END, task_with_date)
        entry.delete(0, tk.END)

# 削除機能
def delete_task():
    selected = task_listbox.curselection()
    if selected:
        task_listbox.delete(selected)
# 保存機能
def save_tasks():
    tasks = task_listbox.get(0, tk.END)
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
            for task in tasks:
                task_listbox.insert(tk.END, task)
    except:
        pass
# ボタンエリア
add_button = tk.Button(button_frame, text="追加", width=10, bg="#4CAF50", fg="white", command=add_task)
add_button.pack(side=tk.LEFT, padx=5)
delete_button = tk.Button(button_frame, text="削除", width=10, bg="#f44336", fg="white", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=5)
save_button = tk.Button(button_frame, text="保存", width=10, bg="#2196F3", fg="white", command=save_tasks)
save_button.pack(side=tk.LEFT, padx=5)

load_tasks()

root.mainloop()