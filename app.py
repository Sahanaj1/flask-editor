import app
from flask import Flask,render_template, requests,flash
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditor
from flask_ckeditor import CKEditorField
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from wtforms.widgets import TextArea

app=Flask(__name__)
ckeditor = CKEditor(app)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///users.db'
app.config['SECRET_KEY']='SahanaIsTheKey'


db=SQLAlchemy(app)

class Posts(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(200), nullable=False)
    content=db.Column(db.Text)
    # content = CKEditorField('Body')
    author=db.Column(db.String(120))
    date_posted=db.Column(db.DateTime, default=datetime.utcnow)
    slug=db.Column(db.String(250))

class PostForm(FlaskForm):
    title=StringField(' title',validators=[DataRequired()])
    # content=StringField(' content',validators=[DataRequired()],widget=TextArea())
    content = CKEditorField('Body',validators=[DataRequired()])
    author=StringField(' author',validators=[DataRequired()])
    slug=StringField(' slug',validators=[DataRequired()])
    submit=SubmitField('submit')


@app.route('/add-post',methods=['GET','POST'])
def add_post():
    form=PostForm()
    if form.validate_on_submit():
        content=form.content.data
        post=Posts(title=form.title.data,content=form.content.data,author=form.author.data,slug=form.slug.data)
        form.title.data=''
        form.content.data=''
        form.author.data=''
        form.slug.data=''
        flash("post submitted sucessfully")
        print(content)
    return render_template('add_post.html',form=form,content=content)

# @app.route('/add-post', methods=['GET', 'POST'])
# def add_post():
#     form = PostForm()
#     if form.validate_on_submit():
#         post_data = {
#             'title': form.title.data,
#             'content': form.content.data,
#             'author': form.author.data,
#             'slug': form.slug.data
#         }
#         response = requests.post('https://demo1338405.mockable.io/posttest', json=post_data)
#         if response.status_code == 200:
#             form.title.data = ''
#             form.content.data = ''
#             form.author.data = ''
#             form.slug.data = ''
#             flash('Post submitted successfully')
           
#         else:
#             flash('Post submission failed')
#     return render_template('add_post.html', form=form)

@app.route('/posted-data',methods=['POST'])
def 

class Users(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(200), nullable=False)
    email=db.Column(db.String(120), nullable=False,unique=True)
    date_added=db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return '<Name %r>' % self.name


class UserForm(FlaskForm):
    name=StringField(' name',validators=[DataRequired()])
    email=StringField('email',validators=[DataRequired()])
    submit=SubmitField('submit')

class NameForm(FlaskForm):
    name=StringField('what is your name?',validators=[DataRequired()])
    submit=SubmitField('submit')

@app.route('/base',methods=['GET'])
def test():
    return render_template("base.html")

@app.route('/name',methods=['GET','POST'])
def name():
    name=None
    form=NameForm()
    if form.validate_on_submit():
        name=form.name.data
        form.name.data=''
        flash("form submitted successfully")
    return render_template('name.html',
    name=name,
    form=form)


@app.route('/bootstrap',methods=['GET'])
def bootstrap():
    return render_template("bootstrap.html")


@app.route('/editor',methods=['GET'])
def editor():
    return render_template("editor.html")

@app.route('/',methods=['GET'])
def root():
    return "hello world"


@app.route('/myroute', methods=['POST'])
def my_route():
    my_param = request.form['my_param']
    # do something with my_param
    print(my_param)
    return my_param


# @app.route('/user/<name>')
# def name(name):
#     return '<h1>Hello {}</h1>'.format(name)

@app.route('/user/<name>')
def user(name):
    stuff='this is <strong>bold</strong> text'
    fav_pizza=['veg pizza','cheese','normal',41]
    return render_template('user.html',username=name,stuff=stuff,fav_pizza=fav_pizza)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'),500




if  __name__=='__main__':
    app.run(debug=True)
