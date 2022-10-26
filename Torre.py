from asyncio.windows_events import NULL
from Disco import Disco
red = "\033[1;31;40m"
cyan = "\033[1;36;40m"
green = "\033[1;32;40m"


class Torre:
    def __init__(self):
        self._id = 0
        self._pilha_de_discos = []

    def empilhar(self, disco):
        return self._pilha_de_discos.append(disco)

    def desempilhar(self):
        if self.get_tamanho() > 0:
            return self._pilha_de_discos.pop()

    def get_ultimo_disco(self):
        if not self._pilha_de_discos:
            return -1
        try:
            return self._pilha_de_discos[self.get_tamanho() - 1].get_id()
        except AttributeError:
            print("\nTorre vazia!\n")

    def set_id(self, id):
        self._id = id

    def get_id(self):
        return self._id

    def to_string(self):
        if self.get_id() == 1:
            print(red + "Torre: " + str(self._id))
        elif self.get_id() == 2:
            print(cyan + "Torre: " + str(self._id))
        else:
            print(green + "Torre: " + str(self._id))

        try:
            for disco in reversed(self._pilha_de_discos):
                print(str(disco.get_id()))
        except AttributeError:
            return None

    def get_pilha_de_discos(self):
        return self._pilha_de_discos

    def get_tamanho(self):
        return len(self._pilha_de_discos)
