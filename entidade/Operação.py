class Operação:
    def __init__(self) -> None:
        pass
    def adição(self, parcela1, parcela2):
        resultado = [0] * (len(parcela1))
        vai_um = 0
        aux = 0
        for i in range(len(parcela1) - 1, -1, -1):
            aux = parcela1[i] + parcela2[i] + vai_um
            resultado[i] = aux %2 #resultado do bit é o resultado da divisão por 2
            vai_um = aux //2 #quociente da divisão por 2

                
        
        return resultado
    def subtração(self, minuendo, subtraendo):
        resultado = []
        #dois numeros positivos
        # subtraendo é da primeira prosição sendo ela 
        #maior significado ou seja do sinal positivo subtração normal
        if(minuendo[0] == 0  and subtraendo[0] == 0):
            subtraendo = self.complemento1(subtraendo)
            subtraendo = self.complemento2(subtraendo)
            resultado = self.adição(parcela1=minuendo, parcela2=subtraendo)
        #caso minuendo positivo e o subtrando negativo
        elif(minuendo[0] == 0 and subtraendo[0] == 1):
            subtraendo = self.complemento1(subtraendo)
            subtraendo = self.complemento2(subtraendo)
            resultado = self.adição(parcela1=minuendo, parcela2=subtraendo)
        #caso 3 minuendo sendo negativo e subtraendo positivo
        elif(minuendo[0] == 1 and subtraendo[0] == 0):
           subtraendo =  self.complemento1(subtraendo)
           subtraendo =  self.complemento2(subtraendo)
           resultado = self.adição(parcela1=minuendo, parcela2=subtraendo)
        #caso 4 ambos sendo negativos
        elif(minuendo[0] == 1 and subtraendo[0] == 1):
            subtraendo = self.complemento1(subtraendo)
            subtraendo = self.complemento2(subtraendo)
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
    def divisão(self,divisor=list, dividendo=list):
        #resto
        m = divisor.copy()
        if(m[0] == 1):
            m= self.complemento1(m)
            m = self.complemento2(m)
            m = [0]* len(divisor) + m
            a = [0] * len(dividendo) + dividendo.copy()
            q = dividendo.copy()
        else:
            #quociente
            a = [0] * len(dividendo)#a inicia um vetor com 0 do tamanho dos bits 
            q = dividendo.copy()
        contador = len(q)
        while(contador > 0):
            self.deslocamentoEsquerdo(valor=a, valor2=q)
            # Etapa 4: Realizar A <- A - M
            a = self.subtração(minuendo=a, subtraendo=m.copy())
           
            if(a[0] == 1):
               
                q[-1] = 0
                a = self.adição(parcela1=a, parcela2=m)#restaura valor de a
            else:
                q[-1] = 1
            contador = contador - 1
        return (q, a)
                
   
    #desloca um bit para esquerda       
    def deslocamentoEsquerdo(self,valor, valor2):
        if(type(valor) == list and type(valor2) == list):
           valor.pop(0)#remove o primeiro elemento
           valor.append(valor2.pop(0)) #insere no final da lista de valor o primeiro elemento do valor2 e remove o primeiro elemento do valor2
           valor2.append(0) #adiciona no final da lista o bit 0
    #desloca 1 bit para direita
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
        valor = [1 if bit == 0 else 0 for bit in valor]
        return valor
    #soma 1 no ultimo bit
    def complemento2(self, valor):
       soma_1 = [0] * (len(valor)-1)
       soma_1.append(1)
       aux = self.adição(valor, parcela2=soma_1)
       return aux