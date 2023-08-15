from controle.Controle  import Controle
class View:
    def __init__(self):
        self.operando1 = 0
        self.operando2 = 0
        self.tamanho_representação_inteiro = 0
        self.operação = ""
        self.continuar = True
        self.controle = Controle()#importando a classe de controle
    #método que faz a entrada de  dados
    def entradaDeDados(self):
        print("╔════════════════════════════════════════════════════╗")
        print("║                CALCULADORA BINÁRIA                 ║")
        print("╚════════════════════════════════════════════════════╝")
        print("\nInforme os operandos e a operação:\n")
        self.tamanho_representação_inteiro = int(input("Qual o Tamanho de representação do inteiro (8, 16, 32 bits): "))
        self.operando1 = int(input("Digite o Primeiro operando: "))
        self.operando2 = int(input("Digite o Segundo operando: "))
        self.operação = input("Qual Operação deseja realizar (+, -, *, /): ")
        #chamando método que recebe alguns paramentros que salva na memória
        self.controle.salveMemória(self.operando1, self.operando2,self.tamanho_representação_inteiro, self.operação)
   #método que imprime em um formato limpo os binários
    def imprimirBinário(self, valor):
        binary_repr = format(valor, '0' + str(self.tamanho_representação_inteiro) + 'b')
        return [int(bit) for bit in binary_repr]
    #método que imprime o resultado das operações
    def imprimirResultado(self, resultado, resto=None, quociente=None):
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
        #caso tenha divisão imprimir  o resto e quociente
        if self.operação == '/':
            print("\n╔══════════════════════════════════════════════════════╗")
            print("║                DETALHES DA DIVISÃO                   ║")
            print("╚══════════════════════════════════════════════════════╝")
            print("Quociente: ", quociente)
            print("Resto: ", resto)
    #método que executa toda a calculadora
    def executarCalculadora(self):
        #loope para prermitir varias entradas
        while self.continuar:
            #chamada  para realizar a entrada de dados
            self.entradaDeDados()
            #verificação da operação e chamada para as operações a ser realizadas
            #Com formatação de texto
            if self.operação == '+':
                resultado = self.controle.operaçãoSoma()
                operacao_texto = "Soma"
            elif self.operação == '-':
                resultado = self.controle.operaçãoSubtração()
                operacao_texto = "Subtração"
            elif self.operação == '*':
                resultado = self.controle.operaçãoMultiplicação()
                operacao_texto = "Multiplicação"
            elif self.operação == '/':
                (quociente, resto) = self.controle.operaçãoDivisão()
                resultado = quociente
                operacao_texto = "Divisão"

            print("\n[Operação Realizada:", operacao_texto)
            #caso seja divisão imprimir com resto e quociente caso contrario somente resultado
            if self.operação == '/':
                self.imprimirResultado(resultado, resto, quociente)
            else:
                self.imprimirResultado(resultado)
            #perguntamos se queremos continuar
            continuar = input("\nDeseja continuar calculando? (s/n): ").strip().lower()
            #caso não queremos continuar encerramos
            if continuar != 's':
                self.continuar = False


# Exemplo de uso da classe

#view = View()
#view.executarCalculadora()
