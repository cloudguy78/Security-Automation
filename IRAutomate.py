#This python script will monitor a directory for new files and generate
#an alert if any file with a suspicious extension (eg. .exe, .bat) is
#added.

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Watcher:
    def __init__(self, directory):
        self.observer = Observer()
        self.directory = directory

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.directory, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()

    if __name__ == '__main__':
        watcher = Watcher("/path/to/monitor") #replace with the file path that you want to monitor
        watcher.run()