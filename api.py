from flask import Flask, request, Response
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origin":"*"}})

@app.route('/procesar', methods=['POST'])
def procesar():
    return Response(status='204')

@app.route('/revisar', methods=['POST'])
def revisar():
    return Response(status='204')

if __name__ == '__main__':
    app.run(debug=True)
