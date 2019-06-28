import eel

eel.init('src/web')

@eel.expose
def connect(host):
    eel.sleep(5); # Set Delay To Test Loading
    return "success"

eel.start('index.html', size=(1000,800))
