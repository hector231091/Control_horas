from tkinter import *

from input_control_plant import InputControlPlant

CELL_MARGIN = 7
CELL_PADDING = 3

class TotalHours(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent, background="grey")

		self.sum_total_hours = StringVar()
		self.sum_total_minutes = StringVar()

		self.__total_result_label()

	def __total_result_label(self):

		total_time_label = Button(self,
								  text="TIEMPO TOTAL",
								  command=self.__total_time_control_plant,
								  state=NORMAL)
		total_time_label.grid(row=0,
							  column=0,
							  padx=(0, CELL_PADDING),
							  pady=CELL_PADDING,
							  ipadx=CELL_MARGIN,
							  ipady=CELL_MARGIN,
							  sticky=W + E + N + S,
							  columnspan=2)

		total_hour_label = Label(self,
								 text="HORAS",
								 anchor="w",
								 relief="groove")
		total_hour_label.grid(row=1,
							  column=0,
							  padx=(0, CELL_PADDING),
							  pady=CELL_PADDING,
							  ipadx=CELL_MARGIN,
							  ipady=CELL_MARGIN,
							  sticky=W + E + N + S)

		total_minute_label = Label(self,
								   text="MINUTOS",
								   anchor="w",
								   relief="groove")
		total_minute_label.grid(row=1,
								column=1,
								padx=(0, CELL_PADDING),
								pady=CELL_PADDING,
								ipadx=CELL_MARGIN,
							 	ipady=CELL_MARGIN,
								sticky=W + E + N + S)

		total_hour_result = Label(self,
								  textvariable=self.sum_total_hours,
								  anchor="w",
								  relief="groove")
		total_hour_result.grid(row=2,
							   column=0,
							   padx=(0, CELL_PADDING),
							   pady=CELL_PADDING,
							   ipadx=CELL_MARGIN,
							   ipady=CELL_MARGIN,
							   sticky=W + E + N + S)

		total_minute_result = Label(self,
									textvariable=self.sum_total_minutes,
									anchor="w",
									relief="groove")
		total_minute_result.grid(row=2,
								 column=1,
								 padx=(0, CELL_PADDING),
								 pady=CELL_PADDING,
								 ipadx=CELL_MARGIN,
							 	 ipady=CELL_MARGIN,
								 sticky=W + E + N + S)

	def __total_time_control_plant(self):

		#self.total_horus, self.total_minutes = InputControlPlant.return_hour_and_minutes()

		self.total_horus = InputControlPlant.return_hour_and_minutes(self)

		self.global_minutes = (self.total_horus + self.total_minutes*60) / 5

		self.hours, self.minutes = input_data_to_real_time(self.global_minutes)

		self.sum_total_hours.set(self.hours)
		self.sum_total_minutes.set(self.minutes)

	def __input_data_to_real_time(input_data):
		# Lo pasamos todo a minutos.
		self.input_data_minutes = self.input_data*5
		# Cogemos las horas.
		self.hours = int(self.input_data_minutes//60)
		# Cogemos los minutos.
		self.minutes = int(self.input_data_minutes%60)

		return self.hours, self.minutes
 