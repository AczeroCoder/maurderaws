from flask import Flask

app = Flask(__name__)

print("dasdsadas")

print("testing")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)