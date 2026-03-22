from flask import Flask, render_template, jsonify
import psutil as ps

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/stats')
def stats():
    # Fetching real-time system metrics
    data = {
        'cpu_usage': ps.cpu_percent(interval=0.2),
        'ram_usage': ps.virtual_memory().percent,
        'disk_usage': ps.disk_usage('/').percent
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)