import eel

eel.init('src/web')

@eel.expose
def connect(host):
    print(host)

eel.start('index.html', size=(1000,800))
