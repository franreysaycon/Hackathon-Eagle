import eel

eel.init('src/web')

@eel.expose
def get_my_name():
    return "World!"

eel.start('index.html', size=(800,800))
