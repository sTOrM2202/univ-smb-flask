from flask import Flask, redirect, url_for, render_template, request, flash, session
import base64

app = Flask(__name__)
app.secret_key = "secret_key"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        with open("logs.txt", "r") as f:
            for line in f:
                line = line.strip()
                decoded = base64.b64decode(line).decode("utf-8")
                if decoded == f"{username}:{password}":
                    session["logged_in"] = True
                    flash("Vous êtes maintenant connecté.")
                    return redirect(url_for("site"))
        flash("Nom d'utilisateur ou mot de passe incorrect.")
    return render_template("auth.html")

@app.route("/")
def site():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("index.html")

@app.route("/alias")
def alias():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("/alias.html")

@app.route("/logout")
def logout():
    session["logged_in"] = False
    session.pop("username", None)
    flash("Vous êtes maintenant déconnecté.")
    return redirect(url_for("login"))

@app.route("/rules_filter")
def rules_filter():
    return render_template("/nat.html")

@app.route("/rules_nat_add ")
def rules_nat_add():
    return render_template("/modify.html")


