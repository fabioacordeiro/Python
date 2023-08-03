'''
Terminal
pip install openai
gerar a API no site

'''
'''
import openai
from get_env import print_env
'''


import os
import openai
openai.organization = "fabioacordeiro@yahoo.com.br"
openai.api_key = os.getenv("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")


#curl https://api.openai.com/v1/models/text-davinci-003 \
#-H 'Authorization: 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'
{
  "data": [
    {
      "id": "model-id-0",
      "object": "model",
      "owned_by": "organization-owner",
      "permission": [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]
    },
    {
      "id": "model-id-1",
      "object": "model",
      "owned_by": "organization-owner",
      "permission": [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]
    },
    {
      "id": "model-id-2",
      "object": "model",
      "owned_by": "openai",
      "permission": [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]
    },
  ],
  "object": "list"
}

openai.Model.list()

#env = print_env(['app_key'])

#configura ambiente
#openai.api_key = env['app_key']
#model engine
model_engine = 'text-davinci-003'
while True:
    print(50*'-')
    prompt = input('Escreva algo')
    print(50*'-')
    #configurando a geração de espera
    completion = openai.Completion.create(
        engine = model_engine,
        prompt = prompt,
        max_tokens = 1024,
        temperature = 0.5,
    )
    response = completion.choises[0].text
    print(response)
    saida = input('Deseja sair do programa ? [S] sim [N] Não')[0].upper()
    if saida == 'S':
        break




'''
chave de API
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
'''
'''
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="code-davinci-002",
  prompt="\"\"\"\nUtil exposes the following:\nutil.openai() -> authenticates & returns the openai module, which has the following functions:\nopenai.Completion.create(\n    prompt=\"<my prompt>\", # The prompt to start completing from\n    max_tokens=123, # The max number of tokens to generate\n    temperature=1.0 # A measure of randomness\n    echo=True, # Whether to return the prompt in addition to the generated completion\n)\n\"\"\"\nimport util\n\"\"\"\nCreate an OpenAI completion starting from the prompt \"Once upon an AI\", no more than 5 tokens. Does not include the prompt.\n\"\"\"\n",
  temperature=0,
  max_tokens=64,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop=["\"\"\""]
)

'''