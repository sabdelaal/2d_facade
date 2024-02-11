# app.py
from flask import Flask, render_template, request, jsonify
from facade_generator import generate_facade

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    width = float(request.form['width'])
    height = float(request.form['height'])
    glass_type = request.form['glassType']

    window_count = int(request.form.get('windowCount', 1))

    facade_svg, window_positions = generate_facade(width, height, glass_type, window_count)

    return jsonify({'facade_svg': facade_svg, 'window_positions': window_positions})

if __name__ == '__main__':
    app.run(debug=True)
