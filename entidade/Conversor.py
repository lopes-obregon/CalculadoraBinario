class Conversor:
    def __init__(self) -> None:
        pass

    def converteBin(self, operando, tamanho_sifra):
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
            #print("Aqui")
            #print(resultado)
        #adiciona o resultado final da divisão
        resto.append(resultado)
        #preenche com os bits faltantes
       
        while len(resto) <= tamanho_sifra - 1:
            resto.append(0)
        
  
        #print(resto)
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
   
        
        