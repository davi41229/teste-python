from config import app

from flask import render_template

#rota de votação
@app.route('/')
def ola():
    return render_template('base.html')


# função que salva os votos

# função que mostra o tatal dos votos

"""
if __name__ == '__main__':
    app.run(debug=True)
"""



if __name__ == '__main__':
    if not os.path.exists('storage.db'):
        db.create_all()
    app.run(debug=True)