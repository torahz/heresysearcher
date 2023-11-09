from colorama import Fore, Style
import requests
from bs4 import BeautifulSoup

print(Fore.MAGENTA + Style.BRIGHT + """
 #####   #####  ####      ##    
##   ## ##   ##  ##      ####   
#       ##   ##  ##     ##  ## 
 #####  ##   ##  ##     ##  ##  
     ## ##   ##  ##   # ######  
##   ## ##   ##  ##  ## ##  ##  
 #####   #####   ###### ##  ## 

""" + Style.RESET_ALL)

print("Pesquisador de Heresias: Que heresia vai pesquisar hoje varão?")

while True:
  pergunta = input("Você: ")

  if pergunta.lower() == "sair":
    break

  url = f"https://solascriptura-tt.org/?s={pergunta}"
  resposta = requests.get(url)

  soup = BeautifulSoup(resposta.text, 'html.parser')
  
  # Procura pelo primeiro elemento article 
  conteudo = soup.find('article')

  if not conteudo:
    print(Fore.RED + "Misericóóóórdia irmão!!! Não vai te meter com isso viu" + Style.RESET_ALL)

  else:
    print(conteudo.text)

print(Fore.MAGENTA + "Encerrando o Pesquisador de Heresias..." + Style.RESET_ALL)
