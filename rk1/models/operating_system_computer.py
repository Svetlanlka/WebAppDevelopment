class OperatingSystemComputer:
    """
    Операционные системы компютеров
    для реализации связи многие-ко-многим
    """

    def __init__(self, computer_id, operation_system_id):
        self.operation_system_id = operation_system_id
        self.computer_id = computer_id