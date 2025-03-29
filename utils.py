import re


def save_access_token(token: str, filename: str = "ACCESS_TOKEN.txt"):
    """Сохраняет токен в файл"""
    try:
        with open(filename, 'w') as f:
            f.write(token)
        print(f"Токен успешно сохранён в {filename}")
        return True
    except Exception as e:
        print(f"Ошибка сохранения токена: {e}")
        return False


def read_access_token(filename: str = "ACCESS_TOKEN.txt"):
    """Читает токен из файла"""
    try:
        with open(filename, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        print(f"Файл {filename} не найден")
        return None
    except Exception as e:
        print(f"Ошибка чтения токена: {e}")
        return None

def read_themes(filename: str = "темы статей.txt"):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except FileNotFoundError:
        print(f"Файл {filename} не найден")
        return None
    except Exception as e:
        print(f"Ошибка чтения: {e}")
        return None

def write_article(text: str, filename: str):
    try:
        filename = filename + '.md'
        with open(filename, 'w') as f:
            f.write(text)
        print(f"Текст успешно сохранён в {filename}")
        return True
    except Exception as e:
        print(f"Ошибка сохранения текста: {e}")
        return False