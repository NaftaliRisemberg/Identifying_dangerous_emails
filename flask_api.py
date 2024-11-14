from flask import Flask

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test():
     return "hello"

if __name__ == '__main__':
    app.run(debug=True)