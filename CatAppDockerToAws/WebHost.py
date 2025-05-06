from flask import Flask, request, jsonify

app = Flask(__name__)

@app.errorhandler(404)
def handle_404(error):
    return error

@app.route('/')
def index():
    return "<p>I'll put version here to see deployment ECR->ECS <mark>0.1.4.</mark></p><br><img src=https://cataas.com/cat>"

if __name__ == '__main__':
    app.run(host='0.0.0.0' ,port=777)