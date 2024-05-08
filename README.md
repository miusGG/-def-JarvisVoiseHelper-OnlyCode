# JarvisVoiseHelper

# Commands
  -ПРИВЕТСТВИЕ: 'джарвис привет', 'джарвис включись'
  -ПОМОЩЬ: "джарвис какие у тебя есть команды", 'джарвис что ты умеешь'
  -СОЗДАТЬ ЗАДАЧУ: 'джарвис добавь задачу', 'джарвис создай задачу', 'джарвис задача'
  -ВЫКЛЮЧИТЬ ПРОГРАММУ: 'джарвис выключись', 'спокойной ночи джарвис'
  -ОТКРЫТЬ ЛИСТ ЗАДАЧ: 'джарвис открой список дел', 'джарвис открой дела', 'джарвис дела'
  -ОЧИСТИТЬ ЛИСТ ЗАДАЧ: 'джарвис очисти список дел', 'джарвис удали дела', 'джарвис я закрыл все дела', 'джарвис удалить дела'
  -ВЫКЛЮЧТЬ КОМПЬЮТЕР: 'джарвис выключи компьютер', 'джарвис выключи комп'

Заготовка для оболочки
```
from tkinter import *
from tkinter import ttk
 
root = Tk()
root.title("JarvisVoiseHelper")
root.geometry("250x200")


def click_button():
    if btn_start["text"] == f"Stop":
        btn_start["text"] = f"Start"
    elif btn_start["text"] == f"Start":
        btn_start["text"] = f"Stop"


def get_text():
    pass


editor = Text
editor.pack(fill=BOTH, expand=1)

btn_start = ttk.Button(text="Stop", command=click_button)
btn_start.pack()
 
root.mainloop()
```

