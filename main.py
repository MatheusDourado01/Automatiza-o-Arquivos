import shutil, time, os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
path = 'C:/Users/matheus.valle/Documents/Automatização'
diretorios_destinos = {
    '.xlsx' : 'U:/Automatização/Bloco de Notas - Estudos/xlsx',
    '.txt' : 'U:/Automatização/Bloco de Notas - Estudos/txt',
    '.png' : 'U:/Automatização/Bloco de Notas - Estudos/png',
}

def nome_unico(nome_do_arquivo, destino):
    root, ext = os.path.splitext(nome_do_arquivo)
    contador = 1
    nome_novo = nome_do_arquivo
    while os.path.exists(os.path.join(destino, nome_novo)):
        nome_novo = f"{root}_{contador}{ext}"
        contador += 1
    return nome_novo

class OrganizadorDeArquivos(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Evento criado: {event}") 
        if not event.is_directory:
            ext = os.path.splitext(event.src_path)[1].lower()
            try:
                print(f"Essa é a {ext}")
            except Exception as e:
                print(f"Erro de {e}")
            if ext in diretorios_destinos:
                destino = diretorios_destinos[ext]
                nome_arquivo = os.path.basename(event.src_path)
                nome_arquivo_unico = nome_unico(nome_arquivo, destino)
                destino_completo = os.path.join(destino, nome_arquivo_unico)
                print(f"Novo arquivo detectado: {event.src_path}")
                try:
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
