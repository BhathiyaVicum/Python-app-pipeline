from flask import Flask
import os
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return f"""
    <html>
        <head><title>DevOps Pipeline Demo</title></head>
        <body style="font-family: Arial; text-align: center; margin-top: 50px;">
            <h1>🚀 CI/CD Pipeline Success!</h1>
            <h2>Deployed via Jenkins + Terraform + Docker</h2>
            <p>Deployment Time: {datetime.datetime.now()}</p>
            <p>Container ID: {os.popen('hostname').read().strip()}</p>
            <hr>
            <p style="color: green;">✅ Fully automated with GitHub webhooks</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)