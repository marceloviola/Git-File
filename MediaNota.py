boas = str(input('Olá!Qual o seu nome?:'))
dis = str(input('{} Digite a Disciplina à Consulta:'.format(boas)))
print('Oi! {}, Vamos ver se você foi aprovada na Disciplina :{}'.format(boas, dis))
nota1 = float(input('Digite a Nota do Semestre:'))
nota2 = float(input('Digite a Nota do Bimestre:'))
media = (nota1 + nota2) / 2
if media >= 7:
    print('Parabens! {} você foi aprovada com a Média {}'.format(boas, media))
    print('Está de Férias!')
else:
    print('{}, sua Média foi {}, portanto você não atingiu a Média da {}'.format(boas, media, dis))
    print('Estará em Recuperação na Disciplina {}'.format(dis))
print('--FIM--')