#importa a classe controle para main
from controle.Controle import Controle

if __name__ == "__main__":
    #cria o objeto controle
    controle = Controle()
    #chama entrada de dados
    controle.entradaDeDados()
    #salva na memória
    controle.salveMemória()
    #imprime os dados que estão na memória
    controle.printMemória()
    #converte para binário
    controle.conversorBin()
    #imprime para binário
    controle.printMemóriaBin()
    #vai para operação escolhida
    controle.operaçãoEscolhida()
