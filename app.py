import os
from flask import Flask, jsonify, request, render_template, redirect, url_for
from dotenv import load_dotenv
import logging

load_dotenv()
app = Flask(__name__)
app.logger.setLevel(logging.INFO)

@app.route("/health", methods=["GET"])
def health():
    app.logger.info("Status:100, Entered Health Route")
    app.logger.info("Health check called")
    return jsonify({"status": "ok"}), 200

@app.route("/login", methods=["GET", "POST"])
def login():
    app.logger.info("Status:101, Entered Dashboard")
    if request.method == "GET":
        return render_template('login_page.html')
    elif request.method == "POST":
        email = request.form.get("email","").strip()
        password = request.form.get("password","").strip()
        app.logger.info(email)
        app.logger.info(password)
        if email == "user@email.com" and password == "password":
            app.logger.info("Status:200, Login Successful redirecting to dashboard")
            return redirect(url_for("dashboard"))
        else:
            app.logger.warning("Status:401, Login Failed")
            return render_template("login_page.html", error="Invalid credentials")
        
@app.route("/dashboard")
def dashboard():
    app.logger.info("Status:102, Entered Dashboard")
    return render_template("dashboard_page.html")

if __name__ == '__main__':
    app.run(debug=True, port=5010)

