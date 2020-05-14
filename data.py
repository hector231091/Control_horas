import enum

class Record:
    def __init__(self,
                 operations_label,
                 operation_code_label,
                 data_input_1_entry,
                 data_input_2_entry,
                 data_input_3_entry,
                 hour_label,
                 minute_label):
        self.operations_label = operations_label
        self.operation_code_label = operation_code_label
        self.data_input_1_entry = data_input_1_entry
        self.data_input_2_entry = data_input_2_entry
        self.data_input_3_entry = data_input_3_entry
        self.hour_label = hour_label
        self.minute_label = minute_label


class Hour:
    def __init__(self,
                 hour_code_3,
                 hour_code_8,
                 hour_code_9,
                 hour_code_15,
                 hour_code_18,
                 hour_code_19,
                 hour_code_20,
                 hour_code_21,
                 hour_code_22,
                 hour_code_23,
                 hour_code_24,
                 hour_code_6,
                 hour_code_29):
        self.hour_code_3 = hour_code_3
        self.hour_code_8 = hour_code_2
        self.hour_code_9 = hour_code_9
        self.hour_code_15 = hour_code_15
        self.hour_code_18 = hour_code_18
        self.hour_code_19 = hour_code_19
        self.hour_code_20 = hour_code_20
        self.hour_code_21 = hour_code_21
        self.hour_code_22 = hour_code_22
        self.hour_code_23 = hour_code_23
        self.hour_code_24 = hour_code_24
        self.hour_code_6 = hour_code_6
        self.hour_code_29 = hour_code_29

class Validation:
    def __init__(self, v_type, message=""):
        self.type = v_type
        self.message = messageç

class ValidationType(enum.Enum):
    VALID = 1
    INVALID = 2
    EMPTY = 3
