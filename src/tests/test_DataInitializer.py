from main.Interviewer import Interviewer, data


def test_ask():
    # Чтобы успешно запустить данный тест, необходимо ответить на вопросы следующим образом:
    # паралич - "y"
    # мания преследования - "n"
    # боль в уретре - любая строка кроме "y", "Y", "n", "N"

    interviewer = Interviewer()
    dataCopyActual = data.copy()
    dataCopyExpected = data.copy()
    dataCopyExpected["Паралич"] = None

    result = interviewer.ask("Паралич", data=dataCopyActual)
    result = interviewer.ask("Мания преследования", data=dataCopyActual)
    noneTest = interviewer.ask("Боль в уретре", data=dataCopyActual)
    assert dataCopyExpected["Паралич"] == result["Паралич"]
    assert dataCopyExpected["Мания преследования"] == result["Мания преследования"]
    assert None == noneTest

def test_getPropability():
    dataCopy = data.copy()
    interviewer = Interviewer()
    propability0 = interviewer.getPropability("Инсульт", dataCopy)
    propability1 = interviewer.getPropability("Гастрит", dataCopy)
    assert 2 / 12 == propability0
    assert 1 / 12 == propability1

def test_getDiagnosesCount():
    dataCopy = data.copy()
    interviewer = Interviewer()
    assert 12 == interviewer.getDiagnosesCount(dataCopy)

test_getPropability()