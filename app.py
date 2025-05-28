import eventlet
eventlet.monkey_patch()  # ⚠️ Must be the first import

from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
import sqlite3
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'
socketio = SocketIO(app, async_mode='eventlet')

DATABASE = 'documents.db'

def init_db():
    if not os.path.exists(DATABASE):
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute('''
            CREATE TABLE documents (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE,
                content TEXT
            )
        ''')
        conn.commit()
        conn.close()

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/load_document', methods=['POST'])
def load_document():
    name = request.form['name']
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT content FROM documents WHERE name = ?", (name,))
    result = c.fetchone()
    conn.close()
    if result:
        return jsonify({'content': result[0]})
    else:
        return jsonify({'content': ''})

@app.route('/save_document', methods=['POST'])
def save_document():
    name = request.form['name']
    content = request.form['content']
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO documents (name, content) VALUES (?, ?)", (name, content))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Document saved successfully!'})

@socketio.on('edit')
def handle_edit(data):
    emit('edit', data, broadcast=True, include_self=False)

if __name__ == '__main__':
    socketio.run(app, debug=True, port=5000)
