from flask import render_template, request, url_for, redirect
from config import db
from app import app
from modelos.asignatura import Asignatura


@app.route('/')
def index():
    asignatura = Asignatura.query.all()
    print(asignatura)
    return render_template('index.html', asignatura=asignatura)


@app.route('/<int:asignaturas_id>/')
def asignaturas(asignaturas_id):
    asignaturas = Asignatura.query.get_or_404(asignaturas_id)
    return render_template('asignatura.html', asignaturas=asignaturas)


@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        # id = request.form['id']
        nomProfesor = request.form['nomProfesor']
        asignatura = request.form['asignatura']
        img = request.form['img']
        nueva_asignatura = Asignatura(nomProfesor, asignatura, img)

        db.session.add(nueva_asignatura)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('create.html')


@app.route('/<int:asignaturas_id>/edit/', methods=('GET', 'POST'))
def edit(asignaturas_id):
    asignatura = Asignatura.query.get_or_404(asignaturas_id)

    if request.method == 'POST':
        id = request.form['id']
        nomProfesor = request.form['profesor']
        asignatura = request.form['asignatura']

        asignatura.id = id
        asignatura.profesor = nomProfesor
        asignatura.asignatura = asignatura

        db.session.add(asignatura)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('edit.html', asignatura=asignatura)


@app.post('/<int:asignaturas_id>/delete/')
def delete(asignaturas_id):
    asignatura = Asignatura.query.get_or_404(asignaturas_id)

    db.session.delete(asignatura)
    db.session.commit()
    return redirect(url_for('index'))
