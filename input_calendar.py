from tkcalendar import Calendar, DateEntry
import tkinter as tk
from tkinter import *
from tkinter import ttk
import datetime
from datetime import datetime, date, time, timedelta

CELL_MARGIN = 7
CELL_PADDING = 3


class Calendar(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="red")

        self.day_name = StringVar()

        self.__calendar()

    def __calendar(self):
        self.calendar_title_label = Label(self,
                                          text="Fecha",
                                          anchor="center",
                                          relief="groove")

        self.calendar_title_label.grid(row=0,
                                       column=0,
                                       padx=(0, CELL_PADDING),
                                       pady=CELL_PADDING,
                                       ipadx=CELL_MARGIN,
                                       ipady=CELL_MARGIN,
                                       sticky=W + E + N + S)
        # ¿Cómo mierda hago para que la fecha sea´"día/mes/año" y no como la tienen los ingleses?
        self.calendar_entry = DateEntry(self,
                                        width=5,
                                        justify="center",
                                        background='darkblue',
                                        foreground='white',
                                        borderwidth=0,
                                        day=datetime.now().day - 1,
                                        month=datetime.now().month,
                                        year=datetime.now().year,
                                        locale="es_ES",
                                        date_pattern="dd/mm/yyyy")
        self.calendar_entry.grid(row=1,
                                 column=0,
                                 padx=(0, CELL_PADDING),
                                 pady=CELL_PADDING,
                                 ipadx=CELL_MARGIN,
                                 ipady=CELL_MARGIN,
                                 sticky=W + E + N + S)

        self.calendar_title_label = Label(self,
                                          text="Día",
                                          anchor="center",
                                          relief="groove")

        self.calendar_title_label.grid(row=0,
                                       column=1,
                                       padx=(0, CELL_PADDING),
                                       pady=CELL_PADDING,
                                       ipadx=CELL_MARGIN,
                                       ipady=CELL_MARGIN,
                                       sticky=W + E + N + S)

        self.calendar_entry = Label(self,
                                    anchor="center",
                                    textvariable=self.day_name)
        self.calendar_entry.grid(row=1,
                                 column=1,
                                 padx=(0, CELL_PADDING),
                                 pady=CELL_PADDING,
                                 ipadx=CELL_MARGIN,
                                 ipady=CELL_MARGIN,
                                 sticky=W + E + N + S)

        self.name_day_button = Button(self,
                                      text="Registrar",
                                      relief="groove",
                                      anchor="center",
                                      command=self.__print_name_day)
        self.name_day_button.grid(row=2,
                                  column=0,
                                  columnspan=2,
                                  padx=(0, CELL_PADDING),
                                  pady=CELL_PADDING,
                                  ipadx=CELL_MARGIN,
                                  ipady=CELL_MARGIN,
                                  sticky=W + E + N + S)

    def __print_name_day(self):
        self.day_name.set(self.calendar_entry.get_date())
