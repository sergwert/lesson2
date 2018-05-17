# Переписать функцию ask_user(), добавив обработку exception-ов
# Добавить перехват ctrl+C и прощание

def ask_user():
    ask=''
    while ask!="Хорошо":
        try:
            ask=input("Как дела? ")
        except KeyboardInterrupt:
            print("Я выхожу из игры")
            ask="Хорошо"

ask_user()