from flask import Flask
from flask_cors import CORS
from routes import routes  # Importa todas las rutas definidas en routes.py

app = Flask(__name__)

# ✅ Permitir conexión desde tu frontend (localhost:3000 o 127.0.0.1:3000)
CORS(app, resources={r"/*": {"origins": ["http://localhost:3000", "http://127.0.0.1:3000"]}})

# 🔗 Registrar las rutas API
app.register_blueprint(routes)

# 🚀 Mensaje de bienvenida
@app.route("/")
def home():
    return {"message": "Backend Flask funcionando correctamente 🚀"}

# ▶️ Ejecutar servidor
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
