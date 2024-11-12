from flask import Flask
from datetime import datetime
import os
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "kaliraj"
    
    username = os.getenv("USER") or os.getenv("USERNAME") or "Unknown User"
    
    ist_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    top_output = subprocess.getoutput("top -b -n 1")
    
    response = f"""
    <html>
        <body>
            <h1>System Information</h1>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Username:</strong> {username}</p>
            <p><strong>Server Time (IST):</strong> {ist_time}</p>
            <pre>{top_output}</pre>
        </body>
    </html>
    """
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
