from flask import Flask, render_template_string, request
import redis
import json
import os

redis_ip = os.getenv("REDIS_IP")

app = Flask(__name__)
redis_client = redis.Redis(host=redis_ip, port=6379, decode_responses=True)

formulario_html = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <title>Formulário com Flask</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f2f2f2;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
    }

    .container {
      background-color: #fff;
      padding: 30px 40px;
      border-radius: 10px;
      box-shadow: 0 0 15px rgba(0,0,0,0.1);
      width: 100%;
      max-width: 400px;
    }

    h2 {
      text-align: center;
      color: #333;
    }

    label {
      font-weight: bold;
      margin-top: 10px;
      display: block;
    }

    input[type="text"],
    input[type="email"],
    input[type="password"] {
      width: 100%;
      padding: 10px;
      margin-top: 5px;
      border-radius: 5px;
      border: 1px solid #ccc;
      margin-bottom: 15px;
      box-sizing: border-box;
    }

    input[type="submit"] {
      width: 100%;
      background-color: #4CAF50;
      color: white;
      padding: 12px;
      border: none;
      border-radius: 5px;
      font-size: 16px;
      cursor: pointer;
    }

    input[type="submit"]:hover {
      background-color: #45a049;
    }

    .resultado {
      margin-top: 20px;
      background-color: #e7f4e4;
      padding: 15px;
      border-radius: 5px;
      border: 1px solid #c1e1c1;
    }
  </style>
</head>
<body>
  <div class="container">
    <h2>Formulário de Contato</h2>
    <form method="POST">
      <label for="nome">Nome:</label>
      <input type="text" name="nome" id="nome" required>

      <label for="email">E-mail:</label>
      <input type="email" name="email" id="email" required>

      <label for="senha">Senha:</label>
      <input type="password" name="senha" id="senha" required>

      <input type="submit" value="Enviar">
    </form>

    {% if nome and email %}
    <div class="resultado">
      <h3>Dados Recebidos:</h3>
      <p><strong>Nome:</strong> {{ nome }}</p>
      <p><strong>Email:</strong> {{ email }}</p>
    </div>
    {% endif %}
  </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def formulario():
    nome = email = senha = None
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        senha = request.form["senha"]
        user = {"nome": nome,
                "email": email,
                "senha": senha}
        user_json = json.dumps(user)
        redis_client.rpush("users", user_json)
    return render_template_string(formulario_html, nome=nome, email=email, senha=senha)    

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
