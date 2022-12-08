from flask import Flask

app = Flask(__name__)

# создаём декаратор
@app.route('/') # / домашняя старница сайта
def index():
    return 'Привет, это первый простой сайт'


if __name__ == "__main__":  # если файл запускается на прямую, запустить сервер
    app.run()
