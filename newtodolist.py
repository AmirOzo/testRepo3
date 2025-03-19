# Простой To-Do List на Python

tasks = []  # Список для хранения задач.

def show_tasks():
    """Функция для отображения всех задач."""
    if not tasks:
        print("Список задач пуст.")
    else:
        print("Ваши задачи:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task():
    """Функция добавления новой задачи."""
    task = input("Введите новую задачу: ")
    tasks.append(task)
    print(f"Задача '{task}' добавлена.")

def delete_task():
    """Функция для удаления задачи."""
    show_tasks()
    try:
        task_number = int(input("Введите номер задачи для удаления: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Задача '{removed_task}' удалена.")
        else:
            print("Неверный номер задачи.")
    except ValueError:
        print("Ошибка: введите число.")

def main():
    """Основная функция для управления программой."""
    while True:
        print("\n--- To-Do List ---")
        print("1. Показать задачи")
        print("2. Добавить задачу")
        print("3. Удалить задачу")
        print("4. Выйти")
        choice = input("Выберите действие (1-4): ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()