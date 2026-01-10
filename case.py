"""
exc_type: O tipo exceção que ocorreu, se houver.
    Se não ocorreu nenhuma exceção, este parâmetro será None

exc_val: O valor da exceção que ocorreu, se houver.
    Se não ocorreu nenhuma exceção, este parâmetro será None

exc_tb: O traceback (rastreamento de pilha) associado à exceção que ocorreu,
se houver.
    Se não ocorreu nenhuma exceção, este parâmetro será None
"""

class AlgumaCoisa:
    def __enter__(self) -> "AlgumaCoisa":
        print("Entrando no contexto")
        return self
    def __exit__(self, exc_type, exc_value, exc_tb) -> None:
        print("Saindo do contexto")

with AlgumaCoisa() as obj:
    print("Dentro do contexto")
