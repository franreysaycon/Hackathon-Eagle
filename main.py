from paramiko import SSHClient
import eel

eel.init('src/web')


@eel.expose
def connect(host):
    ssh = SSHClient()
    try:
        ssh.load_system_host_keys()
        ssh.connect(username='dev', hostname=host + '.syd1.fln-dev.net')
    except Exception as e:
        return {
            "success": False,
            "message": e
        }

    return {
        "success": True
    }


eel.start('index.html', size=(1000, 800))
