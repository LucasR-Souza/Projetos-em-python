import random  # biblioteca para o RNG


class Cartas:
    def __init__(self):
        self.cartas = []  # array para o método criar_cartas
        self.jogadores = []  # array com lista de jogadores
        self.baralho_jogado = []
        self.ordem_jogadores = []

    def criar_cartas(self):

        cores = ["vermelho", "amarelo", "azul", "verde"]
        especiais = ["bloqueio", "reverse", "+2"]

        for i in range(0, 2):      # Loop para a criação da quantidade correta das cartas (112)
            for cor in cores:
                for numero in range(0, 10):
                    self.cartas.append({"nome": str(numero), "cor": cor, "ID": i})  # O id é usado para diferenciar cartas da mesma cor
                for especial in especiais:
                    self.cartas.append({"nome": especial, "cor": cor, "ID": i})
        for i in range(0, 4):
            self.cartas.append({"nome": 'Coringa de cor', "cor": None, "ID": i})
            self.cartas.append({"nome": '+4', "cor": None, "ID": i})

    def adicionar_jogador(self, nome):
        self.jogadores.append({"nome": nome, "cartas": []})
        for i in range(0, 7):
            self.jogadores[-1]['cartas'].append(self.cartas.pop(random.randint(0, len(self.cartas) - 1)))

    def embaralhar(self):

        cores = ["vermelho", "amarelo", "azul", "verde"]
        especiais = ["bloqueio", "reverse", "+2"]

        for i in range(0, 2):      # Loop para a criação da quantidade correta das cartas (112)
            for cor in cores:
                # verificação das cartas normais
                for numero in range(0, 10):
                    encontrada = False  # variavel local
                    for carta_especifica in self.cartas:
                        if carta_especifica == {'nome': str(numero), 'cor': cor, 'ID': i}:
                            encontrada = True
                            break
                        else:
                            encontrada = False
                    if encontrada == False:
                        self.cartas.append({"nome": str(numero), "cor": cor, "ID": i})
                # verificação das cartas especiais
                for especial in especiais:
                    encontrada = False
                    for carta_especifica in self.cartas:
                        if carta_especifica == {'nome': especial, 'cor': cor, 'ID': i}:
                            encontrada = True
                            break
                        else:
                            encontrada = False
                    if encontrada == False:
                        self.cartas.append({"nome": especial, "cor": cor, "ID": i})
        # Verificação do +4 e coringa de cor
        for i in range(0, 4):
            encontrada = False
            encontrada_1 = False
            for carta_especifica in self.cartas:
                if carta_especifica == {'nome': 'Coringa de cor', 'cor': None, 'ID': i}:
                    encontrada = True
                    break
                else:
                    encontrada = False
            if encontrada == False:
                self.cartas.append({"nome": 'Coringa de cor', "cor": None, "ID": i})

            for carta_especifica in self.cartas:
                if carta_especifica == {'nome': '+4', 'cor': None, 'ID': i}:
                    encontrada_1 = True
                    break
                else:
                    encontrada_1 = False
            if encontrada_1 == False:
                self.cartas.append({"nome": '+4', "cor": None, "ID": i})

    def iniciar(self):
        # Define a ordem dos jogadores
        jogadores_possiveis = self.jogadores.copy()
        for i in range(len(self.jogadores)):
            self.ordem_jogadores.append(jogadores_possiveis.pop(random.randint(0, len(jogadores_possiveis) - 1)).get('nome'))
        print(f"A ordem de jogadores será a seguinte, da esquerda para a direita: {self.ordem_jogadores}")
        # Joga a primeira carta do jogo
        self.baralho_jogado.append(self.cartas.pop(random.randint(0, len(self.cartas) - 1)))
        while True:
            if self.baralho_jogado[len(self.baralho_jogado) - 1].get('nome') not in ['Coringa de cor', '+4']:
                break
            else:
                self.baralho_jogado.append(self.cartas.pop(random.randint(0, len(self.cartas) - 1)))
        print(f"A primeira carta do baralho é a: [Nome: {self.baralho_jogado[-1].get('nome')}, cor: {self.baralho_jogado[-1].get('cor')}]")
        # Chama a função principal
        self.main()


    def escolher_carta(self, jogador):
        #Exibe as cartas que o jogador possui
        print("As cartas que você tem na mão são: ")
        cartas = jogador.get('cartas')
        print("-------------------------------")
        for numero, carta in enumerate(cartas):
            if carta.get('cor') is not None:
                print(f"{numero}. Nome: {carta.get('nome')}, cor: {carta.get('cor')}")
            else:
                print(f"{numero}. Nome: {carta.get('nome')}")
        #Faz o jogador escolher a carta que vai jogar
        while True:
            escolhida = input("Digite o número da carta que deseja jogar ou '-1' para retroceder: ")
            if int(escolhida) == -1:
                return None
            elif int(escolhida) > len(cartas) - 1 or int(escolhida) < 0 :
                print("Valor inválido!!!")
            else:
                carta_escolhida = cartas[int(escolhida)]
                if carta_escolhida.get('cor') in [self.baralho_jogado[-1].get('cor'), None] or carta_escolhida.get('nome') == \
                        self.baralho_jogado[-1].get('nome'):
                    print("correct")
                    del cartas[int(escolhida)]
                    return carta_escolhida
                else:
                    print("Carta errada, tente outra ou compre uma nova carta!!")


    # Função pricipal que faz o jogo acontecer
    def main(self):
        #menu
        escolha_menu = input("--------------------Menu--------------------"
              "\nDigite 1 para jogar uma carta do seu baralho"
              "\nDigite 2 para comprar uma nova carta"
              "\nDigite 3 para falar Uno"
              "\n--------------------------------------------"
              "\n:")
        if escolha_menu == "1":
        self.escolher_carta(jogadores[jogador_da_vez])
        elif escolha_menu == "2":
        elif escolha_menu == "3":
        else:

        self.escolher_carta(self.jogadores[0])










cards = Cartas()
cards.criar_cartas()
cards.adicionar_jogador("josé")
cards.adicionar_jogador("Maria")
cards.iniciar()
