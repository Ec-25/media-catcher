import tkinter as tk
from tkinter import messagebox
from simple_media_dl import MediaDownloader


class Home(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.init_widgets()

    def init_widgets(self):
        tk.Label(
            self, text="Media Catcher", font=("Rubik", 18), justify=tk.CENTER
        ).pack()

        top_container = tk.Frame(self)
        top_container.pack(side=tk.TOP, fill=tk.Y)

        tk.Label(top_container, text="URL:", font=("Rubik", 14), justify=tk.LEFT).pack(
            side=tk.LEFT
        )
        self.url_entry = tk.Entry(top_container, font=("Rubik", 12), width=50)
        self.url_entry.pack(
            side=tk.LEFT, padx=10
        )
        tk.Button(
            top_container,
            text="ADD",
            font=("Rubik", 10),
            command= lambda: self.add_url(self.url_entry.get()),
            width=7,
        ).pack(side=tk.LEFT)

        middle_container = tk.Frame(self)
        middle_container.pack(side=tk.TOP, fill=tk.Y)

        self.list_box = tk.Listbox(middle_container, bg="lightgrey", fg="blue", selectbackground="lightyellow", selectforeground="black", font=("Rubik", 12), width=64, height=30)
        self.list_box.pack(pady=10)
        # Vincular evento de doble clic a la función remove_url
        self.list_box.bind("<Double-Button-1>", self.remove_url)

        # Crear una barra de desplazamiento horizontal
        scrollbar_x = tk.Scrollbar(middle_container, orient="horizontal", command=self.list_box.xview)
        scrollbar_x.pack(side=tk.LEFT, pady=10, fill=tk.X, expand=True)
        self.list_box.config(xscrollcommand=scrollbar_x.set)

        bottom_container = tk.Frame(self)
        bottom_container.pack(side=tk.TOP, fill=tk.Y)

        tk.Button(
            bottom_container,
            text="DOWNLOAD",
            font=("Rubik", 12),
            command=lambda: self.download_media(),
            width=20
        ).pack(side=tk.LEFT, padx=17)

        tk.Button(
            bottom_container,
            text="CLEAN",
            font=("Rubik", 12),
            command=lambda: self.clean_list(),
            width=20
        ).pack(side=tk.LEFT, padx=18)

        tk.Button(
            bottom_container,
            text="SETTINGS",
            font=("Rubik", 12),
            command=lambda: self.open_settings(),
            width=20
        ).pack(side=tk.LEFT, padx=17)

    def add_url(self, url: str) -> None:
        if url:
            data = self.get_url_data(url)
            if data and data['duration'] != 'N/A':
                data['duration'] = f"{ (data['duration']//60)//60} : {(data['duration']//60)%60} : {data['duration']%60}"
            self.list_box.insert(tk.END, f"Title:   {data['title']},      Duration:   {data['duration']}")
            self.url_entry.delete(0, tk.END)

    def get_url_data(self, url: str) -> dict:
        if url:
            dl = MediaDownloader()
            return dl.get_info(url)

    def remove_url(self, event):
        index = self.list_box.curselection()
        if index:
            self.list_box.delete(index)

    def clean_list(self):
        self.list_box.delete(0, tk.END)

    def open_settings(self):
        print("Goto Settings")

    def download_media(self):
        urls = self.list_box.get(0, tk.END)
        if urls != ():
            dl = MediaDownloader()
            dl.set_urls(urls)
            dl.download_media()
            self.clean_list()
            messagebox.showinfo(
                "Media Catcher",
                "Media downloaded successfully",
            )
