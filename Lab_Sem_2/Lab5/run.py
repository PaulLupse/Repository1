from flask import Flask, render_template
from app.routes import items
from pathlib import Path

app = Flask(__name__, template_folder=Path(__file__).parent/'app'/'templates', static_folder=Path(__file__).parent/'app'/'static', static_url_path='')

app.add_url_rule('/books', 'get_all_books', items.get_books, methods=['GET']) # returneaza toate cartile
app.add_url_rule('/books/<int:book_id>', 'get_book', items.get_book_by_id, methods=['GET']) # returneaza o singura carte (dupa id)
#app.add_url_rule('/books', 'new_stock', None, methods=['POST']) # inlocuieste baza de date cu noul continut
app.add_url_rule('/books', 'add_book', items.add_book, methods=['POST']) # adauga o carte noua
app.add_url_rule('/books/<int:book_id>', 'uptade_book', items.update_book, methods=['PUT']) # modifica o carte existenta (dupa id)
app.add_url_rule('/books/<int:book_id>', 'delete_book', items.delete_book, methods=['DELETE']) # sterge o carte (dupa id)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

def main():
    app.run()

if __name__ == '__main__':
    main()

