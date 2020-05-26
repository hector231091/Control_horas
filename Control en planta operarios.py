import tkinter as tk
from tkinter import messagebox

from input_control_plant import *

from input_control_plant import InputControlPlant
from input_worker_name import WorkerName
from input_timetable import Timetable
from input_calendar import Calendar

REGISTRY_FILE_NAME = "Registro.csv"

def validate_register_dates(hours_control_plant, hours_timetable, worker_name, input_date):
    # La función va a devolver la variable de verificación, y en función de su valor, luego se registrará en el archivo o no.
    # Debe ser "True" para que pueda registrar
    verification_variable_control_plant = True
    verification_variable_control_plant_hours_timetable = True
    verification_variable_worker_code = True
    verification_variable_hours_control_plant = True
    verification_variable_date = True

    # En principio la validación de la fecha no sé si va a ser necesaria...

    # Valicadión introduccion control en planta
    if int(hours_control_plant) == 0:
        messagebox.showerror(title="Falta meter el control en planta",
                             message="Debes introducir el control en panta para poder registrar")
        verification_variable_control_plant = False

    # Valicadión introduccion horario
    if len(str(hours_timetable)) == 0:
        messagebox.showerror(title="No has puesto el horario",
                             message="Debes introducir el horario del día de hoy para poder registrar")
        verification_variable_control_plant_hours_timetable = False

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

    # Validación de que las horas del control en planta y el horario sean iguales:
    if len(str(hours_control_plant)) != 0 and len(str(hours_timetable)) != 0:
        if hours_control_plant != hours_timetable:
            messagebox.showerror(title="Horas mal introducidas",
                                 message="Para poder registrar, las horas del control en planta y del horario deben coincidir.")
            verification_variable_hours_control_plant = False

    return verification_variable_control_plant, \
           verification_variable_control_plant_hours_timetable, \
           verification_variable_worker_code, \
           verification_variable_hours_control_plant, \
           verification_variable_date


def register():
    hours_control_plant = control_plant.hours_and_minutes_to_decimal()
    worker_name = workername.get_worker_code()
    hours_timetable = timetable.return_total_hours_to_register()

    input_date = calendar.return_date()

    # Vamos a poner las validaciones.
    verif_1, verif_2, verif_3, verif_4, verif_5 = validate_register_dates(hours_control_plant, hours_timetable, worker_name, input_date)
    if verif_1 == True and verif_2 == True and verif_3 == True and verif_4 == True and verif_5 == True:
        # Poner la función para registrar en el .csv
        print("OK")
        register_input(input_date, worker_name)
    else:
        print("NOK")

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
		   date + ";" + worker_name + ";" + code_29 + ";" + str(control_plant.decimal_hours_code_29) + "\n"


def register_input(date, worker_name):

	register_file = open(REGISTRY_FILE_NAME, "a")
	register_file.write(generate_input_to_register(date, worker_name))
	register_file.close()

AMOUNT_OF_ROWS = 14

root = tk.Tk()
root.title("CONTROL EN PLANTA LACADO II")
root.state("zoomed")

control_plant = InputControlPlant(root, AMOUNT_OF_ROWS)
control_plant.pack(fill="both")
control_plant.place(relx=0.37, rely=0, relwidth=0.62, relheigh=0.95)

calendar = Calendar(root)
calendar.pack(fill="both")
calendar.place(relx=0.01, rely=0.15, relwidth=0.31, relheigh=0.25)

timetable = Timetable(root)
timetable.pack(fill="both")
timetable.place(relx=0.01, rely=0.45, relwidth=0.27, relheigh=0.33)

workername = WorkerName(root)
workername.pack(fill="both")
workername.place(relx=0.01, rely=0, relwidth=0.2, relheigh=0.12)

total = Button(root, text="Registrar", command=register)
total.place(relx=0.9, rely=0.9, relwidth=0.1, relheigh=0.1)

root.mainloop()
