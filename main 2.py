from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def huy():
    return ('<h1>Huyy Api</h1>')

@app.route('/huyapi')
def apicheck():
  link = request.args.get('url')
  if link:
    return jsonify({"link":link})
  else:
    return jsonify({"key":"Not Found"})


    

if __name__ == '__main__':
    app.run(debug=True)