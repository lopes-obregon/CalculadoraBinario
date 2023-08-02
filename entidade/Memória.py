class Memória:
    def __init__(self):
        self.operando1 = 0
        self.operando2 = 0
        self.representação_do_inteiro = 0
        self.operando1_bin = []
        self.operando2_bin = []
        self.operação_escolhida = ""
    
    def setRepresentaçãoInteiro(self, representação_do_inteiro):
        if representação_do_inteiro == 8 or representação_do_inteiro == 16 or representação_do_inteiro == 32:
            self.representação_do_inteiro = representação_do_inteiro            
        else:
            print("Valor fora do suportado!")