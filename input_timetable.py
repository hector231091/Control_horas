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

        self.total_day_hours = StringVar()
        self.first_sum = StringVar()
        self.second_sum = StringVar()
        self.third_sum = StringVar()

        self.__load_hours()
        self.__init_headers_labels()
        self.__init_empty_combobox()
        self.__sum_independent_hours()
        self.__total_hour_button()
        self.__total_hours_label()

    def __load_hours(self):
    	with open(HOURS_FILE_NAME, "r") as hour:
    		lines = reader(hour)
    		"""header = next(lines)"""

    		hour_list = []

    		for line in hour:
		        hour_list.append(line[:5])

    	return hour_list

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

    def __init_empty_combobox(self):

    	self.from_hour_1 = ttk.Combobox(self,
    									justify="center",
    									values=self.__load_hours(),
    									width=10)
    	self.from_hour_1.grid(row=1,
							  column=0,
							  padx=(0, CELL_PADDING),
							  pady=CELL_PADDING,
							  ipadx=CELL_MARGIN,
							  ipady=CELL_MARGIN,
							  sticky=W + E + N + S)

    	self.from_hour_2 = ttk.Combobox(self,
    									justify="center",
    									values=self.__load_hours(),
    									width=10)
    	self.from_hour_2.grid(row=2,
							  column=0,
							  padx=(0, CELL_PADDING),
							  pady=CELL_PADDING,
							  ipadx=CELL_MARGIN,
							  ipady=CELL_MARGIN,
							  sticky=W + E + N + S)

    	self.from_hour_3 = ttk.Combobox(self,
    									justify="center",
    									values=self.__load_hours(),
    									width=10)
    	self.from_hour_3.grid(row=3,
							  column=0,
							  padx=(0, CELL_PADDING),
							  pady=CELL_PADDING,
							  ipadx=CELL_MARGIN,
							  ipady=CELL_MARGIN,
							  sticky=W + E + N + S)

    	self.until_hour_1 = ttk.Combobox(self,
    									justify="center",
    									values=self.__load_hours(),
    									width=10)
    	self.until_hour_1.grid(row=1,
							   column=1,
							   padx=(0, CELL_PADDING),
							   pady=CELL_PADDING,
							   ipadx=CELL_MARGIN,
							   ipady=CELL_MARGIN,
							   sticky=W + E + N + S)

    	self.until_hour_2 = ttk.Combobox(self,
    									justify="center",
    									values=self.__load_hours(),
    									width=10)
    	self.until_hour_2.grid(row=2,
							   column=1,
							   padx=(0, CELL_PADDING),
							   pady=CELL_PADDING,
							   ipadx=CELL_MARGIN,
							   ipady=CELL_MARGIN,
							   sticky=W + E + N + S)

    	self.until_hour_3 = ttk.Combobox(self,
    									justify="center",
    									values=self.__load_hours(),
    									width=10)
    	self.until_hour_3.grid(row=3,
							   column=1,
							   padx=(0, CELL_PADDING),
							   pady=CELL_PADDING,
							   ipadx=CELL_MARGIN,
							   ipady=CELL_MARGIN,
							   sticky=W + E + N + S)

    def __sum_independent_hours(self):

    	self.sum_hour_1 = Label(self,
    							textvariable=self.first_sum,
    							relief="sunken")
    	self.sum_hour_1.grid(row=1,
    						column=2,
    						padx=(0, CELL_PADDING),
							pady=CELL_PADDING,
							ipadx=CELL_MARGIN,
							ipady=CELL_MARGIN,
							sticky=W + E + N + S)

    	self.sum_hour_2 = Label(self,
    							textvariable=self.second_sum,
    							relief="sunken")
    	self.sum_hour_2.grid(row=2,
    						column=2,
    						padx=(0, CELL_PADDING),
							pady=CELL_PADDING,
							ipadx=CELL_MARGIN,
							ipady=CELL_MARGIN,
							sticky=W + E + N + S)

    	self.sum_hour_3 = Label(self,
    							textvariable=self.third_sum,
    							relief="sunken")
    	self.sum_hour_3.grid(row=3,
    						column=2,
    						padx=(0, CELL_PADDING),
							pady=CELL_PADDING,
							ipadx=CELL_MARGIN,
							ipady=CELL_MARGIN,
							sticky=W + E + N + S) 

    def __total_hour_button(self):

    	self.total_hour = Button(self,
    							 text="Sumar horas",
    							 command=self.__sum_hours)

    	self.total_hour.grid(row=4,
							 column=0,
							 columnspan=4,
							 padx=(0, CELL_PADDING),
							 pady=CELL_PADDING,
							 ipadx=CELL_MARGIN,
							 ipady=CELL_MARGIN,
							 sticky=W + E + N + S)    	

    def __total_hours_label(self):

     	self.total_hour = Label(self,
    							textvariable=self.total_day_hours,
    							relief="sunken")
     	self.total_hour.grid(row=1,
							column=3,
							rowspan=3,
							padx=(0, CELL_PADDING),
							pady=CELL_PADDING,
							ipadx=CELL_MARGIN,
							ipady=CELL_MARGIN,
							sticky=W + E + N + S)

    def __sum_hours(self):

        now = "00:00"

        if self.until_hour_1.get() != "" and self.from_hour_1.get() != "":
            self.first_sum.set((datetime.strptime(self.until_hour_1.get(), "%H:%M") - datetime.strptime(self.from_hour_1.get(), "%H:%M")))
        else:
            self.until_hour_1.set(now)
            self.from_hour_1.set(now)
            self.first_sum.set((datetime.strptime(self.until_hour_1.get(), "%H:%M") - datetime.strptime(self.from_hour_1.get(), "%H:%M")))
        if self.until_hour_2.get() != "" and self.from_hour_2.get() != "":
       		self.second_sum.set((datetime.strptime(self.until_hour_2.get(), "%H:%M") - datetime.strptime(self.from_hour_2.get(), "%H:%M")))
       	else:
       	    self.until_hour_2.set(now)
       	    self.from_hour_2.set(now)
       	    self.second_sum.set((datetime.strptime(self.until_hour_2.get(), "%H:%M") - datetime.strptime(self.from_hour_2.get(), "%H:%M")))
        if self.until_hour_3.get() != "" and self.from_hour_3.get() != "":
       	    self.third_sum.set((datetime.strptime(self.until_hour_3.get(), "%H:%M") - datetime.strptime(self.from_hour_3.get(), "%H:%M")))
       	else:
       	    self.until_hour_3.set(now)
       	    self.from_hour_3.set(now)
       	    self.third_sum.set((datetime.strptime(self.until_hour_3.get(), "%H:%M") - datetime.strptime(self.from_hour_3.get(), "%H:%M")))

        self.hours_1 = self.first_sum.get().split(":")[0]
        self.minute_1 = self.first_sum.get().split(":")[1]

        self.hours_2 = self.second_sum.get().split(":")[0]
        self.minute_2 = self.second_sum.get().split(":")[1]

        self.hours_3 = self.third_sum.get().split(":")[0]
        self.minute_3 = self.third_sum.get().split(":")[1]

        self.minutes = (int(self.hours_1) + int(self.hours_2) + int(self.hours_3)) * 60 + int(self.minute_1) + int(self.minute_2) + int(self.minute_3)

        self.total_hours = self.minutes // 60
        self.total_minutes = self.minutes % 60

        self.total_day_hours.set(str(self.total_hours) + ":" + str(self.total_minutes))
