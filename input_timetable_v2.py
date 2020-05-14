import tkinter as tk
import datetime
import time

from csv import reader
from tkinter import *
from tkinter import ttk
from datetime import datetime, date, time, timedelta

# Constantes
HOURS_FILE_NAME = "Horas.csv"
CELL_MARGIN = 10
CELL_PADDING = 2

class Timetable(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="green")

        self.__init_headers_labels()
        self.__init_empty_entry()

    def __init_headers_labels(self):

        self.from_hour_header = Label(self,
    								  text="Desde",
    								  anchor="center",
    								  relief="groove")
        self.from_hour_header.grid(row=0,
                                   column=0,
                                   padx=(0, CELL_PADDING),
                                   pady=CELL_PADDING,
                                   ipadx=CELL_MARGIN,
                                   ipady=CELL_MARGIN,
                                   sticky=W + E + N + S)

        self.until_hour_header = Label(self,
                                       text="Hasta",
                                       anchor="center",
                                       relief="groove")
        self.until_hour_header.grid(row=0,
                                    column=1,
                                    padx=(0, CELL_PADDING),
                                    pady=CELL_PADDING,
                                    ipadx=CELL_MARGIN,
                                    ipady=CELL_MARGIN,
                                    sticky=W + E + N + S)

        self.total_row_hour_header = Label(self,
                                           text="Horas",
                                           anchor="center",
                                           relief="groove")
        self.total_row_hour_header.grid(row=0,
                                        column=2,
                                        padx=(0, CELL_PADDING),
                                        pady=CELL_PADDING,
                                        ipadx=CELL_MARGIN,
                                        ipady=CELL_MARGIN,
                                        sticky=W + E + N + S)

        self.total_hour_header = Label(self,
                                       text="Horas totales",
                                       anchor="center",
                                       relief="groove")
        self.total_hour_header.grid(row=0,
                                    column=3,
                                    padx=(0, CELL_PADDING),
                                    pady=CELL_PADDING,
                                    ipadx=CELL_MARGIN,
                                    ipady=CELL_MARGIN,
                                    sticky=W + E + N + S)

    def __init_empty_entry(self):

        self.from_hour_header_1 = Entry(self,
                                        justify="center",
                                        validate="key",
                                        validatecommand=(self.register(self.__validate_hour), "%P", "%S"))
        self.from_hour_header_1.grid(row=1,
                                     column=0,
                                     padx=(0, CELL_PADDING),
                                     pady=CELL_PADDING,
                                     ipadx=CELL_MARGIN,
                                     ipady=CELL_MARGIN,
                                     sticky=W + E + N + S)

        self.from_hour_header_2 = Entry(self,
                                        justify="center",
                                        validate="key",
                                        validatecommand=(self.register(self.__validate_hour), "%P", "%S"))
        self.from_hour_header_2.grid(row=1,
                                     column=1,
                                     padx=(0, CELL_PADDING),
                                     pady=CELL_PADDING,
                                     ipadx=CELL_MARGIN,
                                     ipady=CELL_MARGIN,
                                     sticky=W + E + N + S)

        self.until_hour_header_1 = Entry(self,
                                         justify="center",
                                         validate="key",
                                         validatecommand=(self.register(self.__validate_hour), "%P", "%S"))
        self.until_hour_header_1.grid(row=0,
                                      column=1,
                                      padx=(0, CELL_PADDING),
                                      pady=CELL_PADDING,
                                      ipadx=CELL_MARGIN,
                                      ipady=CELL_MARGIN,
                                      sticky=W + E + N + S)

        self.until_hour_header_2 = Entry(self,
                                         justify="center",
                                         validate="key",
                                         validatecommand=(self.register(self.__validate_hour), "%P", "%S"))
        self.until_hour_header_2.grid(row=0,
                                      column=1,
                                      padx=(0, CELL_PADDING),
                                      pady=CELL_PADDING,
                                      ipadx=CELL_MARGIN,
                                      ipady=CELL_MARGIN,
                                      sticky=W + E + N + S)

