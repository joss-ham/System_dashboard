from flask import Flask, render_template, jsonify
import psutil

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/stats')
def stats():
    # Fetching real-time system metrics
    data = {
        'cpu_usage': psutil.cpu_percent(interval=None),
        'ram_usage': psutil.virtual_memory().percent,
        'disk_usage': psutil.disk_usage('/').percent
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)