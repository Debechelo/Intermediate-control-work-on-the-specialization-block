import json
import os
from datetime import datetime

class Note:
    def __init__(self, note_id, title, body, timestamp):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.timestamp = timestamp

class NotesApp:
    def __init__(self, notes_file="notes.json"):
        self.notes_file = notes_file
        self.notes = []
        self.load_notes()

    def load_notes(self):
        if os.path.exists(self.notes_file):
            with open(self.notes_file, 'r') as file:
                data = json.load(file)
                self.notes = [Note(item['id'], item['title'], item['body'], item['timestamp']) for item in data]

    def save_notes(self):
        with open(self.notes_file, 'w') as file:
            json.dump(self.notes, file, default=lambda o: o.__dict__, indent=4)

    def create_note(self, title, body):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if self.notes:
            new_id = max(note.note_id for note in self.notes) + 1
        else:
            new_id = 1
        new_note = Note(new_id, title, body, timestamp)
        self.notes.append(new_note)
        self.save_notes()
        print("Note created successfully.")

    def read_notes(self):
        if not self.notes:
            print("No notes available.")
        else:
            for note in self.notes:
                print(f"ID: {note.note_id}\nTitle: {note.title}\nBody: {note.body}\nTimestamp: {note.timestamp}\n")

    def edit_note(self, note_id, new_title, new_body):
        for note in self.notes:
            if note.note_id == note_id:
                note.title = new_title
                note.body = new_body
                note.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_notes()
                print("Note edited successfully.")
                return
        print("Note not found.")

    def delete_note(self, note_id):
        for note in self.notes:
            if note.note_id == note_id:
                self.notes.remove(note)
                # Reassign IDs
                for index, note in enumerate(self.notes):
                    note.id = index + 1
                self.save_notes()
                print("Note deleted successfully.")
                return
        print("Note not found.")

if __name__ == "__main__":
    app = NotesApp()

    while True:
        print("\nВведите команду:")
        print("add - Добавить заметку")
        print("read - Показать заметки")
        print("edit - Редактировать заметку")
        print("delete - Удалить заметку")
        print("exit - Выйти из программы\n")
        
        command = input("Введите команду: ")

        if command == 'add':
            title = input("Введите заголовок заметки: ")
            body = input("Введите тело заметки: ")
            app.create_note(title, body)
        elif command == 'read':
            app.read_notes()
        elif command == 'edit':
            note_id = int(input("Введите ID заметки для редактирования: "))
            new_title = input("Введите новый заголовок: ")
            new_body = input("Введите новое тело: ")
            app.edit_note(note_id, new_title, new_body)
        elif command == 'delete':
            note_id = int(input("Введите ID заметки для удаления: "))
            app.delete_note(note_id)
        elif command == 'exit':
            print("Выход из программы...")
            break
        else:
            print("Неверная команда. Пожалуйста, попробуйте снова.")