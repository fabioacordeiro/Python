import openai
#Desenvolvido por Fábio Alves Cordeiro
#fabioacordeiro@yahoo.com.br
#11-95456-7877
openai.api_key = "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"
print(50*'-')
nomedoprograma = 'Inteligência Articial'
Dev = 'Created by: Fábio Alves Cordeiro'
Lang = 'Language: Python'
print(f'{nomedoprograma:^50}')
print(f'{Dev:^50}')
print(f'{Lang:^50}')
print(50*'-')
print('Este é um programa de computador que acessa a ')
print('Inteligência Articial ChatGPT do Elon Musk, ela')
print('não é perfeita, mas tem inúmeras possibilidades,')
print('foi treinada durante anos, use sua imaginação ')
print('e veja o poder da IA nos computadores.')


print(50*'-')

while True:
	ask = input('Faça uma pergunta para IA: ')
	response = openai.Completion.create(
  		model="text-davinci-003",
  		prompt=ask,
  		temperature=0.5,
  		max_tokens=150,
  		top_p=1,
  		frequency_penalty=0,
  		presence_penalty=0.6,
  		stop=[" Human:", " AI:"]
		)

	text = response['choices'][0]['text']
	print ('Resposta: '+text)
	print()
	sair = input('Deseja sair do programa ?[S]Sim ou [N]Não :')[0].upper()
	if sair == 'S':
		break