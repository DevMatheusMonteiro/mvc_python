class HttpNotFoundError(Exception):
    def __init__(self, message:str="The requested resource was not found."):
        # Não é necessário, mas é uma boa prática chamar o construtor da superclasse.
        # É necessário para utilizar os métodos da superclasse.
        super().__init__(message)
        self.status_code = 404
        self.name = "NotFound"
        self.message = message
