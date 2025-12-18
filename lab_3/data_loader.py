def load_html(file_path):
    """Считывает содержимое HTML-файла."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Критическая ошибка: Файл '{file_path}' не найден.")
        return None