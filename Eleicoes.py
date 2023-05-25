nome = input('Digite seu Nome: ')
titulo = input('Digite seu Titulo: ')
candidatoPrefeito = input('Digite o número do candidato a prefeito: 1 = Zé das Couves, 2 = Ana Maria Praga (ou deixe em branco para voto em branco): ')
candidatoVereador = input('Digite o número do candidato a Vereador: 10 = Zeca Coitadinho, 20 = Faustina Silva (ou deixe em branco para voto em branco): ')

votoPrefeito = candidatoPrefeito

if candidatoPrefeito == '':
    print('Voto em Branco: Você Não Sabe Votar!')
elif votoPrefeito == 1:
    print('Zé das Couves será um prefeito maravilhoso! ')
elif votoPrefeito == 2:
    print('Ana Maria Praga será uma Péssima Prefeita! ')
else:
    print('Opção inválida: Você digitou um número de candidato inexistente para prefeito!')

votoVereador = candidatoVereador

if candidatoVereador == '':
    print('Voto Em Branco: Você Não Sabe Votar! ')
elif votoVereador == 10:
    print('Zeca Coitadinho Será um Vereador Maravilhoso! ')
elif votoVereador == 20:
    print('Faustina Silva Será uma Pessima Vereadora! ')
else:
    print('Opção inválida: Você digitou um número de candidato inexistente para vereador! ')


