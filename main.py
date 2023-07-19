from tkinter import *
import customtkinter
from datetime import datetime


def standard_label(input_master, input_text, input_row, input_col, input_font=None, paddingy=10, paddingx=10,) -> object:
    default_label = customtkinter.CTkLabel(master=input_master, text=input_text)
    if input_font != None:
        default_label.configure(font=input_font)
    default_label.grid(row=input_row, column=input_col, pady=paddingy, padx=paddingx)


def new_window_instance(smoked_cigs, money_spend, time_wasted, interest_money):

    def go_back():
        new_window.destroy()
        root.deiconify()

    x = root.winfo_x()
    y = root.winfo_y()

    root.withdraw()

    new_window = customtkinter.CTkToplevel(root)
    new_window.title("QuitToSafe Summary")
    new_window.geometry("+%d+%d" % (x, y))
    new_window.geometry("600x600")

    new_frame = customtkinter.CTkFrame(master=new_window)

    new_logo_label = standard_label(new_frame, "QuitToSave", 0, 0, ("Roboto", 24))

    smoked_cigs_label = standard_label(new_frame, "Total of smoked cigarettes: ", 1, 0)
    smoked_cigs_result_label = standard_label(new_frame, smoked_cigs, 1, 1, ("Roboto", 14, 'bold'), 20, 35)

    money_spend_label = standard_label(new_frame, "Total of money spend: ", 2, 0)
    money_spend_result_label = standard_label(new_frame, f"{int(money_spend)}$", 2, 1, ("Roboto", 14, 'bold'), 10, 35)

    time_wasted_label = standard_label(new_frame, "Total of time wasted: ", 3, 0)
    time_wasted_result_label = standard_label(new_frame, f"{int(time_wasted)} days", 3, 1, ("Roboto", 14, 'bold'), 20,
                                              35)

    invested_money_label = standard_label(new_frame, "If you had invested: ", 4, 0)
    invested_money_result_label = standard_label(new_frame, f"{int(interest_money)}$ ", 4, 1, ("Roboto", 14, 'bold'), 20,
                                              35)

    back_button = customtkinter.CTkButton(master=new_frame, text="Go back", command=go_back).grid(row=5,
                                                                                                         column=0,
                                                                                                         columnspan=2,
                                                                                                         pady=10,
                                                                                                         padx=10)
    new_frame.place(relx=0.5, rely=0.5, anchor=CENTER)


def calculation():
    consume_value = consume_input.get()
    cigs_per_pack_value = int(cigs_per_pack_input.get())
    price_per_pack_value = int(price_per_pack_input.get())

    # Calculation date --> day count
    begin_value = datetime.strptime(period_input.get(), "%d.%m.%Y")
    current_date = datetime.now()
    diff = current_date - begin_value
    days_passed = diff.days

    # Calculation smoked cigs liftime
    smoked_cigs = int(consume_value) * int(days_passed)

    # Calculation money
    money_spend = (smoked_cigs / cigs_per_pack_value) * price_per_pack_value

    # Calculation time waste
    time_wasted = ((smoked_cigs * 5) / 60) / 24

    # Calculation Zines Zins
    yearly_interest_rate = 7
    months = days_passed / 30.436
    monthly_saving = int(consume_value) / int(cigs_per_pack_value) * price_per_pack_value * 30.436
    monthly_interest_rate = 100 * (pow(1 + yearly_interest_rate / 100, 1 / 12) - 1)
    interest_factor = 1 + (monthly_interest_rate / 100)

    interest_money = monthly_saving * interest_factor * (interest_factor ** months - 1) / (interest_factor - 1)

    new_window_instance(smoked_cigs, money_spend, time_wasted, interest_money)


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("QuitToSafe")

# Tkinter App pops up in the middle of your monitor
app_width = 600
app_height = 600

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

root.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

frame = customtkinter.CTkFrame(master=root)

logo_label = standard_label(frame, "QuitToSave", 0, 0, ("Roboto", 24))

consume_label = standard_label(frame, "Consume per day:", 1, 0)

consume_input = customtkinter.CTkEntry(master=frame, placeholder_text="15 cigs")
consume_input.grid(row=1, column=1, pady=10, padx=10)

cigs_per_pack_label = standard_label(frame, "Cigs per pack:", 2, 0)

cigs_per_pack_input = customtkinter.CTkEntry(master=frame, placeholder_text="20 cigs")
cigs_per_pack_input.grid(row=2, column=1, pady=10, padx=10)

price_per_pack_label = standard_label(frame, "Price per pack:", 3, 0)

price_per_pack_input = customtkinter.CTkEntry(master=frame, placeholder_text="8$")
price_per_pack_input.grid(row=3, column=1, pady=10, padx=10)

period_label = standard_label(frame, "Begin:", 4, 0)

period_input = customtkinter.CTkEntry(master=frame, placeholder_text="12.06.2023")
period_input.grid(row=4, column=1, pady=10, padx=10)

# Configure Button
calculate_button = customtkinter.CTkButton(master=frame, text="Calculate", command=calculation).grid(row=5, column=0,
                                                                                                     columnspan=2,
                                                                                              pady=10, padx=10)

frame.place(relx=0.5, rely=0.5, anchor=CENTER)
root.mainloop()
