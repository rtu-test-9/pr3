#Словарь в формате симптом - болезни
data = {
    "Черный язык": [
        "Гастрит",
        "Грибок",
        "Колит"
    ],
    "Паралич": [
        "Полиомиелит",
        "Энцефалит",
        "Клещевой",
        "Энцефалит",
        "Сифилис",
        "Инсульт"
    ],
    "Мания преследования": [
        "Инсульт",
    ],
    "Боль в уретре": [
        "Цистит",
        "Грибок"
    ]
}

class Interviewer:
        
    def getPropability(self, key, data):
        count = 0
        wantedCount = 0
        for k in data:
            if (data[k] != None and key in data[k]):
                wantedCount += 1
            if (data[k] != None):
                count += len(data[k])
        return wantedCount/count

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