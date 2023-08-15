#importando as classes
from entidade.Memória import Memória
from entidade.Conversor import Conversor
from entidade.Operação import Operação
class Controle:
    #init da classe controle
    def __init__(self) -> None:
        self.memória = Memória()
        self.conversor = Conversor()
        self.operação = Operação()
    #controle responsavel por solicitar uma escrita na memória
    def salveMemória(self, operando1=int, operando2=int, tamanho_representação_inteiro=int, operação=str ):
       #salvando dados para depois utilizarmos
        self.memória.operando1 = operando1
        self.memória.operando2= operando2
        self.memória.setRepresentaçãoInteiro(tamanho_representação_inteiro)
        self.memória.operação_escolhida = operação
        #convertendo dado  e salvando para utilizarmos depois
        self.conversorBin(operando1=operando1, operando2=operando2, tamanho_bit=tamanho_representação_inteiro)
    #chamada do método de converter da classe conversor
    def conversorBin(self, operando1=int, operando2=int , tamanho_bit=int):
        
        #convertendo os inteiros para binários
        self.memória.operando1_bin = self.conversor.converteBin(operando=operando1, tamanho_sifra=tamanho_bit)
        self.memória.operando2_bin = self.conversor.converteBin(operando=operando2, tamanho_sifra=tamanho_bit)
    #método que faz a soma de dois operando
    def operaçãoSoma(self):
         #verificamos para ter certeza que trata de uma soma
         if(self.memória.operação_escolhida == "+"):
           #pegamos os valores da memória e jogamos em duas variaveis e retornamos o resultado
           parcela1 = self.memória.operando1_bin
           parcela2 = self.memória.operando2_bin
           #mandamos dois operandos e recebebos um resultado em binário
           resultado = self.operação.adição(parcela1=parcela1, parcela2=parcela2)
           #convertemos esse binário para inteiro e retornamos ele
           resultado_dec_int = self.conversor.converteBinParaDec(resultado)
           return resultado_dec_int
    #operação subtração
    def operaçãoSubtração(self):
        #verificamos se trata uma subtração.
        if(self.memória.operação_escolhida == "-"):
            #pegamos da memória os binários
            bin1 = self.memória.operando1_bin
            bin2 = self.memória.operando2_bin
            #realizamos uma subtração e retornamos em binário
            resultado = self.operação.subtração(minuendo=bin1, subtraendo=bin2)
            #convertemos para inteiro o binário e retornamos
            resultado_dec_int = self.conversor.converteBinParaDec(resultado)
            return resultado_dec_int
    #método para multiplicação
    def operaçãoMultiplicação(self):
        #verificamos existencia de multiplicação
        if(self.memória.operação_escolhida == "*"):
            #pegamos dado da mémoria em binário
            multiplicando=self.memória.operando1_bin
            multiplicador=self.memória.operando2_bin
            quantidade_bits=self.memória.representação_do_inteiro
            #realizamos a multiplicação por booth
            resultado  = self.operação.multiplicação(multiplicando= multiplicando, multiplicador=multiplicador, quantidade_bits=quantidade_bits)
            #pegamos o resultado(binário) e convertemos em inteiro e retornamos
            resultado_dec_int = self.conversor.converteBinParaDec(resultado)
            return resultado_dec_int
    #operação de divisão
    def operaçãoDivisão(self):
       #verificamos se é uma divisão
       if(self.memória.operação_escolhida == "/"):
                #pegamos dados da memória
                dividendo = self.memória.operando1_bin
                divisor = self.memória.operando2_bin
                (quociente, resto) =  self.operação.divisão(dividendo=dividendo, divisor=divisor)
                #pegamos resultado binario e convertamos para inteiro e retornamos
                quociente_int = self.conversor.converteBinParaDec(quociente)
                resto_int = self.conversor.converteBinParaDec(resto)
                return(quociente_int, resto_int)
           