from entidade.Memória import Memória
from entidade.Conversor import Conversor
from view.View import View
from entidade.Operação import Operação
class Controle:
    #init da classe controle
    def __init__(self) -> None:
        self.memória = Memória()
        self.conversor = Conversor()
        self.view = View()
        self.operação = Operação()
    #controle responsavel por solicitar uma escrita na memória
    def salveMemória(self):
       
        self.memória.operando1 = self.view.operando1
        self.memória.operando2= self.view.operando2
        self.memória.setRepresentaçãoInteiro(self.view.tamanho_representação_inteiro)
        self.memória.operação_escolhida = self.view.operação
        #self.memória.setOperandos(operando1=self.view.operando1, operenado2=self.view.operando2)
       
    def entradaDeDados(self):
        self.view.entradaDeDados()  
    
    #imprime resultado da memória    
    def printMemória(self):
        operando1 = self.memória.operando1
        operando2 = self.memória.operando2
        self.view.printMemória("Operando 1:" + str(operando1))
        self.view.printMemória("Operando 2:" + str(operando2))
        #print(self.memória.operando1)
        #print(self.memória.operando2)
    def printMemóriaBin(self):
        lista1 = self.memória.operando1_bin
        lista2 = self.memória.operando2_bin
        operando1 = self.memória.operando1
        operando2 = self.memória.operando2
        self.view.printMemória("Operando em binário:"+str(lista1) + ":" +  str(operando1))
        self.view.printMemória("Operando em binário:"+str(lista2) + ":" +  str(operando2))
    #chamada do método de converter da classe conversor
    def conversorBin(self):
        
        self.memória.operando1_bin = self.conversor.converteBin(operando=self.memória.operando1, tamanho_sifra=self.memória.representação_do_inteiro)
        self.memória.operando2_bin = self.conversor.converteBin(operando=self.memória.operando2, tamanho_sifra=self.memória.representação_do_inteiro)
    def operaçãoEscolhida(self):
        if(self.memória.operação_escolhida == "+"):
           parcela1 = self.memória.operando1_bin
           parcela2 = self.memória.operando2_bin
           resultado = self.operação.adição(parcela1=parcela1, parcela2=parcela2)
           self.view.printMemória("Resultado soma:"+str(resultado)+ ":" + str(self.conversor.converteBinParaDec(resultado)))
        elif(self.memória.operação_escolhida == "-"):
            bin1 = self.memória.operando1_bin
            bin2 = self.memória.operando2_bin
            resultado = self.operação.subtração(minuendo=bin1, subtraendo=bin2)
            self.view.printMemória("Resultado Subtração:"+str(resultado)+ ":" + str(self.conversor.converteBinParaDec(resultado)))
        elif(self.memória.operação_escolhida == "*"):
            multiplicando=self.memória.operando1_bin
            multiplicador=self.memória.operando2_bin
            quantidade_bits=self.memória.representação_do_inteiro
            resultado  = self.operação.multiplicação(multiplicando= multiplicando, multiplicador=multiplicador, quantidade_bits=quantidade_bits)
            self.view.printMemória("Resultado Multiplicação:" + str(resultado)+ ":" + str(self.conversor.converteBinParaDec(resultado)))
        elif(self.memória.operação_escolhida == "/"):
            dividendo = self.memória.operando1_bin
            divisor = self.memória.operando2_bin
            
            (quociente, resto) =  self.operação.divisão(dividendo=dividendo, divisor=divisor)
            self.view.printMemória("Resultado Divisão")
            self.view.printMemória("Quociente:" + str(quociente)+ ":" + str(self.conversor.converteBinParaDec(quociente)))
            self.view.printMemória("Resto:" + str(resto)+ ":" + str(self.conversor.converteBinParaDec(resto)))
        else:
            self.view.printMemória("Operação inválida!")
