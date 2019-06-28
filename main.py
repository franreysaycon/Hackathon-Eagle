#!/usr/bin/env python

from src.eagle import Eagle
import eel
import os
import threading


@eel.expose
def connect(host):

    try:
        eagle.open(host)
    except Exception as e:
        return {
            "success": False,
            "message": str(e)
        }

    return {
        "success": True
    }


def send_log_to_user(log):
	eel.push(log)

def watcher():
    while True:
        if eagle.running:
            eagle.watch()
        eel.sleep(1)

def main():
    print('Welcome to Eagle!')
    global eagle
    eagle = Eagle('eagle.conf', send_log_to_user)

    eel.init('src/web')
    x = threading.Thread(target=watcher)
    x.start()


    try:
        eel.start('index.html', size=(1000, 800))
    except (SystemExit, MemoryError, KeyboardInterrupt):
        eagle.close()

if __name__ == "__main__":
	main()
