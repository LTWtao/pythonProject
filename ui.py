# 创建一个下拉式菜单
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.tix import TList
from db import PersonDb

win = Tk()
win.title("党支部管理系统")
win.geometry('800x500+300+200')
mainmenu = Menu(win)
filemenu = Menu(mainmenu, tearoff=False)
filemenu.add_command(label="导入")
filemenu.add_command(label="导出")
filemenu.add_command(label="保存")
filemenu.add_separator()
filemenu.add_command(label="退出", command=win.quit)
mainmenu.add_cascade(label="文件", menu=filemenu)
mainmenu.add_cascade(label="新建党支部", menu=filemenu)
win.config(menu=mainmenu)


class TimeSearchPage:
    pass


# class ShowPage1:
#     sbar1 = tk.Scrollbar(win)
#     sbar1.pack(side=RIGHT, fill=Y)
#     mylist = tk.Listbox(win, yscrollcommand=sbar1.set)
#     Persons = StudnetDb.read_person(win)
#     for person in Persons:
#         for a in person:
#             mylist.insert(END, a + " ")
#         mylist.insert(END, '\n')
#     mylist.pack(fill=BOTH)
#     sbar1.config(command=mylist.yview)

def treeview_sort_column( tv, col, reverse):  # Treeview、列名、排列方式
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    print(tv.get_children(''))
    l.sort(reverse=reverse)  # 排序方式
    # rearrange items in sorted positions
    for index, (val, k) in enumerate(l):  # 根据排序后索引移动
        tv.move(k, '', index)
        print(k)
    tv.heading(col, command=lambda: treeview_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题



class ShowPage2:
    def __init__(self):
        pass


    # # 给treeview排序函数
    # def treeview_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
    #     l = [(tv.set(k, col), k) for k in tv.get_children('')]
    #     print(tv.get_children(''))
    #     l.sort(reverse=reverse)  # 排序方式
    #     # rearrange items in sorted positions
    #     for index, (val, k) in enumerate(l):  # 根据排序后索引移动
    #         tv.move(k, '', index)
    #         print(k)
    #     tv.heading(col, command=lambda: self.treeview_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题


    # 创建frm1，包含按钮模块。
    frm1 = tk.Frame(win)
    frm1.pack(side='top')
    tk.Label(frm1, text='frm1_操作功能区保留').pack()
    # 创建frm2，包含显示列表块。
    frm2 = tk.Frame(win)
    frm2.pack()

    # 引用Treeview模块展示表。
    columns = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
    tree_view = ttk.Treeview(frm2, show='headings', columns=columns)
    tree_view.column('a', width=100, anchor='center')
    tree_view.column('b', width=100, anchor='center')
    tree_view.column('c', width=100, anchor='center')
    tree_view.column('d', width=100, anchor='center')
    tree_view.column('e', width=100, anchor='center')
    tree_view.column('f', width=100, anchor='center')
    tree_view.column('g', width=100, anchor='center')
    tree_view.column('h', width=100, anchor='center')
    tree_view.heading('a', text='姓名', command=lambda: treeview_sort_column(tree_view, 'a', False))
    tree_view.heading('b', text='所属部门', command=lambda: treeview_sort_column(tree_view, 'b', False))
    tree_view.heading('c', text='职务')
    tree_view.heading('d', text='党支部')
    tree_view.heading('e', text='党支部职务')
    tree_view.heading('f', text='任职时间')
    tree_view.heading('g', text='离任时间')
    tree_view.heading('h', text='其他')
    tree_view.pack(fill=tk.BOTH, expand=True)

    # for col in columns:  # 给所有标题加（循环上边的“手工”）
    #     tree_view.heading(col, text=col, command=lambda _col=col: treeview_sort_column(tree_view, _col, False))
    # tree_view.heading('a', text='123', command=lambda: treeview_sort_column(tree_view, 'a', False))

    # 给列表加上数据
    # tree_view.insert('', 'end', values=[1,1,1,1,1,1,1,1,])
    Persons = PersonDb()
    Persons_data = Persons.read_person()
    index = 0
    for person in Persons_data:
        tree_view.insert('', index + 1, values=(
            person[0], person[1], person[2], person[3], person[4], person[5], person[6], person[7]
        ))

    # 给列表加上循环键





class InsertPage:
    pass


class NewPartyPage:
    pass


class TimeSearchPage:
    pass


class PartySearchPage:
    pass


if __name__ == '__main__':
    win.mainloop()
