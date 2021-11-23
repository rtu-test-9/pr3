from contracts import contract

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

diagnoses = ['Гастрит',
             'Грибок',
             'Колит',
             'Полиомиелит',
             'Энцефалит',
             'Сифилис',
             'Инсульт',
             'Цистит',
             'Грибок']

class Interviewer:

    @contract(data='dict')
    def getDiagnosesCount(self, data):
        count = 0
        for key in data:
            if (data[key] != None):
                count += len(data[key])
        return count

    @contract(key='str', data='dict')
    def getPropability(self, key, data):
        count = 0
        wantedCount = 0
        for k in data:
            if (data[k] != None and key in data[k]):
                wantedCount += 1
            if (data[k] != None):
                count += len(data[k])
        try:
            return wantedCount/count
        except ZeroDivisionError:
            return 0

    @contract(key='str', data='dict')
    def ask(self, key, data):
        print("У вас есть симптом " + str(key) + " ?")
        answer = input()
        print(answer)
        if (answer == 'y' or answer == 'Y'):
            return data
        elif (answer == 'n' or answer == 'N'):
            data[key] = None
            return data
        else:
            return None
    @contract(data='dict', returns='bool')
    def run(self, data):
        dataCopy = data
        while(self.getDiagnosesCount(dataCopy) > 1):
            for key in dataCopy:
                if (dataCopy[key] != None):
                    dataCopy = self.ask(key, dataCopy)
                    print("На данный момент мы оцениваем вероятности диагнозов следующим образом: ")
                    for diagnos in diagnoses:
                        print(str(diagnos) + " " + str(self.getPropability(diagnos, dataCopy)*100) + "%")
        print("Итоговая оценка вероятностей: ")
        for diagnos in diagnoses:
            print(str(diagnos) + " " + str(self.getPropability(diagnos, dataCopy)*100) + "%")
        if (self.getDiagnosesCount(dataCopy) == 1):
            return True
        else:
            return False