from bs4 import BeautifulSoup
import requests

# Caminho para o arquivo HTML
# caminho_arquivo = "Naruttebane - Naruto - Naruto Shippuuden Download.html"

# Lê o conteúdo do HTML
# with open(links.txt, 'r', encoding='utf-8') as f:
#     conteudo = f.read()

link = 'https://www.dattebane.com/pagina/Naruto%20Shippuuden%20Download'
html = requests.get(link)
# Faz o parsing do HTML
soup = BeautifulSoup(html.text, 'html.parser')

# Encontra todos os <a> com o texto "HD" ou que contenham "download" no texto
links_encontrados = []

for a in soup.find_all('a', href=True):
    texto = a.get_text(strip=True).lower()
    if "download" in texto or texto == "hd":
        links_encontrados.append(a['href'])

# Remove duplicados
links_encontrados = list(set(links_encontrados))

# Salva os links em um arquivo de texto
with open("links_extraidos.txt", "w", encoding='utf-8') as f:
    for link in links_encontrados:
        f.write(link + "\n")

print("Links salvos em links_extraidos.txt")