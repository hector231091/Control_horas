from data import Validation, ValidationType


def validate_worker(text, worker_list):
    if len(text) == 0:
        return Validation(ValidationType.EMPTY, "El campo \"Color\" está vacío.")
    elif text in worker_list:
        return Validation(ValidationType.VALID)
    else:
        return Validation(ValidationType.INVALID, "El color que se ha introducido no existe.")
