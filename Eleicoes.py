nome = input('Digite seu Nome: ')
titulo = input('Digite seu Titulo: ')
candidatoPrefeito = int(input('Digite o numero do candidato a prefeito: 1 = Zé das Couves, 2 = Ana Maria Praga '))
candidatoVereador = int(input('Digite o numero do candidato a Vereador: 10 = Zeca coitadinho, 20 = Faustina Silva '))

votoPrefeito = candidatoPrefeito

if (votoPrefeito == 1):
    print('Zé das Couves será um prefeito maravilhoso! ')
elif (votoPrefeito == 2):
    print('Ana Maria Praga será uma Péssima Prefeita! ')
else:
    print('Voto Em Branco: Você Não Sabe Votar! ')

votoVereador = candidatoVereador

if (votoVereador == 10):
    print('Zeca Coitadinho Será um Vereador Maravilhoso! ')
elif (votoVereador == 20):
    print('Faustina Silva Será uma Pessima Vereadora! ')
else:
    print('Voto Em Branco: Você Não Sabe Votar! ')


