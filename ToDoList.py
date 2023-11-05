import tkinter as tk
from tkinter import ttk

class TodoList(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("To-Do List")
        self.geometry("300x400")

        self.task_list = tk.Listbox(self, width=30, height=30)
        self.task_list.pack(pady=20)

        self.add_task_frame = ttk.Frame(self)
        self.add_task_frame.pack(pady=20)

        self.task_entry = ttk.Entry(self.add_task_frame, width=30)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_task_button=ttk.Button(self.add_task_frame, text="Add Task", command=self.add_task)
        self.add_task_button.grid(row=0, column=1, padx=10, pady=10)
        
        self.delete_task_button = ttk.Button(self, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(pady=20)

    def add_task(self):
         task = self.task_entry.get()
         if task:
             self.task_list.insert(tk.END,task)
             self.task_entry.delete(0, tk.END)

    def delete_task(self):
        selected_task = self.task_list.curselection()
        if selected_task:
            self.task_list.delete(selected_task)

if __name__ == "__main__":
    app = TodoList()
    app.mainloop()