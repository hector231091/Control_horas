from tkinter import *

CELL_MARGIN = 7
CELL_PADDING = 3

class InputControlPlant(Frame):
	def __init__(self, parent, rows_to_show):
		Frame.__init__(self, parent, background="cyan")

		self.total_sum_hours = StringVar()
		self.total_sum_minutes = StringVar()

		self.rows_to_show = rows_to_show

		self.__init_horizontal_header()
		self.__init_vertical_name_header()
		self.__init_vertical_code_header()
		self.__create_sum_button()
		self.__create_empty_total_hours_and_minutes_label()

		self.__entries = []
		self.__init_empty_skeleton(self.__entries)

	def __init_vertical_name_header(self):
		prepare_raw_material_label = Label(self, text="PREPARAR MATERIA PRIMA", anchor="w", relief="groove")
		prepare_raw_material_label.grid(row=1,
										column=0,
										padx=(0, CELL_PADDING),
										pady=CELL_PADDING,
										ipadx=CELL_MARGIN,
										ipady=CELL_MARGIN,
										sticky=W + E + N + S)

		rest_label = Label(self, text="DESCANSO", anchor="w", relief="groove")
		rest_label.grid(row=2,
						column=0,
						padx=(0, CELL_PADDING),
						pady=CELL_PADDING,
						ipadx=CELL_MARGIN,
						ipady=CELL_MARGIN,
						sticky=W + E + N + S)

		company_meeting_label = Label(self, text="REUNIÓN DE EMPRESA", anchor="w", relief="groove")
		company_meeting_label.grid(row=3,
								   column=0,
								   padx=(0, CELL_PADDING),
								   pady=CELL_PADDING,
								   ipadx=CELL_MARGIN,
							 	   ipady=CELL_MARGIN,
								   sticky=W + E + N + S)

		cleaning_label = Label(self, text="LIMPIEZA", anchor="w", relief="groove")
		cleaning_label.grid(row=4,
							column=0,
							padx=(0, CELL_PADDING),
							pady=CELL_PADDING,
							ipadx=CELL_MARGIN,
							ipady=CELL_MARGIN,
							sticky=W + E + N + S)

		lacar_profiles_label = Label(self, text="LACAR PERFILES", anchor="w", relief="groove")
		lacar_profiles_label.grid(row=5,
								  column=0,
								  padx=(0, CELL_PADDING),
								  pady=CELL_PADDING,
								  ipadx=CELL_MARGIN,
								  ipady=CELL_MARGIN,
								  sticky=W + E + N + S)

		profile_washing_label = Label(self, text="LAVADO DE PERFILES", anchor="w", relief="groove")
		profile_washing_label.grid(row=6,
								   column=0,
								   padx=(0, CELL_PADDING),
								   pady=CELL_PADDING,
								   ipadx=CELL_MARGIN,
								   ipady=CELL_MARGIN,
								   sticky=W + E + N + S)

		shrink_profiles_label = Label(self, text="RETRACTILAR PERFILES", anchor="w", relief="groove")
		shrink_profiles_label.grid(row=7,
								   column=0,
								   padx=(0, CELL_PADDING),
								   pady=CELL_PADDING,
								   ipadx=CELL_MARGIN,
								   ipady=CELL_MARGIN,
								   sticky=W + E + N + S)

		pack_profiles_label = Label(self, text="EMBALAR PERFILES", anchor="w", relief="groove")
		pack_profiles_label.grid(row=8,
								 column=0,
								 padx=(0, CELL_PADDING),
								 pady=CELL_PADDING,
								 ipadx=CELL_MARGIN,
								 ipady=CELL_MARGIN,
								 sticky=W + E + N + S)

		material_review_label = Label(self, text="REVISAR MATERIAL", anchor="w", relief="groove")
		material_review_label.grid(row=9,
								   column=0,
								   padx=(0, CELL_PADDING),
								   pady=CELL_PADDING,
								   ipadx=CELL_MARGIN,
								   ipady=CELL_MARGIN,
								   sticky=W + E + N + S)

		pickling_label = Label(self, text="DECAPAR", anchor="w", relief="groove")
		pickling_label.grid(row=10,
							column=0,
							padx=(0, CELL_PADDING),
							pady=CELL_PADDING,
							ipadx=CELL_MARGIN,
							ipady=CELL_MARGIN,
							sticky=W + E + N + S)

		movement_painting_label = Label(self, text="MOVIMIENTO DE PINTURA", anchor="w", relief="groove")
		movement_painting_label.grid(row=11,
									 column=0,
									 padx=(0, CELL_PADDING),
									 pady=CELL_PADDING,
									 ipadx=CELL_MARGIN,
									 ipady=CELL_MARGIN,
									 sticky=W + E + N + S)

		truck_loading_unloading_label = Label(self, text="CARGA/DESCARGA DE CAMIONES", anchor="w", relief="groove")
		truck_loading_unloading_label.grid(row=12,
										   column=0,
										   padx=(0, CELL_PADDING),
										   pady=CELL_PADDING,
										   ipadx=CELL_MARGIN,
										   ipady=CELL_MARGIN,
										   sticky=W + E + N + S)

		take_save_profiles_label = Label(self, text="SACAR/GUARDAR LOS PERFILES", anchor="w", relief="groove")
		take_save_profiles_label.grid(row=13,
									  column=0,
									  padx=(0, CELL_PADDING),
									  pady=CELL_PADDING,
									  ipadx=CELL_MARGIN,
									  ipady=CELL_MARGIN,
									  sticky=W + E + N + S)

		check_button_label = Label(self, text="ELEGIR DE UN DESPLEGABLE", anchor="w", relief="groove")
		check_button_label.grid(row=14,
								column=0,
								padx=(0, CELL_PADDING),
								pady=CELL_PADDING,
								ipadx=CELL_MARGIN,
								ipady=CELL_MARGIN,
								sticky=W + E + N + S)

	def __init_vertical_code_header(self):
		prepare_raw_material_label = Label(self, text="3", anchor="center", relief="groove")
		prepare_raw_material_label.grid(row=1,
										column=1,
										padx=(0, CELL_PADDING),
										pady=CELL_PADDING,
										ipadx=CELL_MARGIN,
										ipady=CELL_MARGIN,
										sticky=W + E + N + S)

		rest_label = Label(self, text="8", anchor="center", relief="groove")
		rest_label.grid(row=2,
						column=1,
						padx=(0, CELL_PADDING),
						pady=CELL_PADDING,
						ipadx=CELL_MARGIN,
						ipady=CELL_MARGIN,
						sticky=W + E + N + S)

		company_meeting_label = Label(self, text="9", anchor="center", relief="groove")
		company_meeting_label.grid(row=3,
								   column=1,
								   padx=(0, CELL_PADDING),
								   pady=CELL_PADDING,
								   ipadx=CELL_MARGIN,
							 	   ipady=CELL_MARGIN,
								   sticky=W + E + N + S)

		cleaning_label = Label(self, text="15", anchor="center", relief="groove")
		cleaning_label.grid(row=4,
							column=1,
							padx=(0, CELL_PADDING),
							pady=CELL_PADDING,
							ipadx=CELL_MARGIN,
							ipady=CELL_MARGIN,
							sticky=W + E + N + S)

		lacar_profiles_label = Label(self, text="18", anchor="center", relief="groove")
		lacar_profiles_label.grid(row=5,
								  column=1,
								  padx=(0, CELL_PADDING),
								  pady=CELL_PADDING,
								  ipadx=CELL_MARGIN,
								  ipady=CELL_MARGIN,
								  sticky=W + E + N + S)

		profile_washing_label = Label(self, text="19", anchor="center", relief="groove")
		profile_washing_label.grid(row=6,
								   column=1,
								   padx=(0, CELL_PADDING),
								   pady=CELL_PADDING,
								   ipadx=CELL_MARGIN,
								   ipady=CELL_MARGIN,
								   sticky=W + E + N + S)

		shrink_profiles_label = Label(self, text="20", anchor="center", relief="groove")
		shrink_profiles_label.grid(row=7,
								   column=1,
								   padx=(0, CELL_PADDING),
								   pady=CELL_PADDING,
								   ipadx=CELL_MARGIN,
								   ipady=CELL_MARGIN,
								   sticky=W + E + N + S)

		pack_profiles_label = Label(self, text="21", anchor="center", relief="groove")
		pack_profiles_label.grid(row=8,
								 column=1,
								 padx=(0, CELL_PADDING),
								 pady=CELL_PADDING,
								 ipadx=CELL_MARGIN,
								 ipady=CELL_MARGIN,
								 sticky=W + E + N + S)

		material_review_label = Label(self, text="22", anchor="center", relief="groove")
		material_review_label.grid(row=9,
								   column=1,
								   padx=(0, CELL_PADDING),
								   pady=CELL_PADDING,
								   ipadx=CELL_MARGIN,
								   ipady=CELL_MARGIN,
								   sticky=W + E + N + S)

		pickling_label = Label(self, text="23", anchor="center", relief="groove")
		pickling_label.grid(row=10,
							column=1,
							padx=(0, CELL_PADDING),
							pady=CELL_PADDING,
							ipadx=CELL_MARGIN,
							ipady=CELL_MARGIN,
							sticky=W + E + N + S)

		movement_painting_label = Label(self, text="24", anchor="center", relief="groove")
		movement_painting_label.grid(row=11,
									 column=1,
									 padx=(0, CELL_PADDING),
									 pady=CELL_PADDING,
									 ipadx=CELL_MARGIN,
									 ipady=CELL_MARGIN,
									 sticky=W + E + N + S)

		truck_loading_unloading_label = Label(self, text="6", anchor="center", relief="groove")
		truck_loading_unloading_label.grid(row=12,
										   column=1,
										   padx=(0, CELL_PADDING),
										   pady=CELL_PADDING,
										   ipadx=CELL_MARGIN,
										   ipady=CELL_MARGIN,
										   sticky=W + E + N + S)

		take_save_profiles_label = Label(self, text="29", anchor="center", relief="groove")
		take_save_profiles_label.grid(row=13,
									  column=1,
									  padx=(0, CELL_PADDING),
									  pady=CELL_PADDING,
									  ipadx=CELL_MARGIN,
									  ipady=CELL_MARGIN,
									  sticky=W + E + N + S)

		check_button_label = Label(self, text="¿?", anchor="center", relief="groove")
		check_button_label.grid(row=14,
								column=1,
								padx=(0, CELL_PADDING),
								pady=CELL_PADDING,
								ipadx=CELL_MARGIN,
								ipady=CELL_MARGIN,
								sticky=W + E + N + S)
	
	def __init_horizontal_header(self):
		operation_name = Label(self, text="NOMBRE DE LA OPERACIÓN", anchor="center", relief="groove")
		operation_name.grid(row=0,
							column=0,
							padx=(0, CELL_PADDING),
							pady=CELL_PADDING,
							ipadx=CELL_MARGIN,
							ipady=CELL_MARGIN,
							sticky=W + E + N + S)

		operation_code_name = Label(self, text="CÓDIGO", anchor="center", relief="groove")
		operation_code_name.grid(row=0,
								 column=1,
								 padx=(0, CELL_PADDING),
								 pady=CELL_PADDING,
								 ipadx=CELL_MARGIN,
								 ipady=CELL_MARGIN,
								 sticky=W + E + N + S)

		date_1 = Label(self, text="DATO 1", anchor="center", relief="groove")
		date_1.grid(row=0,
					column=2,
					padx=(0, CELL_PADDING),
					pady=CELL_PADDING,
					ipadx=CELL_MARGIN,
					ipady=CELL_MARGIN,
					sticky=W + E + N + S)

		date_2 = Label(self, text="DATO 2", anchor="center", relief="groove")
		date_2.grid(row=0,
					column=3,
					padx=(0, CELL_PADDING),
					pady=CELL_PADDING,
					ipadx=CELL_MARGIN,
					ipady=CELL_MARGIN,
					sticky=W + E + N + S)

		date_3 = Label(self, text="DATO 3", anchor="center", relief="groove")
		date_3.grid(row=0,
					column=4,
					padx=(0, CELL_PADDING),
					pady=CELL_PADDING,
					ipadx=CELL_MARGIN,
					ipady=CELL_MARGIN,
					sticky=W + E + N + S)

		hours = Label(self, text="HORAS", anchor="center", relief="groove")
		hours.grid(row=0,
				   column=5,
				   padx=(0, CELL_PADDING),
				   pady=CELL_PADDING,
				   ipadx=CELL_MARGIN,
				   ipady=CELL_MARGIN,
				   sticky=W + E + N + S)

		minutes = Label(self, text="MINUTOS", anchor="center", relief="groove")
		minutes.grid(row=0,
					 column=6,
					 padx=(0, CELL_PADDING),
					 pady=CELL_PADDING,
					 ipadx=CELL_MARGIN,
					 ipady=CELL_MARGIN,
					 sticky=W + E + N + S)

	def __init_empty_skeleton(self, entries):
		for i in range(self.rows_to_show):
			row = []
			entries.append(row)
			self.__create_empty_record(i, row)

	def __create_empty_record(self, index, row):
		global_index = index + 1
		column0 = self.__create_empty_record_entry()
		column0.grid(row=global_index,
		             column=2,
		             padx=CELL_PADDING,
		             pady=CELL_PADDING,
		             ipadx=CELL_MARGIN,
		             ipady=CELL_MARGIN,
		             sticky=W + E + N + S)
		row.append(column0)

		column1 = self.__create_empty_record_entry()
		column1.grid(row=global_index,
		             column=3,
		             padx=CELL_PADDING,
		             pady=CELL_PADDING,
		             ipadx=CELL_MARGIN,
		             ipady=CELL_MARGIN,
		             sticky=W + E + N + S)
		row.append(column1)

		column2 = self.__create_empty_record_entry()
		column2.grid(row=global_index,
		             column=4,
		             padx=CELL_PADDING,
		             pady=CELL_PADDING,
		             ipadx=CELL_MARGIN,
		             ipady=CELL_MARGIN,
		             sticky=W + E + N + S)
		row.append(column2)

		column3 = self.__create_empty_record_label()
		column3.grid(row=global_index,
		             column=5,
		             padx=CELL_PADDING,
		             pady=CELL_PADDING,
		             ipadx=CELL_MARGIN,
		             ipady=CELL_MARGIN,
		             sticky=W + E + N + S)
		row.append(column3)

		column4 = self.__create_empty_record_label()
		column4.grid(row=global_index,
		             column=6,
		             padx=CELL_PADDING,
		             pady=CELL_PADDING,
		             ipadx=CELL_MARGIN,
		             ipady=CELL_MARGIN,
		             sticky=W + E + N + S)
		row.append(column4)

	def __create_sum_button(self):
		sum_button = Button(self, text="SUMAR", anchor="center", relief="groove", command=self.sum_codes)
		sum_button.grid(row=self.rows_to_show+1,
						column=0,
						padx=(0, CELL_PADDING),
						pady=CELL_PADDING,
						ipadx=CELL_MARGIN,
						ipady=CELL_MARGIN,
						columnspan=5,
						sticky=W + E + N + S)

	def __create_empty_record_entry(self):
		return Entry(self,
					 background="white",
					 relief="groove",
					 justify="center",
					 validate="key",
					 validatecommand=(self.register(self.__validate_input_data), "%P", "%S"))

	def __create_empty_record_label(self):
		return Label(self,
					 background="white",
					 relief="groove",
					 justify="center")

	def sum_codes(self):

		for i in range (self.rows_to_show):

			row = i

			if self.__entries[row][0].get() == "":
				self.date_1 = 0
			else:
				self.date_1 = int(self.__entries[row][0].get())

			if self.__entries[row][1].get() == "":
				self.date_2 = 0
			else:
				self.date_2 = int(self.__entries[row][1].get())

			if self.__entries[row][2].get() == "":
				self.date_3 = 0
			else:
				self.date_3 = int(self.__entries[row][2].get())

			self.hours = ((self.date_1 + self.date_2 + self.date_3) * 5) // 60
			self.minutes = ((self.date_1 + self.date_2 + self.date_3) * 5) % 60

			self.__entries[row][3].configure(text=self.hours)
			self.__entries[row][4].configure(text=self.minutes)

		self.hours, self.minutes = self.__return_hour_and_minutes()

		total_minutes = (self.hours * 60) + self.minutes

		self.total_sum_hours.set(total_minutes // 60)
		self.total_sum_minutes.set(total_minutes % 60)

	def __create_empty_total_hours_and_minutes_label(self):

		self.result_sum_hours_label = Label(self,
											textvariable=self.total_sum_hours,
											anchor="center",
											relief="groove")
		self.result_sum_hours_label.grid(row=self.rows_to_show+1,
										 column=5,
										 padx=(0, CELL_PADDING),
										 pady=CELL_PADDING,
										 ipadx=CELL_MARGIN,
										 ipady=CELL_MARGIN,
										 sticky=W + E + N + S)

		self.result_sum_minutes_label = Label(self,
											  textvariable=self.total_sum_minutes,
											  anchor="center",
											  relief="groove")
		self.result_sum_minutes_label.grid(row=self.rows_to_show+1,
										   column=6,
										   padx=(0, CELL_PADDING),
										   pady=CELL_PADDING,
										   ipadx=CELL_MARGIN,
										   ipady=CELL_MARGIN,
										   sticky=W + E + N + S)

	def __return_hour_and_minutes(self):

		self.hour_code_3 = self.__validate_if_entry_is_empty(self.__entries[0][3].cget("text"))
		self.minute_code_3 = self.__validate_if_entry_is_empty(self.__entries[0][4].cget("text"))

		self.hour_code_8 = self.__validate_if_entry_is_empty(self.__entries[1][3].cget("text"))
		self.minute_code_8 = self.__validate_if_entry_is_empty(self.__entries[1][4].cget("text"))

		self.hour_code_9 = self.__validate_if_entry_is_empty(self.__entries[2][3].cget("text"))
		self.minute_code_9 = self.__validate_if_entry_is_empty(self.__entries[2][4].cget("text"))

		self.hour_code_15 = self.__validate_if_entry_is_empty(self.__entries[3][3].cget("text"))
		self.minute_code_15 = self.__validate_if_entry_is_empty(self.__entries[3][4].cget("text"))

		self.hour_code_18 = self.__validate_if_entry_is_empty(self.__entries[4][3].cget("text"))
		self.minute_code_18 = self.__validate_if_entry_is_empty(self.__entries[4][4].cget("text"))

		self.hour_code_19 = self.__validate_if_entry_is_empty(self.__entries[5][3].cget("text"))
		self.minute_code_19 = self.__validate_if_entry_is_empty(self.__entries[5][4].cget("text"))

		self.hour_code_20 = self.__validate_if_entry_is_empty(self.__entries[6][3].cget("text"))
		self.minute_code_20= self.__validate_if_entry_is_empty(self.__entries[6][4].cget("text"))

		self.hour_code_21 = self.__validate_if_entry_is_empty(self.__entries[7][3].cget("text"))
		self.minute_code_21 = self.__validate_if_entry_is_empty(self.__entries[7][4].cget("text"))

		self.hour_code_22 = self.__validate_if_entry_is_empty(self.__entries[8][3].cget("text"))
		self.minute_code_22 = self.__validate_if_entry_is_empty(self.__entries[8][4].cget("text"))

		self.hour_code_23 = self.__validate_if_entry_is_empty(self.__entries[9][3].cget("text"))
		self.minute_code_23 = self.__validate_if_entry_is_empty(self.__entries[9][4].cget("text"))

		self.hour_code_24 = self.__validate_if_entry_is_empty(self.__entries[10][3].cget("text"))
		self.minute_code_24 = self.__validate_if_entry_is_empty(self.__entries[10][4].cget("text"))

		self.hour_code_6 = self.__validate_if_entry_is_empty(self.__entries[11][3].cget("text"))
		self.minute_code_6 = self.__validate_if_entry_is_empty(self.__entries[11][4].cget("text"))

		self.hour_code_29 = self.__validate_if_entry_is_empty(self.__entries[12][3].cget("text"))
		self.minute_code_29 = self.__validate_if_entry_is_empty(self.__entries[12][4].cget("text"))

		self.total_hour = self.hour_code_3 +\
						  self.hour_code_8 +\
						  self.hour_code_9 +\
						  self.hour_code_15 +\
						  self.hour_code_18 +\
						  self.hour_code_19 +\
						  self.hour_code_20 +\
						  self.hour_code_21 +\
						  self.hour_code_22 +\
						  self.hour_code_23 +\
						  self.hour_code_24 +\
						  self.hour_code_6 +\
						  self.hour_code_29

		self.total_minutes = self.minute_code_3 +\
							 self.minute_code_8 +\
							 self.minute_code_9 +\
							 self.minute_code_15 +\
							 self.minute_code_18 +\
							 self.minute_code_19 +\
							 self.minute_code_20 +\
							 self.minute_code_21 +\
							 self.minute_code_22 +\
							 self.minute_code_23 +\
							 self.minute_code_24 +\
							 self.minute_code_6 +\
							 self.minute_code_29

		return self.total_hour, self.total_minutes

	def __validate_input_data(self, value_if_allowed, input_text):
		# Limitamos el campo solo a valores numéricos
		if not input_text.isdecimal():
			return False

		# Limitamos el campo a 2 caracteres
		if len(value_if_allowed) > 2:
			return False

		return True

	def hours_and_minutes_to_decimal(self):

		self.hours, self.minutes = self.__return_hour_and_minutes()

		self.decimal_hours = int(self.hours) + float(self.minutes/60)

		return self.decimal_hours

	def __validate_if_entry_is_empty(self, entry):

		if entry == "":
			final_date = 0
		else:
			final_date = int(entry)

		return final_date
