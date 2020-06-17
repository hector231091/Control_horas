from tkinter import *

# Constantes
CELL_MARGIN = 10
CELL_PADDING = 2

class Timetable(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent, highlightbackground="black", highlightcolor="black", highlightthickness=2)

		self.total_hours = StringVar()

		self.__init_header_label()
		self.__init_entries()
		self.__init_label_sum_input_hours_and_minutes()
		self.__button_sum_of_hours()

	def __init_header_label(self):

		self.total_hours_label = Label(self,
									  text="HORAS",
									  anchor="center",
									  relief="groove")
		self.total_hours_label.grid(row=0,
									column=0,
									padx=(0, CELL_PADDING),
									pady=CELL_PADDING,
									ipadx=CELL_MARGIN,
									ipady=CELL_MARGIN,
									sticky=W + E + N + S)

		self.total_minutes_label = Label(self,
										text="MINUTOS",
										anchor="center",
										relief="groove")
		self.total_minutes_label.grid(row=0,
									  column=1,
									  padx=(0, CELL_PADDING),
									  pady=CELL_PADDING,
									  ipadx=CELL_MARGIN,
									  ipady=CELL_MARGIN,
									  sticky=W + E + N + S)

		self.sum_hours = Label(self,
							   text="HORAS TOTALES",
							   anchor="center",
							   relief="groove")
		self.sum_hours.grid(row=0,
							column=2,
							padx=(0, CELL_PADDING),
							pady=CELL_PADDING,
							ipadx=CELL_MARGIN,
							ipady=CELL_MARGIN,
							sticky=W + E + N + S)

	def __init_label_sum_input_hours_and_minutes(self):

		self.result_of_sum_hours_and_minutes = Label(self,
													 textvariable=self.total_hours,
													 anchor="center",
													 relief="groove")
		self.result_of_sum_hours_and_minutes.grid(row=1,
												  column=2,
												  padx=(0, CELL_PADDING),
												  pady=CELL_PADDING,
												  ipadx=CELL_MARGIN,
												  ipady=CELL_MARGIN,
												  sticky=W + E + N + S)

	def __init_entries(self):

		self.total_hours_entry = Entry(self,
									   justify="center",
									   validate="key",
									   validatecommand=(self.register(self.__validate_input_data), "%P", "%S"))
		self.total_hours_entry.grid(row=1,
									column=0,
									padx=(0, CELL_PADDING),
									pady=CELL_PADDING,
									ipadx=CELL_MARGIN,
									ipady=CELL_MARGIN,
									sticky=W + E + N + S)

		self.total_minutes_entry = Entry(self,
									     justify="center",
										 validate="key",
										 validatecommand=(self.register(self.__validate_input_data), "%P", "%S"))
		self.total_minutes_entry.grid(row=1,
									  column=1,
									  padx=(0, CELL_PADDING),
									  pady=CELL_PADDING,
									  ipadx=CELL_MARGIN,
									  ipady=CELL_MARGIN,
									  sticky=W + E + N + S)

	def __button_sum_of_hours(self):

		self.sum = Button(self,
						  text="SUMAR HORAS",
						  anchor="center",
						  command=self.__sum_hours)
		self.sum.grid(row=2,
					  column=0,
					  columnspan=3,
					  padx=(0, CELL_PADDING),
					  pady=CELL_PADDING,
					  ipadx=CELL_MARGIN,
					  ipady=CELL_MARGIN,
					  sticky=W + E + N + S)

	def __sum_hours(self):

		if self.total_hours_entry.get() == "":
			self.hours = 0
		else:
			self.hours = self.total_hours_entry.get()

		if self.total_minutes_entry.get() == "":
			self.minutes = 0
		else:
			self.minutes = self.total_minutes_entry.get()

		self.total_hours_of_day = int(self.hours) + (int(self.minutes) / 60)

		self.total_hours.set(self.total_hours_of_day)

	def __validate_input_data(self, value_if_allowed, input_text):
		# Limitamos el campo solo a valores numéricos
		if not input_text.isdecimal():
			return False

		# Limitamos el campo a 2 caracteres
		if len(value_if_allowed) > 2:
			return False

		return True

	def return_hours(self):

		if self.total_hours_entry.get() == "":
			self.hours = 0
		else:
			self.hours = self.total_hours_entry.get()

		if self.total_minutes_entry.get() == "":
			self.minutes = 0
		else:
			self.minutes = self.total_minutes_entry.get()

		self.total_hours_of_day = int(self.hours) + (int(self.minutes) / 60)

		return self.total_hours_of_day

	def clear(self):

		self.total_hours_entry.delete(0, "end")
		self.total_minutes_entry.delete(0, "end")
		self.total_hours.set("")
