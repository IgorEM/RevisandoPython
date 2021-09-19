class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada: # é igual a self.ligada == True - e if not self.ligada é igual a if self.ligada == False
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada == True:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada == True:
            self.canal -= 1


if __name__ == '__main__':

    televisao = Televisao() #instanciando a classe
    print('Televisão está ligada? : {}'.format(televisao.ligada))

    televisao.power()
    print('Televisão está ligada? : {}'.format(televisao.ligada))

    televisao.power()
    print('Televisão está ligada? : {}'.format(televisao.ligada))
    televisao.power()
    televisao.power()
    print('Televisão está ligada? : {}'.format(televisao.ligada))

    print('Canal: {}'.format(televisao.canal))
    televisao.aumenta_canal()
    televisao.aumenta_canal()
    televisao.aumenta_canal()
    print('Canal: {}'.format(televisao.canal))
    televisao.diminui_canal()
    televisao.diminui_canal()
    print('Canal: {}'.format(televisao.canal))


