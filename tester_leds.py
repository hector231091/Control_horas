from datetime import datetime
from tkinter import *

import tk_tools

CELL_MARGIN = 7
CELL_PADDING = 3

class TesterLeds(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent, background="blue")

		self.__init_leds()
		self.change_led_workers()

	def __init_leds(self):
		
		self.worker_label = Label(self,
								  text="Trabajador",
								  anchor="center",
								  relief="groove")
		self.worker_label.grid(row=0,
							   column=0)

		self.led_workers = tk_tools.Led(self,
										size=30)
		self.led_workers.grid(row=1,
							  column=0)
#--------------------------------------------------------------------------------		
		self.plant_control = Label(self,
								   text="Control en planta",
								   anchor="center",
								   relief="groove")
		self.plant_control.grid(row=0,
							    column=1)

		self.led_plant_control = tk_tools.Led(self,
											  size=30)
		self.led_plant_control.grid(row=1,
									column=1)
#--------------------------------------------------------------------------------	
		self.timetable = Label(self,
							   text="Horario",
							   anchor="center",
							   relief="groove")
		self.timetable.grid(row=0,
							column=2)

		self.led_timetable = tk_tools.Led(self,
										  size=30)
		self.led_timetable.grid(row=1,
							    column=2)
#--------------------------------------------------------------------------------	
		self.date = Label(self,
						  text="Fecha",
						  anchor="center",
						  relief="groove")
		self.date.grid(row=0,
					   column=3)

		self.led_date = tk_tools.Led(self,
									 size=30)
		self.led_date.grid(row=1,
						   column=3)


	def change_led_workers(self):

		self.led_workers.to_grey(on=True)
		self.led_plant_control.to_grey(on=True)
		self.led_timetable.to_grey(on=True)
		self.led_date.to_grey(on=True)