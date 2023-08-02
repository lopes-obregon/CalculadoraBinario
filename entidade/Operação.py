class Operação:
    def __init__(self) -> None:
        pass
    def adição(self, parcela1, parcela2):
        resultado = []
        vai_um = 0
        aux = 0
        for i in range(len(parcela1) - 1, -1, -1):
            aux = parcela1[i] + parcela2[i] + vai_um
            resultado.append(aux %2) #resultado do bit é o resultado da divisão por 2
            vai_um = aux //2 #quociente da divisão por 2

                
        #reverter para forma normal
        resultado.reverse()
        return resultado
    def subtração(self, minuendo, subtraendo):
        resultado = []
        #dois numeros positivos
        # subtraendo é da primeira prosição sendo ela 
        #maior significado ou seja do sinal positivo subtração normal
        if(minuendo[0] == 0  and subtraendo[0] == 0):
            self.complemento1(subtraendo)
            self.complemento2(subtraendo)
            resultado = self.adição(parcela1=minuendo, parcela2=subtraendo)
        #caso minuendo positivo e o subtrando negativo
        elif(minuendo[0] == 0 and subtraendo[0] == 1):
            self.complemento1(subtraendo)
            self.complemento2(subtraendo)
            resultado = self.adição(parcela1=minuendo, parcela2=subtraendo)
        #caso 3 minuendo sendo negativo e subtraendo positivo
        elif(minuendo[0] == 1 and subtraendo[0] == 0):
            self.complemento1(subtraendo)
            self.complemento2(subtraendo)
            resultado = self.adição(parcela1=minuendo, parcela2=subtraendo)
        #caso 4 ambos sendo negativos
        elif(minuendo[0] == 1 and subtraendo[0] == 1):
            self.complemento1(subtraendo)
            self.complemento2(subtraendo)
            resultado = self.adição(parcela1=minuendo, parcela2=subtraendo)
        return resultado
    def multiplicação(self, multiplicando, multiplicador, quantidade_bits):
        #esperado que já passa como reverso
        a = [0] * quantidade_bits
        q1 = 0
        q = []
        m = []
        
        #verifica o tipo da operação
        if(type(multiplicando) == list and type(multiplicador) == list ):
            #copia para não pegar o endereço, reverte para facilitar as contas
            q = multiplicando.copy()
            m = multiplicador.copy()
            while(quantidade_bits > 0):
                #comparação do ultimo bit de q com q-1
                if(q[len(q) - 1] == 1 and q1 == 0):
                    a = self.subtração(minuendo=a, subtraendo=m.copy())
                    #deslocamento
                    q1 = self.deslocamento(a=a,q=q,q1=q1)
                    quantidade_bits = quantidade_bits - 1
                elif(q[len(q) - 1] == 0 and q1 == 1):
                    a = self.adição(parcela1=a, parcela2=m.copy())
                    #deslocamento
                    q1 = self.deslocamento(a=a,q=q,q1=q1)
                    quantidade_bits = quantidade_bits - 1
                elif(q[len(q) - 1] == 1 and q1 == 1):
                    q1 = self.deslocamento(a=a, q=q, q1=q1)
                    quantidade_bits = quantidade_bits - 1
                elif(q[len(q) - 1] == 0 and q1 == 0):
                    q1 = self.deslocamento(a=a, q=q, q1=q1)
                    quantidade_bits = quantidade_bits - 1
            return q
        else:
            pass
    def divisão(self):
        pass
    def deslocamento(self,a, q, q1):
       #verifica tipo da varialvel
       if(type(a) == list and type(q) == list):
           #"duplica" a primeira
           aux = a[0]
           a.insert(0, aux)
           #remove o ultimo
           aux = a.pop()
           q.insert(0, aux)
           q1 = q.pop()
           return q1
        
# faz a negação dos bits inverte caso 1 vira 0 e caso  0 vira 1
    def complemento1(self, valor):
        #invertemos os bits do determinado valor ou array de bits
        for i in range(0, len(valor)):
            if(valor[i] == 0):
                valor[i] = 1
            else:
                valor[i] = 0
    #soma 1 no ultimo bit
    def complemento2(self, valor):
       soma_1 = []
       for i in range(len(valor)):
            # se i + 1 > tamanho de valor, então estamos na última posição
            if (i + 1 > len(valor) - 1):
                soma_1.append(1)
            else:
                soma_1.append(0)
        
       aux = self.adição(valor, parcela2=soma_1)
       #corrigir valor 
       self.copiaLista(aux, valor)
       
    def copiaLista(self, lista1, lista2):
        for i in range(0,len(lista1)):
            lista2[i] = lista1[i]