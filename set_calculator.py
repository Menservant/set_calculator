from tkinter import *
from tkinter import messagebox
import itertools
import re


def show_var():
    messagebox.showinfo("Result", f_set.get() + " " + s_set.get())


def union():
    f_res_set = set(str(f_set.get()).split(","))
    s_res_set = set(str(s_set.get()).split(","))
    f_res_set.update(f_res_set.union(s_res_set))
    return messagebox.showinfo("Result", f_res_set)


def intersection():
    f_res_set = set(str(f_set.get()).split(","))
    s_res_set = set(str(s_set.get()).split(","))
    result = f_res_set.intersection(s_res_set)
    return messagebox.showinfo("Result", result)


def difference():
    f_res_set = set(str(f_set.get()).split(","))
    s_res_set = set(str(s_set.get()).split(","))
    result = f_res_set.difference(s_res_set)
    return messagebox.showinfo("Result", result)


def symmetric_difference():
    f_res_set = set(str(f_set.get()).split(","))
    s_res_set = set(str(s_set.get()).split(","))
    result = f_res_set.symmetric_difference(s_res_set)
    return messagebox.showinfo("Result", result)


def cartesian_product():
    f_res_set = set(str(f_set.get()).split(","))
    s_res_set = set(str(s_set.get()).split(","))
    new_lst = []
    for el in itertools.product(f_res_set, s_res_set):
        new_lst.append(el)
    return messagebox.showinfo("Result", new_lst)


def addition():
    unique_res_set = set(str(unique_set.get()).split(","))
    f_res_set = set(str(f_set.get()).split(","))
    result = unique_res_set - f_res_set
    return messagebox.showinfo("Result", result)


def appeal():
    res_binary_relationship = str(binary_relationship1_entry.get())
    template = r'\([\d\w]+,[\d\w]+\)'
    re_binary_relationship = re.findall(template, res_binary_relationship)
    lst_res = [el[1:-1] for el in re_binary_relationship]
    result = ', '.join(['({}, {})'.format(el[1], el[0]) for el in [ll.split(',') for ll in lst_res]])
    return messagebox.showinfo("Result", result)


def composition():
    res_binary_relationship1 = str(binary_relationship1_entry.get())
    res_binary_relationship2 = str(binary_relationship2_entry.get())
    template = r'\([\d\w]+,[\d\w]+\)'
    re_binary_relationship1 = set(re.findall(template, res_binary_relationship1)[0][1:-1].split(","))
    re_binary_relationship2 = set(re.findall(template, res_binary_relationship2)[0][1:-1].split(","))
    result = re_binary_relationship1.symmetric_difference(re_binary_relationship2)
    return messagebox.showinfo("Result", result)


root = Tk()
root.title("Set calculator")
root.configure(background='#abf')

f_set = StringVar()
s_set = StringVar()
unique_set = StringVar()
binary_relationship1 = StringVar()
binary_relationship2 = StringVar()

f_set_entry = Entry(text="Enter first set", textvariable=f_set, fg="#000", bg="#abf", font="16")
s_set_entry = Entry(text="Enter second set", textvariable=s_set, fg="#000", bg="#abf", font="16")
unique_set_entry = Entry(text="Enter unique set", textvariable=unique_set, fg="#000", bg="#abf", font=16)
binary_relationship1_entry = Entry(text="Enter unique set", textvariable=binary_relationship1, fg="#000", bg="#abf",
                                   font=16)
binary_relationship2_entry = Entry(text="Enter unique set", textvariable=binary_relationship2, fg="#000", bg="#abf",
                                   font=16)

f_set_entry.insert(0, "Enter first set")
s_set_entry.insert(0, "Enter second set")
unique_set_entry.insert(0, "Enter unique set")
binary_relationship1_entry.insert(0, "Enter first binary relationship")
binary_relationship2_entry.insert(0, "Enter second binary relationship")

f_set_entry.grid(row=0, column=1, padx=5, pady=5)
s_set_entry.grid(row=1, column=1, padx=5, pady=5)
unique_set_entry.grid(row=2, column=1, padx=5, pady=5)
binary_relationship1_entry.grid(row=5, column=1, padx=5, pady=5)
binary_relationship2_entry.grid(row=6, column=1, padx=5, pady=5)

union_button = Button(root, text="Union", command=union, pady=8, padx=10, foreground="#000", background="#abf",
                      activebackground="#000", activeforeground="#fff", width=20, height=3, relief=GROOVE)
intersection_button = Button(root, text="Intersection", command=intersection, pady=8, padx=10, foreground="#000",
                             relief=GROOVE,
                             background="#abf", activebackground="#000", activeforeground="#fff", width=20, height=3)
difference_button = Button(root, text="Difference", command=difference, pady=8, padx=10, foreground="#000",
                           relief=GROOVE,
                           background="#abf", activebackground="#000", activeforeground="#fff", width=20, height=3)
symmetric_difference_button = Button(root, text="Symmetric difference", command=symmetric_difference, pady=8, padx=10,
                                     foreground="#000", width=20, height=3, relief=GROOVE,
                                     background="#abf", activebackground="#000", activeforeground="#fff")
cartesian_product_button = Button(root, text="Cartesian product", command=cartesian_product, pady=8, padx=10,
                                  foreground="#000", width=20, height=3, relief=GROOVE,
                                  background="#abf", activebackground="#000", activeforeground="#fff")
addition_button = Button(root, text="Addition\n (first and unique set)", command=addition, pady=8, padx=10,
                         foreground="#000",
                         background="#abf", activebackground="#000", activeforeground="#fff", width=20, height=3,
                         relief=GROOVE)
appeal_button = Button(root, text="Appeal", command=appeal, pady=8, padx=10, foreground="#000", background="#abf",
                       activebackground="#000", activeforeground="#fff", width=20, height=3, relief=GROOVE)
composition_button = Button(root, text="Composition", command=composition, pady=8, padx=10, foreground="#000",
                            background="#abf",
                            activebackground="#000", activeforeground="#fff", width=20, height=3, relief=GROOVE)

union_button.grid(row=3, column=3, padx=5, pady=5, sticky="e")
intersection_button.grid(row=3, column=4, padx=5, pady=5, sticky="e")
difference_button.grid(row=4, column=3, padx=5, pady=5, sticky="e")
symmetric_difference_button.grid(row=4, column=4, padx=5, pady=5, sticky="e")
cartesian_product_button.grid(row=3, column=5, padx=5, pady=5, sticky="e")
addition_button.grid(row=4, column=5, padx=5, pady=5, sticky="e")
appeal_button.grid(row=6, column=5, padx=5, pady=5, sticky="e")
composition_button.grid(row=7, column=5, padx=5, pady=5, sticky="e")

root.mainloop()
