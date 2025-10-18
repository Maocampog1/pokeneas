from flask import Flask, jsonify, render_template_string
import random, socket
from data import POKENEAS, s3_url

app = Flask(__name__)

def container_id():
    return socket.gethostname()

# --- 1. Página principal con tres cards y botones amarillos ---
@app.get("/")
def home():
    html = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>Pokeneas</title>
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
      <style>
        body {{
          background: linear-gradient(135deg, #fffbe6, #fef9c3);
          font-family: 'Poppins', sans-serif;
        }}
        .card {{
          border: none;
          border-radius: 16px;
          box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
          transition: transform 0.2s ease;
        }}
        .card:hover {{
          transform: scale(1.03);
        }}
        .btn-warning {{
          background-color: #facc15;
          border: none;
          font-weight: 600;
          color: #333;
        }}
        .btn-warning:hover {{
          background-color: #fbbf24;
        }}
        h1 {{
          text-align: center;
          margin-top: 30px;
          margin-bottom: 40px;
          color: #333;
          font-weight: 700;
        }}
        footer {{
          text-align: center;
          margin-top: 40px;
          padding: 10px;
          color: #777;
        }}
      </style>
    </head>
    <body>
      <div class="container">
        <h1>Centro de Pokeneas</h1>
        <div class="row justify-content-center g-4">

          <!-- Card 1: Pokenea aleatorio (JSON) -->
          <div class="col-md-4">
            <div class="card h-100 text-center">
              <img src="https://pokeneas-media-maocampog1.s3.us-east-1.amazonaws.com/imagenes/mazamorrchu.png" class="card-img-top" alt="Pokenea JSON">
              <div class="card-body d-flex flex-column">
                <h5 class="card-title">Pokenea Aleatorio</h5>
                <p class="card-text flex-grow-1">Muestra un Pokenea en formato JSON con su id, nombre, altura y habilidad.</p>
                <a href="/api/pokenea" class="btn btn-warning mt-auto">Ver JSON</a>
              </div>
            </div>
          </div>

          <!-- Card 2: Inspiración -->
          <div class="col-md-4">
            <div class="card h-100 text-center">
              <img src="https://pokeneas-media-maocampog1.s3.us-east-1.amazonaws.com/imagenes/mijitomon.png" class="card-img-top" alt="Inspiración Pokenea">
              <div class="card-body d-flex flex-column">
                <h5 class="card-title">Pokenea Inspirador</h5>
                <p class="card-text flex-grow-1">Descubre una frase y una imagen inspiradora de un Pokenea aleatorio.</p>
                <a href="/pokenea-random" class="btn btn-warning mt-auto">Ver Inspiración</a>
              </div>
            </div>
          </div>

          <!-- Card 3: Catálogo -->
          <div class="col-md-4">
            <div class="card h-100 text-center">
              <img src="https://pokeneas-media-maocampog1.s3.us-east-1.amazonaws.com/imagenes/paisachu.png" class="card-img-top" alt="Catálogo Pokeneas">
              <div class="card-body d-flex flex-column">
                <h5 class="card-title">Pokeneas Existentes</h5>
                <p class="card-text flex-grow-1">Explora todos los Pokeneas creados con sus habilidades y características.</p>
                <a href="/pokeneas" class="btn btn-warning mt-auto">Ver Todos</a>
              </div>
            </div>
          </div>

        </div>
        <footer>Contenedor: {container_id()}</footer>
      </div>
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """
    return render_template_string(html)


# --- 2. Ruta inspiradora ---
@app.get("/pokenea-random")
def inspiracion():
    p = random.choice(POKENEAS)
    img_url = s3_url(p["imagen"])

    html = f"""
    <html>
      <head>
        <meta charset="utf-8">
        <title>Pokenea Inspirador</title>
        <style>
          body {{ font-family: Arial; display: grid; place-items: center; padding: 24px; background: #fffde7; }}
          .card {{ max-width: 520px; background: white; border-radius: 16px; padding: 24px; box-shadow: 0 4px 12px rgba(0,0,0,0.2); }}
          img {{ max-width: 100%; border-radius: 12px; }}
          .meta {{ margin-top: 12px; color: #555; font-size: 0.9rem; }}
          a {{ color: #facc15; font-weight: bold; text-decoration: none; }}
        </style>
      </head>
      <body>
        <div class="card">
          <h1>{p["nombre"]}</h1>
          <img src="{img_url}" alt="{p["nombre"]}">
          <p style="margin-top: 12px;"><em>“{p["frase"]}”</em></p>
          <p class="meta">Contenedor: {container_id()}</p>
          <a href="/">← Volver</a>
        </div>
      </body>
    </html>
    """
    return render_template_string(html)


# --- 3. Catálogo ---
@app.get("/pokeneas")
def todos_pokeneas():
    html_cards = ""
    for p in POKENEAS:
        img_url = s3_url(p["imagen"])
        html_cards += f"""
        <div class="poke-card">
          <img src="{img_url}" alt="{p["nombre"]}">
          <h3>{p["nombre"]}</h3>
          <p><strong>Altura:</strong> {p["altura"]} m</p>
          <p><strong>Habilidad:</strong> {p["habilidad"]}</p>
        </div>
        """

    html = f"""
    <html>
      <head>
        <meta charset="utf-8">
        <title>Pokeneas Existentes</title>
        <style>
          body {{ font-family: Arial; padding: 20px; background: #fffde7; }}
          h1 {{ text-align: center; color: #333; }}
          .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; }}
          .poke-card {{ background: white; border-radius: 12px; padding: 16px; text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }}
          img {{ max-width: 100%; border-radius: 8px; }}
          a {{ display: block; text-align: center; margin-top: 20px; color: #facc15; text-decoration: none; font-weight: bold; }}
        </style>
      </head>
      <body>
        <h1>Pokeneas Existentes</h1>
        <div class="grid">
          {html_cards}
        </div>
        <a href="/">← Volver</a>
      </body>
    </html>
    """
    return render_template_string(html)


# --- 4. JSON en una carta bonita ---
@app.get("/api/pokenea")
def api_pokenea():
    p = random.choice(POKENEAS)
    html = f"""
    <html>
      <head>
        <meta charset="utf-8">
        <title>Pokenea JSON</title>
        <style>
          body {{ font-family: 'Poppins', sans-serif; background: #fffde7; display: flex; justify-content: center; align-items: center; height: 100vh; }}
          .card {{ background: white; border-radius: 16px; padding: 24px; max-width: 420px; box-shadow: 0 4px 12px rgba(0,0,0,0.15); text-align: center; }}
          pre {{ background: #fef3c7; border-radius: 8px; padding: 12px; text-align: left; }}
          a {{ color: #facc15; font-weight: bold; text-decoration: none; }}
        </style>
      </head>
      <body>
        <div class="card">
          <h2>Pokenea Aleatorio (JSON)</h2>
          <pre>{{
  "id": {p["id"]},
  "nombre": "{p["nombre"]}",
  "altura": {p["altura"]},
  "habilidad": "{p["habilidad"]}",
  "container_id": "{container_id()}"
}}</pre>
          <a href="/">← Volver</a>
        </div>
      </body>
    </html>
    """
    return render_template_string(html)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
