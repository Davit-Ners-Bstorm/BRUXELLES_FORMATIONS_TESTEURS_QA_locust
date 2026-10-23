def create_chat(nom):
    return {
        "name": nom
    }

def miauler(chat):
    print(f'{chat["name"]} miaule')

bernard_le_chat = create_chat('Bernard')

print(bernard_le_chat)

miauler(bernard_le_chat)

# Orienté objet
class Chat:
    def __init__(self, name):
        self.name = name
    
    def miauler(self):
        print(f'{self.name} miaule')

jerome_le_chat = Chat('Jerome')

print(jerome_le_chat.name)
jerome_le_chat.miauler()
