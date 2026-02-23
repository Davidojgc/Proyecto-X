import tkinter as tk
from tkinter import filedialog

class App:
    def __init__(self, master):
        self.master = master
        master.title("File Upload")

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            "Capacidad de planta",
            "Maestro de materiales",
            "Maestro de clientes",
            "Demanda",
        ]

        for title in buttons:
            button = tk.Button(self.master, text=title, command=lambda t=title: self.upload_file(t))
            button.pack(pady=10)

    def upload_file(self, title):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", ["*.xlsx", "*.xls"]), ("All files", ["*"])])
        if file_path:
            print(f"{title} file uploaded: {file_path}")

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
