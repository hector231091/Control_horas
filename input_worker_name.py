
from csv import reader
from tkinter import *

WORKERS_FILE_NAME = "Operarios.csv"

CELL_MARGIN = 7
CELL_PADDING = 3

class WorkerName(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent, highlightbackground="black", highlightcolor="black", highlightthickness=2)

		self.worker_name = StringVar()

		self.__init_labels()
		self.__load_list_of_workers()

	def __init_labels(self):
		self.worker_code_label = Label(self,
									   text="Nº de operario",
									   anchor="center",
									   relief="groove")
		self.worker_code_label.grid(row=0,
									column=0,
									padx=(0, CELL_PADDING),
									pady=CELL_PADDING,
									ipadx=CELL_MARGIN,
									ipady=CELL_MARGIN,
									sticky=W + E + N + S)

		self.worker_code_entry = Entry(self,
									   justify="center",
									   validate="key",
									   validatecommand=(self.register(self.__validate_worker_name), "%P", "%S"))
		self.worker_code_entry.grid(row=1,
									column=0,
									padx=(0, CELL_PADDING),
									pady=CELL_PADDING,
									ipadx=CELL_MARGIN,
									ipady=CELL_MARGIN,
									sticky=W + E + N + S)

		self.worker_name_title_label = Label(self,
									   text="Nombre de operario",
									   anchor="center",
									   relief="groove")
		self.worker_name_title_label.grid(row=0,
									column=1,
									padx=(0, CELL_PADDING),
									pady=CELL_PADDING,
									ipadx=CELL_MARGIN,
									ipady=CELL_MARGIN,
									sticky=W + E + N + S)

		self.worker_name_label = Label(self,
									   anchor="center",
									   relief="groove",
									   textvariable=self.worker_name,
									   background="#F8B527")
		self.worker_name_label.grid(row=1,
									column=1,
									padx=(0, CELL_PADDING),
									pady=CELL_PADDING,
									ipadx=CELL_MARGIN,
									ipady=CELL_MARGIN,
									sticky=W + E + N + S)

	def __load_list_of_workers(self):
		with open(WORKERS_FILE_NAME, "r") as worker:
			lines = reader(worker)
			header = next(lines)

			worker_code_list = []
			worker_name_list = []


			for line in worker:
				# Realmente lo suyo sería que leyera hasta el primer ";", ya que el código del operario puede ser de 1, 2 ó 3 dígitos. Arreglar en un futuro.
				worker_code_list.append(line[:3])
				worker_name_list.append(line[4:-1])

		worker_code_and_name = dict(zip(worker_code_list, worker_name_list))

		return worker_code_and_name

	def __validate_worker_name(self, value_if_allowed, input_text):

		# Limitamos el campo solo a valores numéricos
		if not input_text.isdecimal():
			return False

		# Limitamos el campo a 3 caracteres
		if len(value_if_allowed) > 3:
			return False

		# Lo ideal no es que el campo se ponga de un color, si no que los leds se enciendan o apaguen.
		if value_if_allowed in self.__load_list_of_workers():
			self.worker_name.set(self.__load_list_of_workers().get(value_if_allowed))
			self.worker_name_label.config(background="#2BFA0B")
			# Modificar para que lo haga bien
			# TesterLeds.init_leds(self).led_workers.to_green(on=True)

		else:
			self.worker_name.set("Algo falla...")
			self.worker_name_label.config(background="#FA0000")

		return True

	def get_worker_code(self):

		return self.worker_code_entry.get()

	def clear(self):
		self.worker_code_entry.delete(0, "end")
		self.worker_name.set("")
		self.worker_name_label.config(background = "#F8B527")

