import sys
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class BotReloader(FileSystemEventHandler):
    def __init__(self):
        self.process = None
        self.restart_bot()

    def restart_bot(self):
        if self.process:
            print("\n🔄 Reiniciando bot...")
            self.process.terminate()
            self.process.wait()
        
        print("🚀 Iniciando bot...")
        self.process = subprocess.Popen([sys.executable, "main.py"])

    def on_modified(self, event):
        if event.src_path.endswith('.py'):
            print(f"\n📝 Arquivo modificado: {event.src_path}")
            self.restart_bot()

if __name__ == "__main__":
    print("👀 Modo desenvolvimento ativado - Auto-reload habilitado")
    print("Pressione Ctrl+C para parar\n")
    
    event_handler = BotReloader()
    observer = Observer()
    observer.schedule(event_handler, path='src', recursive=True)
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n🛑 Parando bot...")
        observer.stop()
        if event_handler.process:
            event_handler.process.terminate()
    
    observer.join()
