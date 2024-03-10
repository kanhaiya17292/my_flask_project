from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/calculate_gc_content', methods=['POST'])
def calculate_gc_content():
    sequence = request.form['sequence']
    gc_content = calculate_gc(sequence)
    return render_template('result.html', gc_content=gc_content)

def calculate_gc(sequence):
    gc_count = sequence.count('G') + sequence.count('C')
    total_bases = len(sequence)
    gc_content = (gc_count / total_bases) * 100
    return gc_content

if __name__ == '__main__':
    app.run(debug=True)
