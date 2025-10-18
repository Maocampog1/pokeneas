# Configuración mínima para S3 público (SIN credenciales; el bucket tendrá acceso público)
import os

S3_BUCKET = os.getenv("S3_BUCKET", "tu-bucket-pokeneas")  # cámbialo o pásalo por env
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")         # cámbialo o pásalo por env

def s3_url(key: str) -> str:
    # URL pública estándar de S3 (requiere que el bucket/objeto sea público)
    return f"https://{S3_BUCKET}.s3.{AWS_REGION}.amazonaws.com/{key}"

# 7–10 Pokeneas quemados (SIN BD)
POKENEAS = [
    {
        "id": 1,
        "nombre": "Mazamorrchu",
        "altura": 1.1,
        "habilidad": "Dulce Resistencia",
        "imagen": "imagenes/mazamorrchu.png",
        "frase": "Con mazamorra y buena charla se arregla el mundo, mijito."
    },
    {
        "id": 2,
        "nombre": "Chicharronix",
        "altura": 1.6,
        "habilidad": "Crocrunch",
        "imagen": "imagenes/chicharronix.png",
        "frase": "El que no arriesga el diente, no prueba chicharrón."
    },
    {
        "id": 3,
        "nombre": "Arepachu",
        "altura": 1.4,
        "habilidad": "Escudo de Maíz",
        "imagen": "imagenes/arepachu.png",
        "frase": "Una arepa al día mantiene la tristeza en la lejanía."
    },
    {
        "id": 4,
        "nombre": "Montañerix",
        "altura": 1.8,
        "habilidad": "Pulmón de Altura",
        "imagen": "imagenes/montanerix.png",
        "frase": "Donde otros se cansan, el montañero apenas empieza."
    },
    {
        "id": 5,
        "nombre": "PaisaChu",
        "altura": 1.3,
        "habilidad": "Voltaje Antioqueño",
        "imagen": "imagenes/paisachu.png",
        "frase": "No se rinda, mijito, que el voltaje paisa nunca se apaga."
    },
    {
        "id": 6,
        "nombre": "Frijolmon",
        "altura": 1.5,
        "habilidad": "Energía Bandejera",
        "imagen": "imagenes/frijolmon.png",
        "frase": "Con fríjoles y guiso se gana cualquier batalla."
    },
    {
        "id": 7,
        "nombre": "Mijitomon",
        "altura": 0.9,
        "habilidad": "Cariño Instantáneo",
        "imagen": "imagenes/mijitomon.png",
        "frase": "Todo suena mejor si le dicen ‘mijito’ primero."
    },
    {
        "id": 8,
        "nombre": "Aguardemon",
        "altura": 1.7,
        "habilidad": "Brillo Valiente",
        "imagen": "imagenes/aguardemon.png",
        "frase": "Un traguito aclara la voz… o la conciencia, según el caso."
    }
]

