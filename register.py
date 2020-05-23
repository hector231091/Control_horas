import tkinter as tk
from csv import reader
from tkinter import *

import validator
from tester_leds import TesterLeds
from data import ValidationType

WORKERS_FILE_NAME = "Operarios.csv"

CELL_MARGIN = 7
CELL_PADDING = 3

class RegisterData(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent, background="yellow")

		# Para hacer por fuera la parte del registro