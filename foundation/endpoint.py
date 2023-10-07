from flask import Blueprint, render_template

endpoint = Blueprint(__name__, "endpoint")


@endpoint.route("/")
def home():
    return render_template("index.html", title="Pomodoro Timer")

@endpoint.route("/timer/<time>")
def profile(time):
    return render_template("index.html", time=time)