

# 🐲 Pokeneas - Flask + Docker + AWS S3 + Docker Swarm

Proyecto educativo basado en los **Pokeneas** (Pokémon paisas). Muestra información de Pokeneas, sus imágenes desde AWS S3 y permite desplegar el sistema en un clúster con Docker Swarm.

---

## 🚀 Ejecución local

### 1️⃣ Crear entorno virtual
**Windows:**
```
powershell
python -m venv .venv
.venv\Scripts\activate
````

**Linux/Mac:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3️⃣ Ejecutar la app

```bash
python app.py
```

Abre [http://localhost:8000](http://localhost:8000)

---

## 🐳 Ejecutar con Docker

### 1️⃣ Construir imagen

```bash
docker build -t pokeneas .
```

### 2️⃣ Correr contenedor

```bash
docker run -d -p 8000:8000 pokeneas
```

---

## ☁️ Despliegue con Docker Swarm (AWS)

### 🔹 Paso 1: Crear 4 instancias EC2

* Una será **líder** (`swarm-leader`)
* Tres serán **managers** (`swarm-mgr-1`, `swarm-mgr-2`, `swarm-mgr-3`)
* Abre puertos TCP: `22, 8000, 2377, 7946` y UDP: `7946, 4789`

### 🔹 Paso 2: Instalar Docker en todas

```bash
sudo dnf -y update
sudo dnf -y install docker
sudo systemctl enable --now docker
sudo usermod -aG docker ec2-user
exit
```

(Vuelve a entrar con *Connect* desde AWS)

### 🔹 Paso 3: Iniciar Swarm en el líder

```bash
docker swarm init --advertise-addr $(hostname -I | awk '{print $1}')
docker swarm join-token manager
```

Copia el token que se muestra.

### 🔹 Paso 4: Unir los 3 managers

En cada uno:

```bash
sudo docker swarm join --token <TOKEN_DEL_LIDER> <IP_PRIVADA_DEL_LIDER>:2377
```

### 🔹 Paso 5: Verificar desde el líder

```bash
docker node ls
```

---

## 🧩 Desplegar el servicio

En el **líder**:

```bash
docker service create \
  --name pokeneas \
  --replicas 10 \
  --publish published=8000,target=8000 \
  --env S3_BUCKET=pokeneas-media-maocampog1 \
  --env AWS_REGION=us-east-1 \
  maocampog1/pokeneas:latest
```

Verifica:

```bash
docker service ls
docker service ps pokeneas
```

---

## 🌍 Acceso

En el navegador:
`http://<IP_PUBLICA_DE_CUALQUIER_INSTANCIA>:8000/`

Rutas:

* `/` → Pokenea aleatorio (JSON bonito)
* `/pokenea-random` → Imagen + frase inspiracional
* `/pokeneas` → Lista de todos los Pokeneas


---  

¿Quieres que te lo deje con emojis de color y formato tipo “README profesional de GitHub” (con badges, centrado y color)? Puedo darte esa versión también si es para entregar o subir a DockerHub.
```
