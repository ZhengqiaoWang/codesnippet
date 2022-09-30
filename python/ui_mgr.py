'''
Author: 王政乔 me@zhengqiao.wang
Date: 2022-09-30 19:52:19
LastEditors: 王政乔 me@zhengqiao.wang
LastEditTime: 2022-09-30 19:52:21
FilePath: /codesnippet/python/ui_mgr.py
Description: 一个用于简单的用于自动化办公的生成工具界面
Website: https://www.zhengqiao.wang
'''

import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog


class UIMgr:

    INPUT_PADDING_V = 50  # 多个INPUT之间的纵向间隔

    def __init__(self, title) -> None:
        self.__input_pos_x = 20
        self.__input_pos_y = 40

        self.__input_dict = {}
        self.__cb_func = None
        self.__window = tk.Tk(className=title)

    def registInput(self, id: str, title: str, default_val=""):
        tk.Label(self.__window, text=title + ":", font=('黑体', 12)
                 ).place(x=self.__input_pos_x, y=self.__input_pos_y, anchor='nw')
        val_obj = tk.StringVar()
        val_obj.set(default_val)
        input_box = tk.Entry(
            self.__window, textvariable=val_obj, font=('黑体', 12), width=30)
        input_box.place(x=self.__input_pos_x + 200, y=self.__input_pos_y)
        self.__input_pos_y += self.INPUT_PADDING_V
        self.__input_dict[id] = val_obj

    def registPathSelect(self, id: str, title: str, default_val=""):
        tk.Label(self.__window, text=title + ":", font=('黑体', 12)
                 ).place(x=self.__input_pos_x, y=self.__input_pos_y, anchor='nw')
        val_obj = tk.StringVar()
        val_obj.set(default_val)
        input_box = tk.Entry(
            self.__window, textvariable=val_obj, font=('黑体', 12), width=30)
        input_box.place(x=self.__input_pos_x + 200, y=self.__input_pos_y)
        path_sel_btn = tk.Button(
            self.__window, text="...", command=lambda: self.__selPath(title, val_obj))
        path_sel_btn.place(x=self.__input_pos_x + 500, y=self.__input_pos_y)
        self.__input_dict[id] = val_obj
        self.__input_pos_y += self.INPUT_PADDING_V

    def __selPath(self, title, val_obj):
        path_ = tkinter.filedialog.askopenfilename(title=title)
        path_ = path_.replace("/", "\\\\")
        val_obj.set(path_)

    def registOnButtonClickCB(self, cb_func):
        self.__cb_func = cb_func

    def onButtonClick(self):
        self.__input_vals = {}
        for key, val in self.__input_dict.items():
            self.__input_vals[key] = val.get()
        self.__cb_func(**self.__input_vals)

    def show(self):
        gene = tk.Button(self.__window, text='OK', font=(
            '黑体', 12), bg='teal', width=20, height=4, command=self.onButtonClick)
        gene.place(x=100, y=self.__input_pos_y)
        self.__window.geometry('600x{}'.format(self.__input_pos_y + 100))
        self.__window.mainloop()

    def message(self, title, text):
        tk.messagebox.showinfo(title=title, message=text)
