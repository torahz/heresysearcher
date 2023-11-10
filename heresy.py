import requests
from bs4 import BeautifulSoup

# Cabeçalho   

print("Pesquisador de Heresias: Qual heresia deseja pesquisar hoje?")

while True:
    term = input("Você: ")
    
    if term.lower() == "sair":
        break
        
    url = f"https://api.duckduckgo.com/?q={term}&format=json"
    results = requests.get(url).json()

    for result in results["relatedTopics"]["results"]:
            if "solascriptura-tt.org" in result["href"]:
            print("Encontrei um resultado relevante!")
            page = requests.get(result["href"])
            soup = BeautifulSoup(page.content, 'html.parser')
            text = soup.find('article').text
            print(text)
            break
            
    print("Deseja pesquisar mais alguma coisa?")
            
print("Encerrando o Pesquisador de Heresias...")
