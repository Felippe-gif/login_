from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def conectar_db():
    return sqlite3.connect("banco.db")

@app.route("/", methods=["GET", "POST"])
def login():
    erro = None  

    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]

        conn = conectar_db()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM usuarios
            WHERE email = ? AND senha = ?
        """, (email, senha))

        usuario = cursor.fetchone()
        conn.close()

        if usuario:
            return "Login realizado com sucesso!"
        else:
            erro = "Email ou senha inválidos"  

    return render_template("index.html", erro=erro)  

if __name__ == "__main__":
    app.run(debug=True)
