from data_loader import load_html
from parser_engine import parse_html
from data_exporter import export_to_csv


def main():
    print("--- Запуск парсера: Легенды Германии и Японии ---")

    raw_html = load_html('page.html')
    if not raw_html:
        print("Файл page.html не найден!")
        return

    cars = parse_html(raw_html)

    if cars:
        print(f"Успех! Найдено машин: {len(cars)}")
        for car in cars:
            print(f" -> {car['Name']} ({car['Year']})")

        export_to_csv(cars, 'results.csv')
        print("\nДанные сохранены в 'results.csv'")
    else:
        print("Ошибка: Регулярное выражение ничего не нашло. Проверьте parser_engine.py")


if __name__ == "__main__":
    main()