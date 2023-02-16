import app
from flask import Flask,render_template, request

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.sqlite3'




@app.route('/base',methods=['GET'])
def test():
    return render_template("base.html")




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
def name(name):
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
