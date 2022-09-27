from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__,"views")

@views.route("/")
def home():
    return render_template("index")

@views.route("/json")
def get_json():
    return jsonify({'name': 'tim', 'coolness': 10})

@views.route("/data")
def get_data():
    data= request.json
    return jsonify(data)

@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.home"))

@views.route('/machinelearningprojects')
def machine_learning_project():
    return render_template('MachineLearning.html')

@views.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@views.route('/featured')
def featured():
    return render_template('featured.html')

@views.route('/svr')
def svr():
    return render_template('svr.html')

@views.route('/spotiboard')
def spotiboard():
    return render_template('spotiboard.html')

@views.route('/btssql')
def btssql():
    return render_template('btssql.html')

@views.route('/about')
def about():
    return render_template('about.html')

@views.route('/contact')
def contact():
    return render_template('contact.html')