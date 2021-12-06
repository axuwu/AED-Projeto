from timeit import default_timer
import datetime
import random

#Queue
class Queue():
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0,item)
    def size(self):
        return  len(self.items)
    def dequeue(self):
        return self.items.pop()

#Passageiro
class Passageiro:
    def __init__(self,bag_pass,ciclo_in):
        self.bag_pass=bag_pass
        self.ciclo_in=ciclo_in
    def obtem_bag_pass(self):
        return self.bag_pass
    def obtem_ciclo_in(self):
        return self.ciclo_in
    def __str__(self):
        return '[bagagens: '+ str(self.obtem_bag_pass())+' | Ciclo: '+ str(self.obtem_ciclo_in())+']'

#Balcao
class Balcao:
    def __init__(self,n_balcao,fila,inic_atend,passt_atend,numt_bag,tempt_esp,bag_utemp):
        self.n_balcao=n_balcao
        self.fila=fila
        self.inic_atend=inic_atend
        self.passt_atend=passt_atend
        self.numt_bag=numt_bag
        self.tempt_esp=tempt_esp
        self.bag_utemp=bag_utemp
    def muda_inic_atend(self):
        passageiro_em_atendimento = self.obtem_fila().pop()
        self.__inic_atend = passageiro_em_atendimento.obtem_ciclo_in()
        self.incr_passt_atend()
        self.muda_numt_bag(passageiro_em_atendimento.obtem_bag_pass())
        self.muda_tempt_esp(passageiro_em_atendimento)
        self.__bag_utemp = self.obtem_numt_bag() / self.obtem_tempt_esp()
    def incr_passt_atend(self):
        self.passt_atend=0
        self.passt_atend=self.passt_atend+1
    def muda_numt_bag(self):
        self.__numt_bag += bag_passageiro
    def muda_tempt_esp(self):
        self.__tempt_esp += (tempo_atual() - passageiro.obtem_ciclo_in())
    def __str__(self):
        return ' balcÃƒÂ£o: '+ str(self.obtem_n_balcao) +' Tempo: ' + str(self.obtem_inic_atend())
    def obtem_n_balcao(self):
        return self.n_balcao
    def obtem_fila(self):
        return self.fila
    def obtem_inic_atend(self):
        return self.inic_atend
    def obtem_passt_atend(self):
        return self.passt_atend
    def obtem_numt_bag(self):
        return self.numt_bag
    def obtem_tempt_esp(self):
        return self.tempt_esp
    def obtem_bag_utemp(self):
        return self.bag_utemp

#Tempo de espera
class Timer(object):
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.timer = default_timer
    def __enter__(self):
        self.start = self.timer()
        return self
    def __exit__(self, *args):
        end = self.timer()
        self.elapsed_secs = end - self.start
        self.elapsed = self.elapsed_secs * 1000
        if self.verbose:
            print ("Tempo:", self.elapsed)

#Criar
def pass_probab(i, balcoes, num_balcoes, ciclos):
    balcoes = []
    balcoes = Queue()
    lista_atend = []
    for balcao in balcoes:
        lista_atend.append(balcao.obtem_fila().size())
    r =  random.randint(1, len(num_bag))
    print(r)
    c1=(ciclos*(1/3)//1) #ciclos dividido em 1/3
    c2=(ciclos*(2/3)//1) #ciclos dividido em 2/3
    if i<c1:
        with Timer() as t:
            balcoes[lista_atend(min(lista))].obtem_fila().enqueue((Passageiro(num_balcoes())))
            print ("Tempo:", t.elapsed)
    if i>c1 and i<c2 and r<0.8:
        with Timer() as t:
            balcoes[lista_atend(min(lista))].obtem_fila().enqueue((Passageiro(num_balcoes())))
            print ("Tempo:", t.elapsed)
    if i>c2 and r<0.6:
        with Timer() as t:
            balcoes[lista_atend(min(lista))].obtem_fila().enqueue((Passageiro(num_balcoes,())))
            print ("Tempo:", t.elapsed)
    mostrar_balcoes(balcoes)

#Mostrar
def mostrar_balcoes(balcoes):
    for balcao in balcoes:
        print(balcao)

#Simpar
def simpar_simula(num_pass, num_bag, num_balcoes, ciclos):
    lista_pass = []
    for i in range(int(num_balcoes)):
        lista_pass.append(Passageiro(num_bag ,ciclos))

    lista_balcoes = []
    for i in range(0, num_balcoes, 1):
        lista_balcoes.append(Balcao(i+1))

    for i in range(1, int(ciclos) + 1):
        print(" " + str(i) + " ")
        atende_passageiros(i, lista_balcao, num_balcoes, ciclos)

#Main
if __name__ == '__main__':

    #cont = True
    #while cont:
    #    num_pass = input("NÃƒÂºmero de passageiros:")
    #    if int(num_pass) > 0:
    #        cont = False
    #
    #cont = True
    #while cont:
    #    num_bag  = input("NÃƒÂºmero mÃƒÂ¡ximo de bagagens por passageiro:")
    #    if int(num_bag) > 0:
    #        cont = False
    #
    #cont = True
    #while cont:
    #    num_balcoes = input("NÃƒÂºmero de balcÃƒÂµes:")
    #    if int(num_balcoes) > 0:
    #        cont = False
    #
    #cont = True
    #while cont:
    #    ciclos = input("NÃƒÂºmero de ciclos:")
    #    if int(ciclos) > 0:
    #        cont = False

    num_pass=31 #n=um de passageiros com bagagem previsto para este voo
    num_bag=4   #num mÃƒÂ¡ximo de bagagens oermitido por passageiro
    num_balcoes=3  #num de balcoes abertoes para atendimento
    ciclos=3   #ciclos de tempo que a simulaÃƒÂ§ÃƒÂ£o decorre

    simpar_simula(num_pass, num_bag, num_balcoes, ciclos)








