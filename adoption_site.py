import os
from forms import  AddForm , DelForm, AddOwnerForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import pandas as pd
import sqlalchemy as sq


app = Flask(__name__)
# Key for Forms
app.config['SECRET_KEY'] = 'mysecretkey'

############################################

        # SQL DATABASE AND MODELS

##########################################
basedir = os.path.abspath(os.path.dirname(__file__))
#OLD SQLite DB
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
#NEW SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:SQL5Data@localhost/puppies'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

class Puppy(db.Model):

    __tablename__ = 'puppies'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    color_fur = db.Column(db.Text)
    owner = db.relationship('Owner',backref='puppy',uselist=False)

    def __init__(self,name, color_fur):
        self.name = name
        self.color_fur = color_fur


    def __repr__(self):
        if self.owner:
            return f"Puppy name: {self.name}, Fur color: {self.color_fur}, Owner: {self.owner.name}"
        else:
            return f"Puppy name: {self.name}, Fur color: {self.color_fur}, Owner: none"

class Owner(db.Model):

    __tablename__ = 'owners'

    id = db.Column(db.Integer,primary_key= True)
    name = db.Column(db.Text)
    # We use puppies.id because __tablename__='puppies'
    puppy_id = db.Column(db.Integer,db.ForeignKey('puppies.id'))

    def __init__(self,name,puppy_id):
        self.name = name
        self.puppy_id = puppy_id

    def __repr__(self):
        return f"Owner Name: {self.name}"
############################################

        # VIEWS WITH FORMS

##########################################
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_pup():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        color_fur = form.color_fur.data
        # Add new Puppy to database
        new_pup = Puppy(name, color_fur)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('list_pup'))

    return render_template('add.html',form=form)
@app.route('/add_owner', methods=['GET', 'POST'])
def add_owner():

    form = AddOwnerForm()

    if form.validate_on_submit():
        name = form.name.data
        pup_id = form.pup_id.data
        # Add new owner to database
        new_owner = Owner(name,pup_id)
        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for('list_pup'))

    return render_template('add_owner.html',form=form)

@app.route('/list')
def list_pup():
    con = sq.create_engine('mysql+pymysql://root:SQL5Data@localhost/puppies')
    df_owner = pd.read_sql('owners', con)
    print(df_owner)

    # read only
    df_puppies = pd.read_sql('puppies', con)
    print(df_puppies)

    df_fur_group = df_puppies.groupby('color_fur')
    print('---Group by color---')
    print(df_fur_group.size())
    total_row_puppies = df_puppies.shape[0]
    total_row_owner = df_owner.shape[0]
    print('Total count for puppies table: ' + str(total_row_puppies))
    print('Total count for owners table: ' + str(total_row_owner))
    print('Total number of column in puppies table: ' + str(df_puppies.shape[1]))
    print('Total number of column in owners table: ' + str(df_owner.shape[1]))



    # Grab a list of puppies from database.
    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies, total_row_puppies=total_row_puppies, total_row_owner=total_row_owner, puppies_column=df_puppies.shape[1], owner_column=df_owner.shape[1], group_by_fur=df_fur_group.size())

@app.route('/delete', methods=['GET', 'POST'])
def del_pup():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('list_pup'))
    return render_template('delete.html',form=form)


if __name__ == '__main__':
    app.run(debug=True)
