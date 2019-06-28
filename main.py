#!/usr/bin/env python

from src.eagle import Eagle
import eel
import os
import _thread


@eel.expose
def connect(host):

    try:
        eagle.open(host)
        _thread.start_new_thread(eagle.watch(), ("Watch Thread"))
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


def main():
    print('Welcome to Eagle!')
    global eagle
    eagle = Eagle('eagle.conf', send_log_to_user)
    eel.init('src/web')
    eel.start('index.html', size=(1000, 800))


if __name__ == "__main__":
	main()
