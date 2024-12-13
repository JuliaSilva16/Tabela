from flask import *
from sqlalchemy import *

from models import *

app = Flask(__name__)
app.secret_key = 'chave_secreta'

@app.route('/')
def redirecionar():
    return redirect(url_for('base'))

@app.route('/base')
def base():
    busca = db_session.query(Pessoa)
    db_session.close()
    return render_template('Exercicio_3.html', resultado=busca)

if __name__ == '__main__':
    app.run(debug=True)

