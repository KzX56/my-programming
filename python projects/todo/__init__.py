import json
import os
from xml.etree.ElementTree import indent
import customtkinter as ctk
from tkinter import IntVar

DB_FILE = "todo_db.json"

def load_tasks():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks():
    with open(DB_FILE, "w") as file:
        json.dump(todo, file, indent=4)

todo = load_tasks()


def strikethrough(text):
    return ''.join(char + '\u0336' for char in text)

def is_struckthrough(text):
    return '\u0336' in text

def remove_strikethrough(text):
    return text.replace('\u0336', '')

def add(new_todo):
    todo.append(str(new_todo))
    save_tasks()

def delete(delete):
    try:
        delete = int(delete)
        todo.pop(delete - 1)
    except ValueError:
        pass
    except IndexError:
        print("[!] please enter a valid number")

def check(check):
    try:
        check -= 1
        if is_struckthrough(todo[check]):
            todo[check] = remove_strikethrough(todo[check])
        else:
            todo[check] = strikethrough(todo[check])
        save_tasks()
    except IndexError:
        print("[!] please enter a valid number")

def main():
    for number,task in enumerate(todo , start=1):
        print(f"{number} - {task}")
    options()
    save_tasks()

def close():
    print("closing...")
    exit()


def options():
    print("""
    1-add      2-delete     3-check     4-close
    """)
    selector = int(input("select : "))
    match selector:

        case 1:
            var = input("write the task you want to add : ")
            add(var)
        case 2:
                var = input("write the task number you want to Delete : ")
                delete(var)
        case 3:
                var = int(input("write the task you want to check : "))
                check(var)

        case 4:
            close()


