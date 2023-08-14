class View:
    def __init__(self):
        self.operando1 = 0
        self.operando2 = 0
        self.tamanho_representação_inteiro = 0
        self.operação = ""

    def entradaDeDados(self):
        print("╔════════════════════════════════════════════════════╗")
        print("║                CALCULADORA BINÁRIA                 ║")
        print("╚════════════════════════════════════════════════════╝")
        print("\nInforme os operandos e a operação:\n")
        self.tamanho_representação_inteiro = int(input("Qual o Tamanho de representação do inteiro (8, 16, 32 bits): "))
        self.operando1 = int(input("Digite o Primeiro operando: "))
        self.operando2 = int(input("Digite o Segundo operando: "))
        self.operação = input("Qual Operação deseja realizar (+, -, *, /): ")

    def imprimirBinário(self, valor):
        binary_repr = format(valor, '0' + str(self.tamanho_representação_inteiro) + 'b')
        return [int(bit) for bit in binary_repr]

    def imprimirResultado(self, resultado):
        print("\n╔══════════════════════════════════════════════════════╗")
        print("║                RESULTADO DA OPERAÇÃO                 ║")
        print("╚══════════════════════════════════════════════════════╝")
        print("\n╔══════════════════════════════════════════════════════╗")
        print("║                     Operando 1                       ║")
        print("╚══════════════════════════════════════════════════════╝")
        print("Binário: ", ' '.join(map(str, self.imprimirBinário(self.operando1))))
        print("Decimal:", self.operando1)
        print("\n╔══════════════════════════════════════════════════════╗")
        print("║                     Operando 2                       ║")
        print("╚══════════════════════════════════════════════════════╝")
        print("Binário: ", ' '.join(map(str, self.imprimirBinário(self.operando2))))
        print("Decimal:", self.operando2)
        print("\n╔══════════════════════════════════════════════════════╗")
        print("║                     RESULTADO                        ║")
        print("╚══════════════════════════════════════════════════════╝")
        print("Binário: ", ' '.join(map(str, self.imprimirBinário(resultado))))
        print("Decimal:", resultado)

# Exemplo de uso da classe

#view = View()
#view.entradaDeDados()

#if view.operação == '+':
#    resultado = view.operando1 + view.operando2
 #   operacao_texto = "Soma]"
#elif view.operação == '-':
 #   resultado = view.operando1 - view.operando2
  #  operacao_texto = "Subtração]"
#elif view.operação == '*':
 #   resultado = view.operando1 * view.operando2
  #  operacao_texto = "Multiplicação]"
#elif view.operação == '/':
 #   resultado = view.operando1 // view.operando2
  #  operacao_texto = "Divisão]"

#print("\n[Operação Realizada:", operacao_texto)
#view.imprimirResultado(resultado)


