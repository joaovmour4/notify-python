import requests
import smtplib
import sys

# É passado um arquivo txt como argumento de inicialização para guardar os números das atualizações no site
arq = open(sys.argv[1], 'r+')
servidor_email = smtplib.SMTP('smtp.gmail.com', 587)


# The API endpoint
url = "https://8rm.eb.mil.br/en/?option=com_content&view=article&layout=edit&id=347"

# A GET request to the API
response = requests.get(url)

# Print the response
lines = arq.readlines()
actual = int(lines[-1])

if(f'AD 0{actual+1}' in response.text):
    actual+= 1
    arq.write(f'\n{actual}')
    servidor_email.starttls()
    servidor_email.login('seu-email@gmail.com', 'sua-senha-de-app')
    remetente = 'seu-email@gmail.com'
    destinatarios = 'destinatario@gmail.com'
    conteudo = 'Houve atualização no site!'

    servidor_email.sendmail(remetente, destinatarios, conteudo.format(destinatarios, remetente, conteudo).encode('utf-8'))
else:
    print('Nenhuma atualizaçao.')

servidor_email.quit()
arq.close()