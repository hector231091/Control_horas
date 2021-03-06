import tkinter as tk
from tkinter import messagebox

from input_control_plant import *

from input_control_plant import InputControlPlant
from input_worker_name import WorkerName
#from input_timetable import Timetable
from input_total_day_hours import Timetable
from input_calendar import Calendar

REGISTRY_FILE_NAME = "Registro_horas.csv"

# La función va a devolver la variable de verificación, y en función de su valor, luego se registrará en el archivo o no.
# Las variables deben ser "True" para que pueda registrar
def validate_register_dates(hours_control_plant, hours_timetable, worker_name, input_date):

    verification_variable_control_plant = True
    verification_variable_control_plant_hours_timetable = True
    verification_variable_worker_code = True
    verification_variable_hours_control_plant = True
    verification_variable_date = True

    verification_all_variables_true = True

    # En principio la validación de la fecha no sé si va a ser necesaria...

    # Validación del trabajador:
    # Ahora cogemos el nombre del trabajador, pero tendíamos que coger el código del trabajador
    if len(worker_name) == 0 or str(worker_name) == "Algo falla...":
        messagebox.showerror(title="Código del trabajador erróneo",
                             message="El código del trabajador introducido es erróneo")
        verification_variable_worker_code = False

    # Validación de la fecha
    if len(input_date) != 10:
        messagebox.showerror(title="Error en la fecha",
                             message="No se ha seleccionado ninguna fecha")
        verification_variable_date = False

    # Valicadión introduccion horario
    if len(str(hours_timetable)) == 0 or str(hours_timetable) == "-":
        messagebox.showerror(title="No has puesto el horario",
                             message="Debes introducir el horario del día de hoy para poder registrar")
        verification_variable_control_plant_hours_timetable = False

    # Valicadión introduccion control en planta
    if float(hours_control_plant) == 0:
        messagebox.showerror(title="Falta meter el control en planta",
                             message="Debes introducir el control en panta para poder registrar")
        verification_variable_control_plant = False

    # Validación de que las horas del control en planta y el horario sean iguales:
    if len(str(hours_control_plant)) != 0:
        if hours_control_plant != hours_timetable:
            messagebox.showerror(title="Horas mal introducidas",
                                 message="Para poder registrar, las horas del control en planta y del horario deben coincidir.")
            verification_variable_hours_control_plant = False

    if verification_True_of_variables(verification_variable_control_plant, \
                                      verification_variable_control_plant_hours_timetable, \
                                      verification_variable_worker_code, \
                                      verification_variable_hours_control_plant, \
                                      verification_variable_date) == True:
        verification_all_variables_true = True
    else:
        verification_all_variables_true = False

    return verification_all_variables_true

# Función para comprobar que las variables son todas True
def verification_True_of_variables(var_1, var_2, var_3, var_4, var_5):

    if var_1 == True and var_2 == True and var_3 == True and var_4 == True and var_5 == True:
        return True
    else:
        return False

# En esta función se va a registrar en el .csv todos los datos del programa.
def register():
    hours_control_plant = control_plant.hours_and_minutes_to_decimal()
    worker_name = workername.get_worker_code()
    hours_timetable = timetable.return_hours()

    input_date = calendar.return_date()

    # Comprobamos que todas las validaciones son True

    if validate_register_dates(hours_control_plant, hours_timetable, worker_name, input_date) == True:
        register_input(input_date, worker_name)
        clear()

def generate_input_to_register(date, worker_name):
    date = str(date)
    worker_name = str(worker_name)
    return date + ";" + worker_name + ";" + code_3 + ";" + str(control_plant.decimal_hours_code_3) + "\n" + \
           date + ";" + worker_name + ";" + code_8 + ";" + str(control_plant.decimal_hours_code_8) + "\n" + \
           date + ";" + worker_name + ";" + code_9 + ";" + str(control_plant.decimal_hours_code_9) + "\n" + \
           date + ";" + worker_name + ";" + code_15 + ";" + str(control_plant.decimal_hours_code_15) + "\n" + \
           date + ";" + worker_name + ";" + code_18 + ";" + str(control_plant.decimal_hours_code_18) + "\n" + \
           date + ";" + worker_name + ";" + code_19 + ";" + str(control_plant.decimal_hours_code_19) + "\n" + \
           date + ";" + worker_name + ";" + code_20 + ";" + str(control_plant.decimal_hours_code_20) + "\n" + \
           date + ";" + worker_name + ";" + code_21 + ";" + str(control_plant.decimal_hours_code_21) + "\n" + \
           date + ";" + worker_name + ";" + code_22 + ";" + str(control_plant.decimal_hours_code_22) + "\n" + \
           date + ";" + worker_name + ";" + code_23 + ";" + str(control_plant.decimal_hours_code_23) + "\n" + \
           date + ";" + worker_name + ";" + code_24 + ";" + str(control_plant.decimal_hours_code_24) + "\n" + \
           date + ";" + worker_name + ";" + code_6 + ";" + str(control_plant.decimal_hours_code_6) + "\n" + \
           date + ";" + worker_name + ";" + code_29 + ";" + str(control_plant.decimal_hours_code_29) + "\n"

# Esta función registra los datos introducidos por el usuario.
def register_input(date, worker_name):

	register_file = open(REGISTRY_FILE_NAME, "a")
	register_file.write(generate_input_to_register(date, worker_name))
	register_file.close()

# Esta función llama a todas las funciones "clear()" de cada uno de los archivos para que reseteen la pantalla.
def clear():
    workername.clear()
    calendar.clear()
    timetable.clear()
    control_plant.clear()


AMOUNT_OF_ROWS = 14

root = tk.Tk()
root.title("CONTROL EN PLANTA LACADO II")
root.state("zoomed")
#root.geometry()

control_plant = InputControlPlant(root, AMOUNT_OF_ROWS)
control_plant.pack(fill="both")
control_plant.place(relx=0.33, rely=0, relwidth=0.67, relheigh=0.95)

calendar = Calendar(root)
calendar.pack(fill="both")
calendar.place(relx=0.01, rely=0.15, relwidth=0.31, relheigh=0.25)

timetable = Timetable(root)
timetable.pack(fill="both")
timetable.place(relx=0.01, rely=0.45, relwidth=0.31, relheigh=0.4)

workername = WorkerName(root)
workername.pack(fill="both")
workername.place(relx=0.01, rely=0, relwidth=0.3, relheigh=0.12)

total = Button(root, text="Registrar", command=register)
total.place(relx=0.1, rely=0.9, relwidth=0.1, relheigh=0.1)

root.mainloop()
