class biblioteca:
    def __init__(self):
        self.livros = []
    def adicionar_livro(self, titulo, autor, ano):
        self.livros.append({"titulo" : titulo, "autor" : autor, "ano" : ano})
        print("Livro adicionado com sucesso!!")


    def pesquisar_livro(self, livro_procurado):
        if self.livros == []:
            print("A biblioteca está vazia")
            return
        for livro in self.livros:
            if livro_procurado == livro["titulo"]:
                print(f"titulo: {livro['titulo']}, autor: {livro['autor']}, ano: {livro['ano']}")
                return
        print("Livro não encontrado.")

    def remover_livro(self, livro_removido):
        if self.livros == []:
            print("A biblioteca está vazia")
            return
        removido = None
        i = 0
        for livro in self.livros:
            if livro_removido == livro["titulo"]:
                removido = self.livros.pop(i)
                break
            i += 1
        if removido is not None:
            print(f"Você removeu o livro {removido['titulo']}!!")
        else:
            print("Livro não encontrado")


minha_biblioteca = biblioteca()
def main():
    while True:
        escolha_do_menu = input("\n1. Digite 1 para adicionar um livro \n"
                                "2. Digite 2 para remover um livro \n"
                                "3. Digite 3 para pesquisar um livro \n"
                                "4. Digite 4 para finalizar o programa:\n")
        if escolha_do_menu == '1':
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o nome do autor do livro: ")
            ano = input("Digite o ano de lançamento do livro: ")
            minha_biblioteca.adicionar_livro(titulo, autor, ano)
        elif escolha_do_menu == '2':
            titulo = input("Digite o título do livro que será removido: ")
            minha_biblioteca.remover_livro(titulo)
        elif escolha_do_menu == '3':
            titulo = input("Digite o título do livro que será pesquisado: ")
            minha_biblioteca.pesquisar_livro(titulo)
        elif escolha_do_menu == '4':
            print("Programa finalizado!!")
            break
        else:
            print("Erro!! Resposta inválida")

if __name__ == "__main__":
    main()