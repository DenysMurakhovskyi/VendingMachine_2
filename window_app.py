import tkinter as tk
from tkinter import ttk, IntVar
import os, sys

sizes_coordinates = {0: (0.05, 0.15),
                     1: (0.05, 0.7),
                     2: (0.75, 0.15),
                     3: (0.67, 0.7)}

sizes_quantity = {0: (0.05, 0.15),
                  1: (0.05, 0.7),
                  2: (0.83, 0.15),
                  3: (0.83, 0.7)}

sizes_payment = {0: (0.05, 0.15),
                 1: (0.05, 0.7),
                 2: (0.75, 0.15),
                 3: (0.3, 0.7)}

place_qty = {0: (0.05, 0.15),
             1: (0.05, 0.35)}

prices = (25, 50, 150, 350)

font_aspect_ratio = 8
font_aspect_ratio_2 = 12


pins = {1: 26, 2: 16, 3: 12, 4: 6, 5: 5}
sizes = ['0.5 л', '1.5 л', '5 л', '19 л']
anchors = [tk.W, tk.W, tk.E, tk.E]


class Fullscreen_Window:
    def __init__(self):

        # инициализация основного окна
        self.tk = tk.Tk()
        self.tk.title("Clean water vending")

        # определение параметров экрана
        self.screen_width = self.tk.winfo_screenwidth()
        self.screen_height = self.tk.winfo_screenheight()

        # привязка кнопок
        self.tk.attributes('-fullscreen', True)
        self.tk.bind("<F11>", self.toggle_fullscreen)
        self.tk.bind("<F10>", self.end_fullscreen)
        self.tk.bind("<F12>", self.workend)

        # инициализация меток
        self.labels = [None] * 4

        # переменные процесса
        self._qty = 0
        self.size = 2

        # виджеты
        self.widgets = {
                        'qty1': ttk.Label(self.tk, text='К оплате', anchor=tk.W),
                        'qty2': ttk.Label(self.tk, text='1 x руб. = ', anchor=tk.W)}
        for item in ['qty1', 'qty2']:
            self.widgets[item].config(font='size, ' + str(int(self.screen_height / font_aspect_ratio_2)))

        # конфигурация параметров, запуск основного окна в полноэкранном режиме
        self._pressed_button = -1  # свойство - номер нажатой кнопки
        self.screen_num = 0  # номер текущего активного экрана
        self.state = True  # статус полного экрана
        self.tk.config(cursor="none")

        self.show_sizes()

    @property
    def pressed_button(self):
        return self._pressed_button

    @pressed_button.setter
    def pressed_button(self, value):
        if self.screen_num == 0:  # начальный экран автомата
            self.size = value
            self.screen_num += 1
            self.show_quantity_buttons()
            self.show_quantity_string(True)
        elif self.screen_num == 1:  # экран выбора количества
            if value == 1:
                self.clear_widgets()
                self.screen_num += 1
                self.show_payments()
            if value in [2, 3]:
                if value == 2:
                    self.qty += 1
                elif value == 3:
                    if self.qty > 1:
                        self.qty -= 1
        self._pressed_button = -1

    @property
    def qty(self):
        return self._qty

    @qty.setter
    def qty(self, value):
        self._qty = value
        self.widgets['qty2']['text'] = str(self.qty) + ' x ' + str(prices[self.size]) + ' руб. = ' \
                                       + str(self.qty * prices[self.size])

    @qty.getter
    def qty(self):
        return  self._qty

    def destroy_labels(self):
        for item in self.labels:
            if item:
                item.destroy()

    def make_labels(self, flags, coordinates, text):
        self.destroy_labels()

        # создание меток кнопок
        self.labels = [ttk.Label(self.tk, text=item[1], anchor=item[2]) if item[0] else None for item in
                       zip(flags, text, anchors)]
        for item in self.labels:
            if item:
                item.config(font='size, ' + str(int(self.screen_height / font_aspect_ratio)))

        for key in sizes_coordinates.keys():
            if self.labels[key]:
                self.labels[key].place(x=coordinates[key][0] * self.screen_width,
                                       y=coordinates[key][1] * self.screen_height)

    def show_quantity_string(self, flag):
        if flag:
            self.widgets['qty1'].place(x=place_qty[0][0] * self.screen_width, y=place_qty[0][1] * self.screen_height)
            self.widgets['qty2'].place(x=place_qty[1][0] * self.screen_width, y=place_qty[1][1] * self.screen_height)
            self.qty = 1

    def show_sizes(self):
        self.make_labels([True] * 4, sizes_coordinates, sizes)

    def show_quantity_buttons(self, event=None):
        self.destroy_labels()
        self.make_labels([False, True, True, True], sizes_quantity, ['', 'Ok', '+', '\u2212'])

    def show_payments(self, event=None):
        self.destroy_labels()
        self.make_labels([True, False, False, True], sizes_payment, ['Карта', '', '', 'Наличные'])

    def NFC_payment(self):
        pass

    def cash_payment(self):
        pass

    def clear_widgets(self):
        for key in self.widgets.keys():
            self.widgets[key].place_forget()

    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"

    def workend(self, event=None):
        sys.exit(0)
