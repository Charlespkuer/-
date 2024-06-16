import tkinter as tk
from tkinter import ttk, messagebox

class App:
    def __init__(self, master):
        self.master = master
        self.public_count = 0
        self.limit_count = 0
        self.history = []

        self.label = tk.Label(self.master, text="Press 1 for public, 2 for limit, Backspace to undo, Enter to show result")
        self.label.pack()

        self.table = ttk.Treeview(self.master, columns=('Public', 'Limit', 'Total'), show='headings')
        self.table.heading('Public', text='Public')
        self.table.heading('Limit', text='Limit')
        self.table.heading('Total', text='Total')
        self.table.pack()

        self.master.bind('1', self.increment_public)
        self.master.bind('2', self.increment_limit)
        self.master.bind('<BackSpace>', self.undo)
        self.master.bind('<Return>', self.show_result)

        self.update_table()

    def increment_public(self, event):
        self.public_count += 1
        self.history.append(('Public', 1))
        self.update_table()

    def increment_limit(self, event):
        self.limit_count += 1
        self.history.append(('Limit', 1))
        self.update_table()

    def undo(self, event):
        if self.history:
            operation, count = self.history.pop()
            if operation == 'Public':
                self.public_count -= count
            else:
                self.limit_count -= count
            self.update_table()

    def show_result(self, event):
        messagebox.showinfo("Result", f"Public: {self.public_count}, Limit: {self.limit_count}, Total: {self.public_count + self.limit_count}")

    def update_table(self):
        self.table.delete(*self.table.get_children())
        self.table.insert('', 'end', values=(self.public_count, self.limit_count, self.public_count + self.limit_count))

root = tk.Tk()
app = App(root)
root.mainloop()
