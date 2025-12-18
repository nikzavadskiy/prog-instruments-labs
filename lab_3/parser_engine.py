import re

CAR_PATTERN = re.compile(
    r'<h2 class="title">(?P<name>.*?)</h2>.*?'  
    r'<span class="price">(?P<price>.*?) €</span>.*?' 
    r'<span class="year">(?P<year>\d{4})</span>.*?' 
    r'<span class="mileage">(?P<mileage>.*?) км</span>.*?'  
    r'<span class="gearbox">(?P<gear>.*?)</span>',
    re.DOTALL
)


def parse_html(html_text):
    """Извлекает данные из созданного нами HTML."""
    matches = CAR_PATTERN.finditer(html_text)
    data_list = []

    for m in matches:
        data_list.append({
            "Name": m.group("name").strip(),
            "Price": m.group("price").replace('.', '').strip(),
            "Year": m.group("year").strip(),
            "Mileage": m.group("mileage").replace('.', '').strip(),
            "Transmission": m.group("gear").strip()
        })
    return data_list