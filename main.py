from flask import Flask, render_template
import json

app = Flask(__name__)

with open('news.json', encoding='utf-8') as file:
    news = json.load(file)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/news_detail/<int:id_new>')
def news_detail1(id_new):
    return render_template('news_detail.html', title=news[id_new - 1]['title'], text=news[id_new - 1]['text'])


@app.route('/category/<string:name_category>')
def categories(name_category):
    return f'Категория {name_category}'


if __name__ == '__main__':
    pass
    app.run(debug=True)
