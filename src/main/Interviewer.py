#Словарь в формате симптом - болезни
data = {
    "Черный язык": {
        "Гастрит",
        "Грибок",
        "Колит"
    },
    "Паралич": {
        "Полиомиелит",
        "Энцефалит",
        "Клещевой",
        "Энцефалит",
        "Сифилис",
        "Инсульт"
    },
    "Мания преследования": {
        "Инсульт",
        ""
    },
    "Боль в уретре": {
        "Цистит",
        "Грибок"
    }
}

class Interviewer:
    field = []
    def ask(self, key, data):
        print("У вас есть симптом " + str(key) + " ?")
        answer = input()
        if (answer == 'y' or answer == 'Y'):
            data[key] = None
            return data
        elif (answer == 'n' or answer == 'N'):
            return data
        else:
            return None