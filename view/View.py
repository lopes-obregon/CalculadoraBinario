class View:
    def __init__(self) -> None:
        self.operando1 = 0
        self.operando2 = 0
        self.tamanho_representação_inteiro = 0
        self.operação = ""
    #imprime e recene p vaçpr fornecido
    def entradaDeDados(self):
        self.tamanho_representação_inteiro = int(input("Informe o tamanho de representação do inteiro:"))
        self.operando1 = int(input("Informe o primeiro operando:"))
        self.operando2 = int(input("Informe o segundo operando:"))
        self.operação = input("Informe operação:\t + -> Soma\t- -> Subtração\t* -> Multiplicação\t /  -> Divisão\n")
   #imprime um valor fornecido na tela
    def printMemória(self, valor):
        print(valor)