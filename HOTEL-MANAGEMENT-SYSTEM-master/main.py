from tkinter import *
import check_in_ui
import check_out
import get_info
import customer_info
import os


class Hotel:
    def __init__(self, root):
        self.root = root
        pad = 3
        self.root.title("Hotel Karol")
        self.root.geometry(
            "{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))

        # Stworzenie głównej ramki 
        top = Frame(self.root)
        top.pack(side="top")

        # stworzenie ramki do dodania przycisków
        bottom = Frame(self.root)
        bottom.pack(side="top")

        # wyświetlanie wiadomosci
        self.label = Label(top, font=('arial', 50, 'bold'), text="Witamy", fg="#15d3ba", anchor="center")
        self.label.grid(row=0, column=3)

        # stworzenie guzika "zamelduj się"
        self.check_in_button = Button(bottom, text="Zamelduj sie", font=('', 20), bg="#15d3ba", relief=RIDGE, height=2,
                                      width=50,
                                      fg="black", anchor="center",
                                      command=check_in_ui.check_in_ui_fun)  # wywolanie funkcji zamelduj siez pliku check_in.py
        self.check_in_button.grid(row=0, column=2, padx=10, pady=10)

        # Stworzenie guzika wymelduj się
        self.check_out_button = Button(bottom, text="Wymelduj sie", font=('', 20), bg="#15d3ba", relief=RIDGE, height=2,
                                       width=50, fg="black", anchor="center",
                                       command=check_out.check_out_ui)  # wywolanie funkcji wymelduj się
        self.check_out_button.grid(row=1, column=2, padx=10, pady=10)

        # Stworzenie guzika informację o pokojach
        self.room_info_button = Button(bottom, text="Informacje o pokojach", font=('', 20), bg="#15d3ba", relief=RIDGE,
                                       height=2,
                                       width=50, fg="black", anchor="center",
                                       command=get_info.get_info_ui)  # wywolanie funkcji informacje o pokojach
        self.room_info_button.grid(row=2, column=2, padx=10, pady=10)

        # stworzenie guzika informację o gościach
        self.get_info_button = Button(bottom, text="Informacje o gościach", font=('', 20), bg="#15d3ba",
                                      relief=RIDGE,
                                      height=2, width=50, fg="black", anchor="center",
                                      command=customer_info.customer_info_ui)
        # wywolanie funkcji informacje o klientach z pliku customer_info.py
        self.get_info_button.grid(row=3, column=2, padx=10, pady=10)

        # wyjście z programu
        self.exit_button = Button(bottom, text="wyjdz", font=('', 20), bg="#15d3ba", relief=RIDGE, height=2, width=50,
                                  fg="black",
                                  anchor="center", command=quit)
        self.exit_button.grid(row=4, column=2, padx=10, pady=10)


def home_ui():
    root = Tk()
    application = Hotel(root)
    root.mainloop()


if __name__ == '__main__':
    home_ui()
