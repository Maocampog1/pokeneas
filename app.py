from flask import Flask, jsonify, render_template_string
import random, socket
from data import POKENEAS, s3_url

app = Flask(__name__)

def container_id():
    return socket.gethostname()

# Ruta 1: JSON con id, nombre, altura, habilidad + id del contenedor
@app.get("/api/pokenea")
def api_pokenea():
    p = random.choice(POKENEAS)
    return jsonify({
        "id": p["id"],
        "nombre": p["nombre"],
        "altura": p["altura"],
        "habilidad": p["habilidad"],
        "container_id": container_id()
    }), 200

# Ruta 2: Página con imagen (desde S3) + frase + id del contenedor
@app.get("/inspiracion")
def inspiracion():
    p = random.choice(POKENEAS)
    img_url = s3_url(p["imagen"])

    html = f"""
    <html>
      <head>
        <meta charset="utf-8">
        <title>Pokeneas</title>
        <style>
          body {{ font-family: Arial, sans-serif; display: grid; place-items: center; padding: 24px; }}
          .card {{ max-width: 520px; border: 1px solid #ddd; border-radius: 16px; padding: 24px; }}
          img {{ max-width: 100%; border-radius: 12px; }}
          .meta {{ margin-top: 12px; color: #555; font-size: 0.9rem }}
        </style>
      </head>
      <body>
        <div class="card">
          <h1>{p["nombre"]}</h1>
          <img src="{img_url}" alt="{p["nombre"]}">
          <p style="margin-top: 12px;"><em>“{p["frase"]}”</em></p>
          <p class="meta">Contenedor: {container_id()}</p>
        </div>
      </body>
    </html>
    """
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
