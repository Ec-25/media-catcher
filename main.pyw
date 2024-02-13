import tkinter as tk
from screens.home import Home


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Media Catcher")
        self.geometry("800x800")
        self.iconbitmap("icon.ico")
        self.resizable(False, False)

        self.configure(bg="#ececec", padx=10, pady=10)

        container = tk.Frame(self)
        container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

        self.frames = {}

        for F in (Home,):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky=tk.NSEW)
        self.show_frame(Home)

    def show_frame(self, container):
        if container == "Home":
            frame = self.frames[Home]
            frame.tkraise()
        else:
            frame = self.frames[container]
            frame.tkraise()


if __name__ == "__main__":
    print("[APP]: Start Running ... ")
    app = App()
    app.mainloop()
    print("[APP]: Stop Running ... ")
    exit(0)
