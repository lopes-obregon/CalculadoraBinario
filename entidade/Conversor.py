class Conversor:
    def __init__(self) -> None:
        pass

    def converteBin(self, operando=int, tamanho_sifra=int):
        #guarda o resto da divisão
        resto = []
        tem_negativo = False
        resultado  = operando
        #tratamento negativo
        if(resultado < 0):
            resultado =  resultado * -1
            tem_negativo = True
        #calculo de conversão binario
        while resultado > 1:
            resto.append(resultado%2)
            resultado = int(resultado/2)
           
        #adiciona o resultado final da divisão
        resto.append(resultado)
        #preenche com os bits faltantes
       
        while len(resto) <= tamanho_sifra - 1:
            resto.append(0)
        #verifica se um dos operandos é negativo
        if(tem_negativo):
            #xor caso for inverte os bits
            for i in range(0, len(resto)):
                if resto[i] == 0:
                    resto[i] = 1
                else:
                    resto[i] = 0
            #complemento 2
            vai_um = 0
            for i in range(0, len(resto)):
                #soma 1
                if(i == 0):
                    resto[i] = resto[i] + 1
                    if(resto[i] > 1):
                        vai_um = 1
                        resto[i] = 0
                else:
                    resto[i] = resto[i] + vai_um
                    #significa que vai um 
                    if(resto[i] > 1):
                        resto[i] = 0
                        vai_um = 1
                    else:
                        vai_um = 0
     
        resto.reverse()
        return resto
   #método que converte de binário para decimal
    def converteBinParaDec(self, binário=list):
        sinal = 1 if binário[0] == 0 else -1# guarda o sinal do bit
        expoente = len(binário) - 1
        valor = 0
        #sinal negativo
        if(sinal == -1):
            binário = self.complemento1(binário)
            binário = self.complemento2(binário)
        for bit in binário:
            valor = valor +((2**expoente)*bit)
            expoente = expoente - 1
        valor = valor * sinal
        return valor
    #método que retorna complemento 1
    def complemento1(self, binário=list):
        valor = [1 if bit == 0 else 0 for bit in binário]  
        return valor
    #método que retorna complemento 2
    def complemento2(self, binário=list):
        resultado = [0] * (len(binário))
        parcela = [0] * (len(binário) - 1)
        parcela.append(1)
        vai_um = 0
        aux = 0
        for i in range(len(binário) - 1, -1, -1):
            aux = binário[i] + parcela[i] + vai_um
            resultado[i] = aux %2 #resultado do bit é o resultado da divisão por 2
            vai_um = aux //2 #quociente da divisão por 2

        
        return resultado