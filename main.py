import os
import random
import speech_recognition
import pyttsx3

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.75
n = 1

commands_dict = {
    'commands': {
        'greeting': ['джарвис привет', 'джарвис включись'],
        'helper': ["джарвис какие у тебя есть команды", 'джарвис что ты умеешь'],
        'create_task': ['джарвис добавь задачу', 'джарвис создай задачу', 'джарвис задача'],
        'shut': ['джарвис выключись', 'спокойной ночи джарвис'],
        'open_todo_list': ['джарвис открой список дел', 'джарвис открой дела', 'джарвис дела'],
        'erase_todo_list': ['джарвис очисти список дел', 'джарвис удали дела', 'джарвис я закрыл все дела', 'джарвис удалить дела'],
        'shutComp': ['джарвис выключи компьютер', 'джарвис выключи комп'],
    }
}


def open_todo_list():
    os.system('todo-list.txt')
    return "Ваши дела на сегодня, перед вами"


def shutComp():
    os.system('shutdown /s /t 1')
    return 'Пока-пока, создатель!'


def erase_todo_list():
    f = open('todo-list.txt', 'r+')
    f.truncate(0)
    return "Все ваши дела очищены. Не бездельничайте, заполните этот список снова!"


def helper():
    return ("Я голосовой помощник Джарвис, я могу отвечать вам на заранее прописанные команды, такие как - создать "
            "задачу, очистить список дел, выклучить компьютер. Более подробно можно узнать на GitHub проекта.")


def listen_command():
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()

        return query
    except speech_recognition.UnknownValueError:
        return 'Не распознан голос. Проблема с вводом звука'


def greeting():
    return 'Привет, создатель, чем могу помочь?'


def create_task():

    engine = pyttsx3.init()
    engine.say('Что добавим в список дел?')
    engine.runAndWait()

    query = listen_command()

    with open('todo-list.txt', 'a', encoding="utf-8") as myfile:
        myfile.write(f'❗️ {query}\n')

    return f'Задача добавлена'


def shut():
    global n
    n = 0
    return 'До свидания, создатель!'


def main():
    while n != 0:
        query = listen_command()

        for k, v in commands_dict['commands'].items():
            if query in v:
                engine = pyttsx3.init()
                engine.say(globals()[k]())
                engine.runAndWait()


if __name__ == '__main__':
    main()
