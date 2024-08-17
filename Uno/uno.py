import random  # biblioteca para o RNG

class Cartas:
    def __init__(self):
        self.cartas = []  # array para o método criar_cartas
        self.jogadores = []  # array com lista de jogadores
        self.jogador_atual = 0
        self.baralho_jogado = []
        self.ordem_progressiva = True # usado para a carta de reverse
        self.comprar = 0 # usado para as cartas de comer
        self.classificacao = [] # Colocação

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
        print("cartas embaralhadas!!")

    def coringa_de_cor(self, carta):
        while True:
            num = int(input("Escolha uma cor "
                        "\nDigite 0 para vermelho"
                        "\nDigite 1 para verde"
                        "\nDigite 2 para azul"
                        "\nDigite 3 para amarelo"
                        "\n:"))
            if num == 0:
                carta['cor'] = 'vermelho'
                break
            elif num == 1:
                carta['cor'] = 'verde'
                break
            elif num == 2:
                carta['cor'] = 'azul'
                break
            elif num == 3:
                carta['cor'] = 'amarelo'
                break
            else:
                print("Valor inválido")
        return carta

    def comes(self, carta):
        self.comprar += int(carta.get('nome'))
        return carta

    def iniciar(self):
        # Define a ordem dos jogadores
        ordem_jogadores = []
        for jogador in self.jogadores:
            ordem_jogadores.append(jogador.get('nome'))
        print(f"A ordem de jogadores será a seguinte, da esquerda para a direita: {ordem_jogadores}")
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

    def proximo_jogador(self):
        if self.ordem_progressiva == True:
            if self.jogador_atual < len(self.jogadores) - 1:
                self.jogador_atual += 1
            else:
                self.jogador_atual = 0

        elif self.ordem_progressiva == False:
            if self.jogador_atual > 0:
                self.jogador_atual -= 1
            else:
                self.jogador_atual = len(self.jogadores) - 1

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
            try:
                carta_escolhida = cartas[int(escolhida)]
                if int(escolhida) == -1:
                    return None
                elif int(escolhida) > len(cartas) - 1 or int(escolhida) < 0:
                    print("Valor inválido!!!")
                # Obriga o jogador a jogar uma carta de come caso necessario
                elif self.comprar > 0:
                    if carta_escolhida.get('nome') == '+4' or carta_escolhida.get('nome') == '+2':
                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                        print(f"Você jogou a carta: {carta_escolhida}")
                        del cartas[int(escolhida)]
                        return carta_escolhida
                    else:
                        print("Carta errada, tente outra ou compre!!")
                else:
                    if carta_escolhida.get('cor') in [self.baralho_jogado[-1].get('cor'), None] or carta_escolhida.get(
                            'nome') == \
                            self.baralho_jogado[-1].get('nome'):
                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                        print(f"Você jogou a carta: {carta_escolhida}")
                        del cartas[int(escolhida)]
                        return carta_escolhida
                    else:
                        print("Carta errada, tente outra ou compre uma nova carta!!")
            except:
                print("Valor inválido!!")



    def jogar_carta(self, carta, uno, jogador):
        player = self.jogador_atual
        if carta['nome'] == 'reverse':
            self.ordem_progressiva = not self.ordem_progressiva
            print('A ordem de jogo se inverteu')
        elif carta['nome'] == 'bloqueio':
            self.proximo_jogador()
            print(f"A vez do(a) {self.jogadores[self.jogador_atual].get('nome')} foi pulada")
        elif carta['nome'] == 'Coringa de cor':
            carta = self.coringa_de_cor(carta)
        elif carta['nome'] == '+2':
            carta = self.comes(carta)
        elif carta['nome'] == '+4':
            carta = self.comes(carta)
            carta = self.coringa_de_cor(carta)
        self.baralho_jogado.append(carta)
        #Verifica se o jogador falou uno antes de jogar a carta
        if len(jogador['cartas']) == 0:
            if uno == False:
                print("Você esqueceu de falar uno e recebeu mais 2 cartas")
                self.comprar_carta(self.jogador_atual, 2)
            if uno == True:
                print(f"Parabéns {jogador['nome']}, suas cartas acabaram!!")
                self.classificacao.append(self.jogadores.pop(player))
                self.proximo_jogador()

    def comprar_carta(self, jogador, quantidade):
        if len(self.cartas) < quantidade:
            print("Quantidade de cartas no baralho insuficiente para comprar, pule sua vez ou embaralhe as cartas!!")
        else:
            for i in range(0, quantidade):
                    self.jogadores[jogador]['cartas'].append(self.cartas.pop(random.randint(0, len(self.cartas) - 1)))
                    print(f"Voce compro a carta {self.jogadores[jogador]['cartas'][-1]}!!")
            self.comprar = 0

    # Função pricipal que faz o jogo acontecer
    def main(self):
        while True:
            #menu
            while True:
                print(f"\nVez do {self.jogadores[self.jogador_atual]['nome']}")
                print(f"Ultima carta do baralho {self.baralho_jogado[-1]}")
                if self.comprar > 0:
                    print(f"Cartas para comprar: {self.comprar}")

                escolha_menu = input("--------------------Menu--------------------"
                                     "\nDigite 1 para jogar uma carta do seu baralho"
                                     "\nDigite 2 para comprar a(s) carta(s)"
                                     "\nDigite 3 para falar Uno e jogar uma carta"
                                     "\nDigite 4 embaralhar"
                                     "\nDigite 5 para pular a vez"
                                     "\n--------------------------------------------"
                                     "\n:")
                if escolha_menu == "1":
                    uno = False
                    carta = self.escolher_carta(self.jogadores[self.jogador_atual])
                    if carta is not None:
                        self.jogar_carta(carta, uno, self.jogadores[self.jogador_atual])
                        break
                elif escolha_menu == "2":
                    if self.comprar > 0:
                        self.comprar_carta(self.jogador_atual, self.comprar)
                    else:
                        self.comprar_carta(self.jogador_atual, 1)
                    break
                elif escolha_menu == "3":
                    uno = True
                    carta = self.escolher_carta(self.jogadores[self.jogador_atual])
                    if carta is not None:
                        self.jogar_carta(carta, uno, self.jogadores[self.jogador_atual])
                        break
                elif escolha_menu == "4":
                    self.embaralhar()
                elif escolha_menu == "5":
                    if len(self.cartas) > self.comprar:
                        print("O baralho ainda tem cartas para serem compradas, compre no lugar de pular!!")
                    else:
                        self.proximo_jogador()
                else:
                    print("Número fora do intervalo. Tente novamente.")
            #Olha se tem mais de 1 jogador com cartas na mão
            if len(self.jogadores) <= 1:
                print("A ordem de vencedores é:" )
                i = 1
                for jogador in self.classificacao:
                    print(f"{i}˚ {jogador["nome"]}")
                    i += 1
                break
            self.proximo_jogador()




cards = Cartas()
cards.criar_cartas()
cards.adicionar_jogador("josé")
cards.adicionar_jogador("Maria")
cards.adicionar_jogador("ana")
cards.iniciar()
