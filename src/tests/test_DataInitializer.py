from main.Interviewer import Interviewer, data


def test_ask():
    # Чтобы успешно запустить данный тест, необходимо ответить на вопросы следующим образом:
    # паралич - "y"
    # мания преследования - "n"
    # боль в уретре - любая строка кроме "y", "Y", "n", "N"

    interviewer = Interviewer()
    dataCopy = data.copy()
    dataCopy["Паралич"] = None

    result = interviewer.ask("Паралич", data=data)
    result = interviewer.ask("Мания преследования", data=data)
    noneTest = interviewer.ask("Боль в уретре", data=data)
    assert dataCopy["Паралич"] == result["Паралич"]
    assert dataCopy["Мания преследования"] == result["Мания преследования"]
    assert None == noneTest