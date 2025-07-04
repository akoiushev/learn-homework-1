"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions_and_answers = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую", "Какой сегодня день недели?": "Понедельник", "Какой язык программирования твой любимый?": "Python"}

def ask_user(answers_dict):
    """
    Замените pass на ваш код
    """
    while True:
      user_say = input('Скажи что-нибудь: ')
      if user_say == 'Пока':
          print('Ну пока')
          break
      else:
          if user_say in questions_and_answers:
              print(questions_and_answers[user_say])
          else:
              print("Такого вопроса в словаре нет.")
          
    
    # answer = questions_and_answers.get(user_say)
    # print(answer)
    
if __name__ == "__main__":
    ask_user(questions_and_answers)
