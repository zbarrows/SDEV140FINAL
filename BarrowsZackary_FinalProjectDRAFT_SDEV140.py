#Program by Zac Barrows V1.6



from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.ttk import Checkbutton

root = Tk()
root.geometry("750x330")
root.title("Take-Out Ramen Eatery")


def place_order():
    total = 0  

    if name.get() == "" or phone.get() == "":
        tmsg.showerror("Ramen take-out", "Please enter all details")
    else:
        if size.get() == -1:
            tmsg.showerror("Ramen take-out", "Please select bowl-size")
            return
        else:
            selected_size = size_list[size.get()]
            selected_size_price = size_dict[selected_size]

            total = total + selected_size_price

        if noodle.get() == -1:
            tmsg.showerror("Ramen take-out", "Please select noodle type:")
            return
        else:
            selected_noodle = noodle_list[noodle.get()]
            selected_noodle_price = noodle_dict[selected_noodle]

            total = total + selected_noodle_price

        if Beef.get() == 1:
            total = total + toppings_price[0]
        if Chicken.get() == 1:
            total = total + toppings_price[1]
        if Boiled_egg.get() == 1:
            total = total + toppings_price[2]
        if Green_onion.get() == 1:
            total = total + toppings_price[3]

        tmsg.showinfo("Ramen take-out: ", f"Order Placed Successfully"
        f"\nName - {name.get()}\nPhone Number - {phone.get()}\nSize - {selected_size}\nNoodle - {selected_noodle}\nTotal - ${total}")


Label(root, text="Enter customer's name: ", font=("Times", 15)).place(x=15, y=15)
name = Entry(root, font=("Times", 14))
name.place(x=290, y=15)

Label(root, text="Enter Phone number: ", font=("Times", 15)).place(x=15, y=55)
phone = Entry(root, font=("Times", 14))
phone.place(x=290, y=55)

#Bowl Sizes_____________________________________________________________________
Label(root, text="Select Bowl size:", font=("Times", 15)).place(x=15, y=105)
Label(root, text="Price", font=("Times", 13)).place(x=15, y=135)
Label(root, text="Type", font=("Times", 13)).place(x=115, y=135)
size = IntVar()
size.set(-1)

size_dict = {"Small Bowl": 4, "Medium Bowl": 7, "Large Bowl": 12}
size_list = ["Small Bowl", "Medium Bowl", "Large Bowl"]
size_price = [4, 7, 12]

for i in range(0, len(size_list)):
    radio = Radiobutton(root, text=size_list[i], variable=size, value=i, font=("Times", 14))
    Label(root, text=f"${size_price[i]}").place(x=15, y=167 + i * 25)
    radio.place(x=95, y=165 + i * 25)

#Noodle Type_____________________________________________________________________
Label(root, text="Select Noodle type:", font=("Times", 15)).place(x=270, y=105)
Label(root, text="Price", font=("Times", 13)).place(x=275, y=135)
Label(root, text="Type", font=("Times", 13)).place(x=355, y=135)

noodle = IntVar()
noodle.set(-1)

noodle_dict = {"Thin noodles": 2.50, "Thick noodles": 3, "Rice noodles": 4}
noodle_list = ["Thin noodles", "Thick noodles", "Rice noodles"]
noodle_price = [2.50, 3, 4]

for i in range(0, len(noodle_list)):
    radio = Radiobutton(root, text=noodle_list[i], variable=noodle, value=i, font=("Comic Sans Ms", 11))
    Label(root, text=f"${noodle_price[i]}").place(x=275, y=167 + i * 25)
    radio.place(x=355, y=165 + i * 25)


#Toppings_____________________________________________________________________
Label(root, text="Select Topping:", font=("Times", 15)).place(x=525, y=105)
Label(root, text="Price", font=("Times", 13)).place(x=520, y=135)
Label(root, text="Type", font=("Times", 13)).place(x=640, y=135)

toppings_dict = {"Beef": 5, "Chicken": 3, "Boiled Egg": 2, "Green Onions": 2}
toppings_price = [t for t in toppings_dict.values()]
for i in range(0, len(toppings_price)):
    Label(root, text=f"${toppings_price[i]}").place(x=525, y=167 + i * 25)

#Beef
Beef = IntVar()
Beef_checkbutton = Checkbutton(root, text="Beef", variable=Beef)
Beef_checkbutton.place(x=605, y=165)

#Chicken
Chicken = IntVar()
Chicken_checkbutton = Checkbutton(root, text="Chicken", variable=Chicken)
Chicken_checkbutton.place(x=605, y=190)

#Boiled Egg
Boiled_egg = IntVar()
Boiled_egg_checkbutton = Checkbutton(root, text="Boiled Egg", variable=Boiled_egg)
Boiled_egg_checkbutton.place(x=605, y=215)

#Green onion
Green_onion = IntVar()
Green_onion_checkbutton = Checkbutton(root, text="Green Onions", variable=Green_onion)
Green_onion_checkbutton.place(x=605, y=240)


#Order button_____________________________________________________________________
Button(root, text="Place order", font=("Times", 13), width=45, command=place_order).place(x=15, y=285)

# Exit Button
Button(root, text="Exit", font=("Times", 13), width=20, command=quit).place(x=505, y=285)

root.mainloop()

