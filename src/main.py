import eel

eel.init('web')

@eel.expose
def hello_world():
    print("HELLO WORLD FROM THE BACKEND!")

eel.start('index.html', size=(800,800))
