from bs4 import BeautifulSoup
from requests import get
from os import listdir
from time import sleep

# Salvando todos os links em um arquivo
def set_links(url: str, folder: str):
  html = get(url)

  soup = BeautifulSoup(html.text, 'html.parser')

  # Encontrando todas as músicas
  songs = soup.find_all(attrs={ 'class': 'song-name' })

  # Salvando os links em um arquivo
  with open(f'musics/{folder}/links.txt', 'w') as file:
    for song in songs:
      file.write(f'https://www.letras.mus.br/{song["href"]}\n')


def get_links(folder: str) -> list:
  with open(f'musics/{folder}/links.txt', 'r') as file:
    links = file.read().split('\n')

  # Removendo link vazio, se tiver
  links.remove('')
  return links


def set_letter(folder: str, link: str):
  try:
    html = get(link)
  except:
    print('Não foi possível ver o link!')
    return

  soup = BeautifulSoup(html.text, 'html.parser')

  title_music = soup.find('h1').text # Título da música

  try:
    div_letters = soup.find(attrs={'class': 'cnt-letra p402_premium'})
    # Caso a música seja instrumental, lance a exceção
    if div_letters.p.text == '(Instrumental)':
      raise Exception()

    lines = []
    for strophe in div_letters.find_all('p'):
      text = str(strophe).replace('<p>', '').replace('</p>', '').replace('<br>', '\n').replace('<br/>', '\n').replace('</br>', '')

      for verse in text.split('\n'):
        lines.append(verse)

      lines.append('')
    name_file = title_music.replace(' ', '-')

    with open(f'musics/{folder}/{name_file}.txt', 'w') as file:
      file.write(f'{title_music}\n\n')
    
      for line in lines:
        file.write(f'{line}\n')

    print(f'Música "{title_music}" foi concluída!')
  except:
    print(f'A música "{title_music}" não possui letra!')


def agroup_letters_in_a_same_file():
  folders = listdir('musics')

  all_lines = []
  for folder in folders:
    name_files = listdir(f'musics/{folder}')
    name_files.remove('links.txt')

    for name in name_files:
      with open(f'musics/{folder}/{name}', 'r') as file:
        for line in file.read().split('\n'):
          all_lines.append(line)
        
    all_lines.append('')

  with open('all_letters.txt', 'w', encoding='utf-8') as file:
    for line in all_lines:
      file.write(f'{line}\n')

  
if __name__ == "__main__":
  folder = 'red-hot'
  url = 'https://www.letras.mus.br/red-hot-chili-peppers/'

  set_links(url, folder)

  for link in get_links(folder):
    set_letter(folder, link)

  agroup_letters_in_a_same_file()