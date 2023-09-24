import ast

from flask import Flask, render_template, request, url_for

from src.services import calculate_standard_deviation, visualize

app = Flask(__name__, static_url_path='/static')


@app.route('/', methods=['GET', 'POST'])
def form_view():
    if request.method == 'POST':
        array = request.form['array']
        array = ast.literal_eval(array)
        result = calculate_standard_deviation(array)
        image_name = visualize(array, result)
        image_path = url_for('static', filename=image_name)
        return render_template('result.html', image=image_path)
    return render_template('input.html')


@app.route('/api', methods=["POST"])
def api():
    array = request.json['array']
    array = ast.literal_eval(array)
    return list(calculate_standard_deviation(array))
