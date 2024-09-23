'''
exc_type: O tipo de exceção que ocorreu, se houver.
  Se não ocorreu nenhuma exceção, este parâmetro será None.

  exc_val: O valor da exceção que ocorreu, se houver.
    Se não ocorreu nenuma exceção, este parâmetro será None.

  exc_tbm: O traceback (rastreamento de pilha) associado à exceção que ocorreu.
    Se não ocorreu nenhuma exceção, este parâmetro será None.

'''

class AlgumaCoisa:
    def __enter__(self):
        print("Estou entrando")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Estou saindo")

with AlgumaCoisa() as somenthing:
    print("estou no meio")
