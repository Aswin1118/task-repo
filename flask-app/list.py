from flask import Flask, render_template, request

app = Flask(__name__)

items = ["Apples", "Bananas", "Oranges"]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'new_item' in request.form:
            new_item = request.form['new_item']
            items.append(new_item)
        elif 'remove_item' in request.form:
            item_to_remove = request.form['remove_item']
            items.remove(item_to_remove)
    return render_template('index.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)
