import datetime
import tkinter as tk
from csv import reader
from datetime import datetime
from tkinter import *
from tkinter import messagebox

import pandas as pd
import tk_tools
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
from matplotlib import style
import matplotlib.animation as animation

from input_control_plant import InputControlPlant
from input_worker_name import WorkerName
from input_timetable import Timetable
# from input_calendar import Calendar
from input_calendar_v2 import Calendar
from tester_leds import TesterLeds
# from total_hours_control_plant import TotalHours

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

# No lo he hecho así porque no sé llamar una función de otra clase. Ver con David.
"""total_hours_control_plant = TotalHours(root)
total_hours_control_plant.pack(fill="both")
total_hours_control_plant.place(relx=0.65, rely=0.15, relwidth=0.2, relheigh=0.2)"""

tester_leds = TesterLeds(root)
tester_leds.pack(fill="both")
tester_leds.place(relx=0.01, rely=0.9, relwidth=0.3, relheigh=0.1)

root.mainloop()