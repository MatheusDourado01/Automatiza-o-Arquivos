import shutil, time, os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

path = 'C:/Users/matheus.valle/Documents/Automatização'
diretorios_destinos = {
    'path_destino' : 'U:/Automatização/Bloco de Notas - Estudos/csv',
    'path_destino2' : 'U:/Automatização/Bloco de Notas - Estudos/txt',
    'path_destino3' : 'U:/Automatização/Bloco de Notas - Estudos/png',
}

def diretorio_certo(nome_do_arquivo):
    root, ext = os.path.splitext(nome_do_arquivo).lower()
    if ext in diretorios_destinos:
        destino = diretorios_destinos[ext]
        if not os.path.exists(destino):
            os.makedirs(destino)
        
def nome_unico(nome_do_arquivo, path_destino):
    root, ext = os.path.splitext(nome_do_arquivo)
    contador = 1
    nome_novo = nome_do_arquivo
    while os.path.exists(os.path.join(path_destino, nome_novo)):
        nome_novo = f"{root}_{contador}{ext}"
        contador += 1
    return nome_novo

class OrganizadorDeArquivos(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Evento criado: {event}") 
        if not event.is_directory:
            print(f"Novo arquivo detectado: {event.src_path}")
            nome_arquivo = os.path.basename(event.src_path)
            try:
                nome_arquivo_unico = nome_unico(nome_arquivo, path_destino)
                destino_completo = os.path.join(path_destino, nome_arquivo_unico)
                print(f"Tentando mover para: {destino_completo}")  # Adicionando log
                shutil.move(event.src_path, destino_completo)
                print(f"Arquivo movido para {destino_completo}")  # Corrigido aqui
            except FileExistsError as e:
                print(f"Arquivo já existe no destino: {e}")
            except OSError as e:
                print(f"Erro do sistema operacional: {e}")
#observer.schedule(event_handler, path, recursive=True): 
# Configura o observador para usar o manipulador de eventos e monitorar o diretório especificado. 
# recursive=True permite que o observador monitore também subpastas.
print("Iniciando o observador...")
observer = Observer()
event_handler = OrganizadorDeArquivos()
observer.schedule(event_handler,path,recursive=True)
observer.start( )
print("Observador iniciado.")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
