class HttpBadRequestError(Exception):
    def __init__(self, message:str):
        # Não é necessário, mas é uma boa prática chamar o construtor da superclasse.
        # É necessário para utilizar os métodos da superclasse.
        super().__init__(message)
        self.status_code = 400
        self.name = "BadRequest"
        self.message = message
