from Disco import Disco
from Torre import Torre
color = '\033[93m'

class Hanoi:
    def __init__(self):
        self._lista_de_torres = []

    def iniciar_torres(self):
        for torres in range(3):
            torre = Torre()
            torre.set_id(torres + 1)
            self._lista_de_torres.append(torre)

    def iniciar_discos(self, qtd_discos):
        for discos in range(qtd_discos):
            disco = Disco()
            disco.set_id(qtd_discos - discos)
            self.get_torre(1).empilhar(disco)

    def get_torre(self, position):
        return self._lista_de_torres[position - 1]

    def trocar_disco_de_torre(self, source, target):
        try:
            if self.get_torre(source).get_tamanho() != 0 or self.get_torre(source).get_ultimo_disco() <= self.get_torre(target).get_ultimo_disco():
                self.get_torre(target).empilhar(
                    self.get_torre(source).desempilhar())
        except TypeError:
            print("")

    def iniciar(self):
        while True:
            try:
                self.iniciar_torres()
                qtd_discos = int(
                    input("Digite a quantidade de discos (3 à 8): "))
                if qtd_discos >= 3 and qtd_discos <= 8:
                    self.iniciar_discos(qtd_discos)
                    break
            except ValueError:
                print("\nQuantidade inválida!\n")

    def exibir_torres(self):
        self.get_torre(1).to_string()
        print("\n---------\n")
        self.get_torre(2).to_string()
        print("\n---------")
        self.get_torre(3).to_string()
        print("\n---------\n")

    def opcoes(self):
        print(color + "1 - Torre 1 para Torre 2")
        print("2 - Torre 1 para Torre 3")
        print("3 - Torre 2 para Torre 1")
        print("4 - Torre 2 para Torre 3")
        print("5 - Torre 3 para Torre 1")
        print("6 - Torre 3 para Torre 2")

    def escolher_opcao(self):
        try:
            self.opcoes()
            opcao = int(input("\nDigite uma opção: "))

            if opcao == 1:
                self.trocar_disco_de_torre(1, 2)
            elif opcao == 2:
                self.trocar_disco_de_torre(1, 3)
            elif opcao == 3:
                self.trocar_disco_de_torre(2, 1)
            elif opcao == 4:
                self.trocar_disco_de_torre(2, 3)
            elif opcao == 5:
                self.trocar_disco_de_torre(3, 1)
            elif opcao == 6:
                self.trocar_disco_de_torre(3, 2)
            else:
                print("\nOpção inválida!\n")

        except ValueError:
            print("\nOpção inválida!\n")

    def vencer(self):
        if self.get_torre(1).get_tamanho() == 0 and self.get_torre(2).get_tamanho() == 0:
            return True
        return False

    def jogar(self):
        self.iniciar()
        while not self.vencer():
            self.escolher_opcao()
            self.exibir_torres()
            
        print("Venceu!")
