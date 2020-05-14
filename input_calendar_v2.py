from tkcalendar import Calendar, DateEntry
import tkinter as tk
from tkinter import *
from tkinter import ttk
import datetime
from datetime import datetime, date, time, timedelta
from babel.dates import format_date, format_datetime, format_time

import datetime

CELL_MARGIN = 7
CELL_PADDING = 3

class Calendar(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="red")

        self.name_day =StringVar()

        # self.__list_day()
        # self.__list_month()
        # self.__list_year()

        self.__header_label()
        self.__day_month_year_entry()
        self.__name_day_label()
        self.__button_register_date()

    def __header_label(self):

      self.header_day_label = Label(self,
                                    text="Día",
                                    anchor="center",
                                    relief="groove",
                                    background="#F8B527")
      self.header_day_label.grid(row=0,
                                 column=0,
                                 padx=(0, CELL_PADDING),
                                 pady=CELL_PADDING,
                                 ipadx=CELL_MARGIN,
                                 ipady=CELL_MARGIN,
                                 sticky=W + E + N + S)

      self.header_month_label = Label(self,
                                      text="Mes",
                                      anchor="center",
                                      relief="groove",
                                      background="#F8B527")
      self.header_month_label.grid(row=0,
                                   column=1,
                                   padx=(0, CELL_PADDING),
                                   pady=CELL_PADDING,
                                   ipadx=CELL_MARGIN,
                                   ipady=CELL_MARGIN,
                                   sticky=W + E + N + S)

      self.header_year_label = Label(self,
                                     text="Año",
                                     anchor="center",
                                     relief="groove",
                                     background="#F8B527")
      self.header_year_label.grid(row=0,
                                  column=2,
                                  padx=(0, CELL_PADDING),
                                  pady=CELL_PADDING,
                                  ipadx=CELL_MARGIN,
                                  ipady=CELL_MARGIN,
                                  sticky=W + E + N + S)

    def __day_month_year_entry(self):

      self.day_entry = Entry(self,
                             justify="center",
                             validate="key",
                             validatecommand=(self.register(self.__validate_number_day), "%P", "%S"))
      self.day_entry.grid(row=1,
                          column=0,
                          padx=(0, CELL_PADDING),
                          pady=CELL_PADDING,
                          ipadx=CELL_MARGIN,
                          ipady=CELL_MARGIN,
                          sticky=W + E + N + S)

      self.month_entry = Entry(self,
                               justify="center",
                               validate="key",
                              validatecommand=(self.register(self.__validate_number_month), "%P", "%S"))
      self.month_entry.grid(row=1,
                            column=1,
                            padx=(0, CELL_PADDING),
                            pady=CELL_PADDING,
                            ipadx=CELL_MARGIN,
                            ipady=CELL_MARGIN,
                            sticky=W + E + N + S)

      self.year_entry = Entry(self,
                              justify="center",
                              validate="key",
                              validatecommand=(self.register(self.__validate_number_year), "%P", "%S"))
      self.year_entry.grid(row=1,
                           column=2,
                           padx=(0, CELL_PADDING),
                           pady=CELL_PADDING,
                           ipadx=CELL_MARGIN,
                           ipady=CELL_MARGIN,
                           sticky=W + E + N + S)

    def __name_day_label(self):

        self.name_day_label = Label(self,
                                    anchor="center",
                                    textvariable=self.name_day,
                                    relief="groove")                                   
        self.name_day_label.grid(row=3,
                                 column=0,
                                 columnspan=3,
                                 padx=(0, CELL_PADDING),
                                 pady=CELL_PADDING,
                                 ipadx=CELL_MARGIN,
                                 ipady=CELL_MARGIN,
                                 sticky=W + E + N + S)

    def __button_register_date(self):

      self.register_date_button = Button(self,
                                         text="Registrar fecha",
                                         anchor="center",
                                         command=self.__validate_name_day)
      self.register_date_button.grid(row=2,
                                    column=0,
                                    columnspan=3,
                                    padx=(0, CELL_PADDING),
                                    pady=CELL_PADDING,
                                    ipadx=CELL_MARGIN,
                                    ipady=CELL_MARGIN,
                                    sticky=W + E + N + S)

    def __validate_number_day(self, value_if_allowed, input_text):

      # Limitamos el campo solo a valores numéricos
      if not input_text.isdecimal():
        return False

      # Limitamos el campo a 2 caracteres
      if len(value_if_allowed) > 2:
        return False

      if value_if_allowed in self.__list_day():
        self.header_day_label.config(background="#2BFA0B")
      else:
        self.header_day_label.config(background="#FA0000")

      return True

    def __validate_number_month(self, value_if_allowed, input_text):

      # Limitamos el campo solo a valores numéricos
      if not input_text.isdecimal():
        return False

      # Limitamos el campo a 2 caracteres
      if len(value_if_allowed) > 2:
        return False

      if value_if_allowed in self.__list_month():
        self.header_month_label.config(background="#2BFA0B")
      else:
        self.header_month_label.config(background="#FA0000")

      return True

    def __validate_number_year(self, value_if_allowed, input_text):

      # Limitamos el campo solo a valores numéricos
      if not input_text.isdecimal():
        return False

      # Limitamos el campo a 4 caracteres
      if len(value_if_allowed) > 4:
        return False

      if value_if_allowed in self.__list_year():
        self.header_year_label.config(background="#2BFA0B")
      else:
        self.header_year_label.config(background="#FA0000")

      return True

    def __list_day(self):

      # Creamos una lista con los números que puede tener el campo, es decir, del 0 al 31.
      self.list_day = []

      for i in range(1, 32):
        self.list_day.append(str(i))

      return self.list_day

    def __list_month(self):

      # Creamos una lista con los números que puede tener el campo, es decir, del 0 al 12.
      self.list_month = []

      for i in range(1, 13):
        self.list_month.append(str(i))
      
      return self.list_month

    def __list_year(self):

      # Creamos una lista con los números que puede tener el campo, es decir, del 2000 al 3000.
      self.list_year = []

      for i in range(2020, 3000):
        self.list_year.append(str(i))

      return self.list_year

    def __validate_name_day(self):

      self.day = self.day_entry.get()
      self.month = self.month_entry.get()
      self.year = self.year_entry.get()

      isValidDate = True
      try :
          self.date = datetime.datetime(int(self.year), int(self.month), int(self.day))
          # Intentar poner el día con el siguiente formato: Lunes, 11 de Mayo de 2020.
          """
          self.d = date(int(self.year), int(self.month), int(self.day))
          self.f = format_date(d, locale='es_ES')
          print(self.f)
          self.dia = self.d.strftime("%a, %d %b %Y %H:%M:%S")
          print(self.dia)
          """
          isValidDate = True
      except ValueError :
          isValidDate = False

      if isValidDate == True:
        self.name_day_label.config(background="#2BFA0B")
        # self.name_day.set("Esta fecha SÍ existe en el calendario.")
        self.name_day.set(self.day + " / " + self.month + " / " + self.year)
      else:
        self.name_day_label.config(background="#FA0000")
        self.name_day.set("ERROR, LA FECHA NO EXISTE.")
