import csv


def export_to_csv(data, filename):
    """Записывает данные в CSV файл."""
    if not data:
        return False

    headers = ["Name", "Price", "Year", "Mileage", "Transmission"]
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
        return True
    except Exception as e:
        print(f"Ошибка при сохранении: {e}")
        return False