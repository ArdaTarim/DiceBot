class InputError(Exception):
    def __init__(self, message="An input error occurred."):
        self.message = message
        super().__init__(self.message)