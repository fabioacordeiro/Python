import smtplib
#SMTP - SIMPLE MAIL TRANSFERE PROTOCOL
#lib de librari => biblioteca
#Mime é um formato padrão utilizado no envio de mensagens
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# Bibliotecas necessárias para envio de anexo 
# O arquivo em anexo é enviado de forma binária
from email.mime.base import MIMEBase
from email import encoders


# Passos
# 1 Iniciar o servidor
# 2 Construir do tipo MIME
# 3 Enviar o Email do tipo MIME do servidor SMTP

# 1 - Iniciando o servidor
vhost = "smtp.gmail.com"
porta = "587"
#porta = 465
login = "novosprojetos@gmail.com"
senha = "Fac@16705501847"

#server = smtplib.SMTP(port=porta, host=vhost)
server = smtplib.SMTP(vhost, porta)
#Inicializando o STARTTLS padrão do gmail
server.ehlo()
server.starttls()
server.login(login, senha)
print(60*'-')
print('Logado no servidor !!!')
# 2 Construindo o e-mail
corpo_do_email = "<b> Meu email de teste </b>"
email_msg = MIMEMultipart()
email_msg['From'] = login # De
email_msg['To'] = login #Para - Enviando para mim mesmo
email_msg['Subject'] = "Teste de envio de Email via Python - VSCODE"
email_msg.attach(MIMEText(corpo,'html'))

#anexando arquivo
Caminho_arquivo = "C:\\Fabio\\Python\\Extras\\Curriculum_2023_Projetos.pdf"
anexo = open(Caminho_arquivo, 'rb') # r = ready b = binary
# Codificando em base 64bits (Veja qual o seu tipo de arquivo no gerenciador do Window ou Linux)
anexar = MIMEBase('application', 'octec-stream')
anexar.set_payload(anexo.read())
encoders.encode_base64(anexar)

anexar.add_header('Content-Disposition', f'attachment; filename={Curriculum_2023_Projetos.pdf}')
anexar.close()
email_msg.attach(anexar)




# 3 Enviando o email tipo MIME no servidor SMTP
server.sendmail(email_msg['From'], email_msg['To'],email_msg.as_string())
server.quit()
print(60*'-')
print(f'{"Email enviado com Sucesso":^60}')
