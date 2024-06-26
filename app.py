from flask import Flask , redirect
app = Flask(__name__)
@app.route('/file/<id>')
def file_id(id=None):
  url = f'http://127.0.0.1:7890/stream/{id}'
  return redirect(url)
@app.route('/connect/<db>/<username>')
def connect(db=None,username=None):
  url = f'http://127.0.0.1:7890/connect/{db}/{username}'
  return redirect(url)
if __name__=='__main__':
  app.run('0.0.0.0',port=443)
