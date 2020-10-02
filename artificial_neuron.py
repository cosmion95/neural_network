from functions import entry as entry_functions, activation as activation_functions
import numpy as np
import tkinter as tk
from tkinter import ttk



#liste valori
inputs = []
entry_functions_list = []
activation_functions_list = []

#posibile variabile
teta = 0
a = 1
g = 1

entry_functions_list.clear()
entry_functions_list.append(("Suma", entry_functions.suma(inputs)))
entry_functions_list.append(("Produs", entry_functions.produs(inputs)))
entry_functions_list.append(("Minim", entry_functions.minim(inputs)))
entry_functions_list.append(("Maxim", entry_functions.maxim(inputs)))

activation_functions_list.clear()
activation_functions_list.append(("Treapta", activation_functions.treapta(0, teta)))
activation_functions_list.append(("Sigmoidala", activation_functions.sigmoidala(0, teta, g)))
activation_functions_list.append(("Signum", activation_functions.signum(0, teta)))
activation_functions_list.append(("Tangenta hiperbolica", activation_functions.tangenta_hiperbolica(0, teta, g)))
activation_functions_list.append(("Rampa", activation_functions.rampa(0, teta, a)))

#gui
main_window = tk.Tk()
main_window.title("Neuronul artificial")

binar = tk.BooleanVar()

# campuri folosite la fiecare actiune, definite la inceput

entry_functions_combo = ttk.Combobox(main_window)
entry_functions_combo.grid(column=2, row=7)
entry_functions_combo['values'] = ["Suma", "Produs", "Minim", "Maxim"]
entry_functions_combo.current(0)

ef_value = tk.Label(main_window, text=str(entry_functions_list[entry_functions_combo.current()][1]))
ef_value.grid(column=2, row=15)

act_functions_combo = ttk.Combobox(main_window)
act_functions_combo.grid(column=2, row=9)
act_functions_combo['values'] = ["Treapta", "Sigmoidala", "Signum", "Tangenta hiperbolica", "Rampa" ]
act_functions_combo.current(0)

af_value = tk.Label(main_window, text=str(activation_functions_list[act_functions_combo.current()][1]))
af_value.grid(column=2, row=16)

out_value = tk.Label(main_window, text=str(activation_functions_list[act_functions_combo.current()][1]))
out_value.grid(column=2, row=17)

teta_value = tk.Entry(main_window)
teta_value.grid(column=2, row=11)
teta_value.insert(0, teta)

g_value = tk.Entry(main_window)
g_value.grid(column=2, row=12)
g_value.insert(0, g)

a_value = tk.Entry(main_window)
a_value.grid(column=2, row=13)
a_value.insert(0, a)

binar_value = tk.Checkbutton(main_window, variable=binar)
binar_value.grid(column=2, row=14)

#actualizarea valorilor afisate
def recalculate_entry_functions():
    entry_functions_list.clear()
    entry_functions_list.append(("Suma", entry_functions.suma(inputs)))
    entry_functions_list.append(("Produs", entry_functions.produs(inputs)))
    entry_functions_list.append(("Minim", entry_functions.minim(inputs)))
    entry_functions_list.append(("Maxim", entry_functions.maxim(inputs)))

#recalculare valoare functii de activare
def recalculate_activation_functions():
    activation_functions_list.clear()
    activation_functions_list.append(("Treapta", activation_functions.treapta(float(ef_value.cget("text")), float(teta_value.get()))))
    activation_functions_list.append(("Sigmoidala", activation_functions.sigmoidala(float(ef_value.cget("text")), float(teta_value.get()), float(g_value.get()))))
    activation_functions_list.append(("Signum", activation_functions.signum(float(ef_value.cget("text")), float(teta_value.get()))))
    activation_functions_list.append(("Tangenta hiperbolica", activation_functions.tangenta_hiperbolica(float(ef_value.cget("text")), float(teta_value.get()), float(g_value.get()))))
    activation_functions_list.append(("Rampa", activation_functions.rampa(float(ef_value.cget("text")), float(teta_value.get()), float(a_value.get()))))


def recalculate_functions():
    recalculate_entry_functions()
    recalculate_activation_functions()

#adauga input
def add_input(i=0.0, w=0.0):
    inputs.append((i, w))
    recalculate_functions()
add_input()

#sterge input
def remove_input():
    inputs.pop()
    recalculate_functions()

#editare input
def edit_value(index, i, w):
    inputs[index] = (i, w)
    recalculate_functions()

def set_output_value():
    out_result = float(af_value.cget("text"))
    if binar.get():
        if activation_functions_list[act_functions_combo.current()][0] == 'Sigmoidala':
        # verific daca e sigmoidala 1 daca >= 0.5, 0 altfel
            if float(af_value.cget("text")) >= 0.5:
                out_result = 1
            else:
                out_result = 0
        elif activation_functions_list[act_functions_combo.current()][0] == 'Tangenta hiperbolica':
        # sau tangenta hiperbolica 1 daca >= 0, -1 altfel
            if float(af_value.cget("text")) >= 0:
                out_result = 1
            else:
                out_result = -1
        elif activation_functions_list[act_functions_combo.current()][0] == 'Rampa':
        # sau rampa 1 daca >=0, -1 altfel
            if float(af_value.cget("text")) >= 0:
                out_result = 1
            else:
                out_result = -1
    out_value.config(text=str(f'{out_result:.15f}'))

#recalculeaza functiile si modifica valorile afisate
def change_displayed_values():
    recalculate_entry_functions()
    recalculate_activation_functions()
    ef_value["text"] = str(f'{entry_functions_list[entry_functions_combo.current()][1]:.15f}')
    af_value["text"] = str(f'{activation_functions_list[act_functions_combo.current()][1]:.15f}')
    set_output_value()

# ****************** ------------- ENTRY VALUES ---------------------- ***********************


#values
inputs_entry = tk.Entry(main_window)
inputs_entry.grid(column=2, row=1)

#labels
inputs_label = tk.Label(main_window, text="Inputs:")
inputs_label.grid(column=1, row=0)

#scrollbars
inputs_list_sb = tk.Scrollbar(main_window)
inputs_list_sb.grid(column=2, row=2)

i_label = tk.Label(main_window, text="i:")
i_label.grid(column=1, row=4)

i_value = tk.Entry(main_window)
i_value.grid(column=2, row=4)

w_label = tk.Label(main_window, text="w:")
w_label.grid(column=1, row=5)

w_value = tk.Entry(main_window)
w_value.grid(column=2, row=5)

#configuring inputs list
inputs_list_lb = tk.Listbox(main_window, selectmode=tk.SINGLE)
inputs_list_lb.grid(column=1, row=2)

counter = 1
for item in inputs:
    inputs_list_lb.insert(tk.END, str(counter) + " - i[ " + str(item[0]) + " ] w[ " + str(item[1]) + " ]")
    counter += 1

inputs_entry.insert(0, len(inputs))

inputs_list_lb.config(yscrollcommand = inputs_list_sb.set)
inputs_list_sb.config(command=inputs_list_lb.yview)

#adding items to inputs list
def add_item_to_inputs_list():
    add_input()
    inputs_list_lb.insert(tk.END, str(len(inputs)) + " - i[ " + str(inputs[-1][0]) + " ] w[ " + str(inputs[-1][1]) + " ]")
    inputs_entry.delete(0,tk.END)
    inputs_entry.insert(0, len(inputs))
    change_displayed_values()

#removing items from inputs list
def remove_item_from_inputs_list():
    remove_input()
    inputs_list_lb.delete(len(inputs))
    inputs_entry.delete(0,tk.END)
    inputs_entry.insert(0, len(inputs))
    change_displayed_values()

#setting a number of items in the inputs list
def set_specific_inputs(event):
    count = int(inputs_entry.get())
    if count < len(inputs):
        if count < 1:
            count = 1
            while len(inputs) > count:
                remove_item_from_inputs_list()
        else:
            while len(inputs) > count:
                remove_item_from_inputs_list()
    else:
        while len(inputs) < count:
            add_item_to_inputs_list()
    change_displayed_values()

def select_entry_item(event):
    if inputs_list_lb.curselection():
        selected_index = inputs_list_lb.curselection()[0]

        i_value.delete(0,tk.END)
        i_value.insert(0, inputs[selected_index][0])

        w_value.delete(0,tk.END)
        w_value.insert(0, inputs[selected_index][1])

        i_label.config(text=str(selected_index+1) + " - i: ")
        w_label.config(text=str(selected_index+1) + " - w: ")

#modify an item
def set_entry_values():
    try:
        selected_index = int(i_label.cget("text")[0])-1
        i = float(i_value.get())
        w = float(w_value.get())
        edit_value(selected_index, i, w)
        inputs_list_lb.delete(selected_index)
        inputs_list_lb.insert(selected_index, str(selected_index+1) + " - i[ " + str(i) + " ] w[ " + str(w) + " ]")
        change_displayed_values()
    except:
        print("error")

inputs_entry.bind('<Return>', set_specific_inputs)

inputs_list_lb.bind('<<ListboxSelect>>', select_entry_item)

#buttons
add_input_button = tk.Button(main_window, text="+", command=add_item_to_inputs_list)
add_input_button.grid(column=3, row=1)

remove_input_button = tk.Button(main_window, text="-", command=remove_item_from_inputs_list)
remove_input_button.grid(column=1, row=1)

set_iw_bt = tk.Button(main_window, text="OK", command=set_entry_values)
set_iw_bt.grid(column=3, row=5)

# ****************** ------------- ENTRY FUNCTIONS ---------------------- ***********************

ef_label = tk.Label(main_window, text="Entry function:")
ef_label.grid(column=1, row=7)


ef_label2 = tk.Label(main_window, text="Entry function value:")
ef_label2.grid(column=1, row=15)

#aleg o alta functie de intrare
def select_entry_function(event):
    ef_value.config(text=str(entry_functions_list[entry_functions_combo.current()][1]))
    change_displayed_values()

entry_functions_combo.bind("<<ComboboxSelected>>", select_entry_function)


# ****************** ------------- ACTIVATION FUNCTIONS ---------------------- ***********************

def modify_variable(event):
    change_displayed_values()

###### TETA
teta_label = tk.Label(main_window, text="Teta:")
teta_label.grid(column=1, row=11)
teta_value.bind('<Return>', modify_variable)

###### g
g_label = tk.Label(main_window, text="g:")
g_label.grid(column=1, row=12)
g_value.bind('<Return>', modify_variable)

####### a

a_label = tk.Label(main_window, text="a:")
a_label.grid(column=1, row=13)
a_value.bind('<Return>', modify_variable)

af_label = tk.Label(main_window, text="Activation function:")
af_label.grid(column=1, row=9)

binar_label = tk.Label(main_window, text="Binar:")
binar_label.grid(column=1, row=14)

af_label2 = tk.Label(main_window, text="Activation function value:")
af_label2.grid(column=1, row=16)

#aleg o alta functie de activare
def select_activ_function(event):
    af_value.config(text=str(activation_functions_list[act_functions_combo.current()][1]))
    change_displayed_values()

act_functions_combo.bind("<<ComboboxSelected>>", select_activ_function)


# OUTPUT

out_label = tk.Label(main_window, text="Output value:")
out_label.grid(column=1, row=17)


main_window.mainloop()