import os
import sys
import shutil
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileSystemEventHandler
path = 'C:/Users/matheus.valle/Documents/Automatização'
class OrganizadorDeArquivos(FileExistsError):
    def on_created(self, event):
        if not event.is_directory:
            print(f"O caminho fornecido não é um diretório válido: {path}")
            sys.exit(1)

        
#observer.schedule(event_handler, path, recursive=True): 
# Configura o observador para usar o manipulador de eventos e monitorar o diretório especificado. 
# recursive=True permite que o observador monitore também subpastas.
event_handler = LoggingEventHandler()
observer = Observer()
observer.schedule(event_handler,path,recursive=True)
observer.start( )
#Listando os diretórios
for arquivos in os.listdir(path):
    print(arquivos)