from flask import FlaskApp
app = new Flask(__name__)
@app.route('/file/<id>')
def file_id(id=None):
  url = 'http://127.0.0.1:7890/chunks/FzNJiyFDKwp3'
  return "<body style='margin:0;padding:0;'><video style='max-width: 100%;max-height: 100%;background:black;min-width: 100%;min-height: 100%;' controls autoplay><source src='"+url+"'/></video></body>",200
if __name__=='__main__':
  app.run('0.0.0.0',port=443)
