# aqui ficara o codigo do projeto

media =  float(input('Media do aluno dever ser maior quer: '))

aluno = str(input('Qual e o nome do aluno: '))

nota1 = float(input('Qual foi a nota da primeira nota do aluno {} ? '.format(aluno)))
nota2 = float(input('Qual foi a nota da segunda nota do aluno {} ? '.format(aluno)))

media1 = (nota1 + nota2) / 2

print('O aluno {} ficou com media {}, ele passou de ano'.format(aluno, media1) 
      if media1 > media 
      else 'O aluno {} ficou com media {}, ele nao passou de ano'.format(aluno, media1))

##print('carro novo' if tempo<=3 else 'carro velho)


# if media1 > media:
#     print('O aluno {} ficou com media {}, ele passou de ano'.format(aluno ,media1))
# else:
#     print('O aluno {} ficou com media {}, ele nao passou de ano'.format(aluno ,media1)) 


print('fim do codigo')

