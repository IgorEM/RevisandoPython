class Calculadora:

    def __init__(self, num1, num2): #obrigatoriamente ele vai passar antes pelo método init
        self.valor_a = num1
        self.valor_b = num2

    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicacao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b

calculadora = Calculadora(10,2)
print(calculadora.soma(),'-',calculadora.subtracao(),'-',calculadora.multiplicacao(),'-',calculadora.divisao())

