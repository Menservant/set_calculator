from tkinter import *
from tkinter import messagebox
import itertools


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


root = Tk()
root.title("Set calculator")
root.configure(background='#abf')

f_set = StringVar()
s_set = StringVar()
unique_set = StringVar()

f_set_entry = Entry(text="Enter first set", textvariable=f_set, fg="#000", bg="#abf", font="16")
s_set_entry = Entry(text="Enter second set", textvariable=s_set, fg="#000", bg="#abf", font="16")
unique_set_entry = Entry(text="Enter unique set", textvariable=unique_set, fg="#000", bg="#abf", font=16)

f_set_entry.insert(0, "Enter first set")
s_set_entry.insert(0, "Enter second set")
unique_set_entry.insert(0, "Enter unique set")

f_set_entry.grid(row=0, column=1, padx=5, pady=5)
s_set_entry.grid(row=1, column=1, padx=5, pady=5)
unique_set_entry.grid(row=2, column=1, padx=5, pady=5)

union_button = Button(root, text="Union", command=union, pady=8, padx=10, foreground="#000", background="#abf",
                      activebackground="#000", activeforeground="#fff", width=20, height=3)
intersection_button = Button(root, text="Intersection", command=intersection, pady=8, padx=10, foreground="#000",
                             background="#abf", activebackground="#000", activeforeground="#fff", width=20, height=3)
difference_button = Button(root, text="Difference", command=difference, pady=8, padx=10, foreground="#000",
                           background="#abf", activebackground="#000", activeforeground="#fff", width=20, height=3)
symmetric_difference_button = Button(root, text="Symmetric difference", command=symmetric_difference, pady=8, padx=10,
                                     foreground="#000", width=20, height=3,
                                     background="#abf", activebackground="#000", activeforeground="#fff")
cartesian_product_button = Button(root, text="Cartesian product", command=cartesian_product, pady=8, padx=10,
                                  foreground="#000", width=20, height=3,
                                  background="#abf", activebackground="#000", activeforeground="#fff")
addition_button = Button(root, text="Addition", command=addition, pady=8, padx=10,
                         foreground="#000",
                         background="#abf", activebackground="#000", activeforeground="#fff", width=20, height=3)

union_button.grid(row=3, column=3, padx=5, pady=5, sticky="e")
intersection_button.grid(row=3, column=4, padx=5, pady=5, sticky="e")
difference_button.grid(row=4, column=3, padx=5, pady=5, sticky="e")
symmetric_difference_button.grid(row=4, column=4, padx=5, pady=5, sticky="e")
cartesian_product_button.grid(row=3, column=5, padx=5, pady=5, sticky="e")
addition_button.grid(row=4, column=5, padx=5, pady=5, sticky="e")
union_button.size()
root.mainloop()
