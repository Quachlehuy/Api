from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def huy():
    return '<h1>Huyy Api</h1>'

@app.route('/api')
def apicheck():
  link = request.args.get('link')
  if link:
    return ({"link":link})
  else:
    return ({"key":"Loi Roi"})
    

if __name__ == '__main__':
    app.run(debug=True)