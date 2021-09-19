import datetime
from datetime import date, time, datetime

def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%d/%m/%y') #formatar a data
    dia_atual_semana = data_atual.strftime('%A')

    print(type(dia_atual_semana)) #<class 'str'>
    print(type(data_atual_str)) #<class 'str'>
    print(type(data_atual)) #<class 'datetime.date'>
    print(dia_atual_semana)
    print(data_atual_str)
    print(data_atual)

def trabalhando_com_time():

    criei_horario = time(hour=13, minute=10, second=30) #datetime.time
    print(criei_horario)


def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y %H:%M:%S'))
    print(data_atual.strftime(('%c')))
    print(data_atual.day)
    print(data_atual.hour)
    print(data_atual.minute)
    print(data_atual.date())
    print(data_atual.weekday())
    tupla = ('Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Sabádo', 'Domingo')
    print(tupla[data_atual.weekday()])

    data_criada = datetime(2018,6,20,15,30,21)
    print(data_criada)
    print(data_criada.strftime('%c'))
    data_string = '01/04/2021'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y')
    print(data_convertida)
    print(data_convertida.weekday())


if __name__ == '__main__':
    # trabalhando_com_time()
    # trabalhando_com_date()
    trabalhando_com_datetime()