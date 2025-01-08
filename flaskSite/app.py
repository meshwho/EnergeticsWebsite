from flask import Flask, render_template_string

app = Flask(__name__)

app.static_folder = 'static'

# Функция для чтения HTML-кода из файла
def load_html_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

@app.route('/ua')
def home():
    html_main = load_html_from_file('main_page.html')  # Укажите путь к вашему HTML-файлу
    return render_template_string(html_main)

@app.route('/en')
def home_en():
    html_main = load_html_from_file('main_page_en.html')  # Укажите путь к вашему HTML-файлу
    return render_template_string(html_main)

@app.route('/transformer')
def transformer():
    html_transformer = load_html_from_file('transformer_page.html')  # Укажите путь к вашему HTML-файлу
    return render_template_string(html_transformer)

@app.route('/transformer_en')
def transformer_en():
    html_transformer = load_html_from_file('transformer_page_en.html')  # Укажите путь к вашему HTML-файлу
    return render_template_string(html_transformer)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)