# arquivo = open('teste.txt', 'w')
# arquivo.write('Minha primeira escrita') # w sobrescreve oq está escrito
# arquivo.close()


# arquivo = open('teste.txt', 'a')
# # arquivo.write('\n Segunda Linha')
# arquivo.write('\n Terceira Linha')
# arquivo.close()
import shutil #importando a biblioteca shutil

def escrever_arquivo(texto):
    diretorio = 'C:/Users/igorm/Documents/teste.txt' # / barra invertida
    arquivo = open(diretorio, 'w')
    arquivo.write(texto) # w sobrescreve oq está escrito
    arquivo.close()

def atualizar_arquivo(nome_arquivo,texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto) # a atualiza o arquivo sem sobrescrevelo
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r') # read
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    lista_media = []
    arquivo = open(nome_arquivo, 'r')
    aluno_notas = arquivo.read()

    aluno_notas = aluno_notas.split('\n') #transforma em lista
    # print(aluno_notas)
    for x in aluno_notas:
        lista_notas = x.split(',')
        # print(lista_notas)
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([float(i) for i in notas]) / 4 #transformou em inteiros, somou tudo e dividiu por 4
        print('A media de {} foi : {} \n'.format(aluno,media(lista_notas)))
        #armazenar o nome e as medias em um dicionario
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

        # for i in lista_notas:
        #     float(i)
        # print(lista_notas)

def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo,'C:/Users/igorm/Desktop/')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'C:/Users/igorm/Documents/')


if __name__ == '__main__':

    move_arquivo('notas.txt')
    # copia_arquivo('notas.txt')

    # lista = media_notas('notas.txt')
    # print(lista)

    # escrever_arquivo('Primeira linha \n')
    # atualizar_arquivo('Segunda Linha \n')
    # ler_arquivo('teste.txt')
    # aluno = '\nJoas , 5,10,5,7 '
    # atualizar_arquivo('notas.txt', aluno)

