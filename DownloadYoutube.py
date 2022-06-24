from pytube import YouTube
link = input('Digite o link do video que deseja baixar ')
nome = input('Digite o nome de usuario: ')
path = str(f'C:/Users/{nome.title()}/Downloads')
# path = input('Digite o diretorio que deseja guardar o video: ')
yt = YouTube(link)

print('Titulo: ', yt.title)
print('Numero de views:', yt.views)
print('Tamanho do video:', yt.length, 'segundos')
print('Avaliação do video:', yt.rating)

ys = yt.streams.get_highest_resolution()

print('Baixando...')
ys.download(path)
print(f'Download Concluido em {path}')

