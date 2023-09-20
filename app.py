from config import app,db

from flask import render_template, request, redirect, url_for

from models import Votos

import os


#rota de votação
@app.route('/')
def ola():
    return render_template('base.html')


# função que mostra o tatal dos votos
def count():
    vt_s = Votos.query.filter_by(voto='sim').count()
    vt_n = Votos.query.filter_by(voto='nao').count()
    return vt_s, vt_n


# função que salva os votos
@app.route('/salvar_voto', methods=['POST'])
def salvar_voto():
    voto = request.form.get('voto')
    
    if voto in ('sim', 'nao'):
        novo_voto = Votos(voto=voto)
        db.session.add(novo_voto)
        db.session.commit()
    
    vt_s, vt_n = count()
    
    return render_template('base.html', vt_s=vt_s, vt_n=vt_n)




if __name__ == '__main__':
    if not os.path.exists('storage.db'):
        db.create_all()
    app.run(debug=True)