import locale

from tkcalendar import DateEntry
from tkinter import *
import datetime
from datetime import datetime

CELL_MARGIN = 7
CELL_PADDING = 3


class Calendar(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="red")

        self.day_number = StringVar()

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
        self.calendar_date_entry = DateEntry(self,
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
        self.calendar_date_entry.grid(row=1,
                                 column=0,
                                 padx=(0, CELL_PADDING),
                                 pady=CELL_PADDING,
                                 ipadx=CELL_MARGIN,
                                 ipady=CELL_MARGIN,
                                 sticky=W + E + N + S)
        self.calendar_date_entry.bind("<<DateEntrySelected>>", self.__print_name_day)

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
                                    textvariable=self.day_number)
        self.calendar_entry.grid(row=1,
                                 column=1,
                                 padx=(0, CELL_PADDING),
                                 pady=CELL_PADDING,
                                 ipadx=CELL_MARGIN,
                                 ipady=CELL_MARGIN,
                                 sticky=W + E + N + S)

    def __print_name_day(self, event):
        w = event.widget
        date = w.get_date()
        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
        date_with_format = date.strftime("%A, %-d de %B de %Y")
        self.day_number.set(date_with_format)

    def return_date(self):
        return str(self.calendar_date_entry.get_date())
