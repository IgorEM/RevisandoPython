class Calculadora:
    # def __init__(self):
    #     pass

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self,valor_a,valor_b):
        return valor_a - valor_b

    def multiplicacao(self,valor_a,valor_b):
        return valor_a * valor_b

    def divisao(self,valor_a, valor_b):
        return valor_a / valor_b

if __name__ == '__main__':
    calculadora = Calculadora() #instanciando a classe calculadora
    print("------")
    print(calculadora.soma(5,2))
    print(calculadora.subtracao(5,2))
    print(calculadora.multiplicacao(5,2))
    print(calculadora.divisao(100,5))