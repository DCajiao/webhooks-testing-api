# 🚀 Webhook Tester API 🌐

¡Bienvenido a **Webhook Tester API**! 🎉 Este proyecto es una API simple para probar tus webhooks, registrar las solicitudes y manejarlas fácilmente. ¡Perfecto para asegurarte de que todo está funcionando a la perfección antes de ponerlo en producción! 🛠️

## 💡 ¿Qué hace esta API?
Esta API tiene 3 endpoints:
1. **/post** – Recibe solicitudes `POST` y guarda los datos en un archivo de logs.
2. **/get** – Devuelve todo el contenido registrado en los logs.
3. **/delete** – Limpia todos los logs, ¡como si nada hubiera pasado! ✨

## 📂 Estructura de archivos
```
├── logs/                # Carpeta para almacenar los logs
│   └── data.txt         # Archivo donde se registran los datos
├── main.py              # Código de la API
├── Dockerfile           # Archivo Docker para correr la API
├── requirements.txt     # Dependencias del proyecto
└── README.md            # Este increíble archivo
```

## 🚀 Cómo usar la API

### 1. Clonar el repositorio:
Primero, clona el repo para tener todo listo en tu máquina.
```bash
git clone https://github.com/tu-repositorio/webhook-tester-api.git
cd webhook-tester-api
```

### 2. Instalar dependencias:
Asegúrate de tener Flask instalado. Si no lo tienes, puedes instalarlo con:
```bash
pip install -r requirements.txt
```

### 3. Ejecutar la API:
Arranca el servidor Flask con el siguiente comando:
```bash
python main.py
```
Ahora tu API debería estar corriendo en `http://localhost:5000` 🎉

### 4. Usar Docker 🐳 (¡la forma cool de correr tu API!)
Si prefieres usar Docker (y claro que sí), sigue estos pasos:

#### 1. Crear la imagen de Docker:
```bash
docker build -t webhook-tester-api .
```

#### 2. Correr la API en un contenedor:
```bash
docker run -d -p 5000:5000 webhook-tester-api
```

¡Y voilà! 🎉 Tu API está lista en `http://localhost:5000`.

### 5. Prueba los endpoints:
#### **Enviar datos a `/post`** 📨
Haz una solicitud `POST` a `/post` con un JSON para guardar datos en los logs.
```bash
curl -X POST http://localhost:5000/post -H "Content-Type: application/json" -d '{"mensaje": "¡Hola, webhook!"}'
```

#### **Consultar los logs en `/get`** 📜
Accede a todos los datos registrados con una solicitud `GET`.
```bash
curl http://localhost:5000/get
```

#### **Eliminar los logs con `/delete`** 🗑️
Limpia todos los registros con una solicitud `DELETE`.
```bash
curl -X DELETE http://localhost:5000/delete
```

## 📝 Notas:
- Todos los datos se almacenan en el archivo `logs/data.txt` en formato de texto plano.
- Los logs se guardan con un timestamp 🕒, así que siempre sabrás cuándo recibiste una solicitud.
- ¡Recuerda no exponer esta API en producción sin seguridad! 🚨

## 🤖 ¿Qué sigue?
- Implementar autenticación básica 🔒 para que solo tú puedas acceder a los logs.
- Integrar una base de datos para guardar los datos de manera más robusta.
- ¡O lo que se te ocurra! 🎨

---

¡Disfruta probando tus webhooks con Docker o sin Docker! 🐳🌈

