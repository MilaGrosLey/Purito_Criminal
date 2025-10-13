from flask import Blueprint, jsonify, request

routes = Blueprint('routes', __name__)

# ===========================
#   RUTAS DE DATASETS
# ===========================

datasets = [
    {
        "id": 1,
        "nombre": "Dataset de prueba",
        "usuario_id": "123",
        "archivo_url": "https://ejemplo.com/archivo.csv",
        "filas": 120,
        "columnas": 5,
        "creado_en": "2025-10-12T10:00:00Z"
    }
]


@routes.route('/api/datasets', methods=['GET'])
def obtener_datasets():
    return jsonify(datasets)


@routes.route('/api/datasets', methods=['POST'])
def crear_dataset():
    data = request.get_json()
    nuevo = {
        "id": len(datasets) + 1,
        "nombre": data.get("nombre", "Sin nombre"),
        "usuario_id": data.get("usuario_id", "0"),
        "archivo_url": data.get("archivo_url", ""),
        "filas": 200,
        "columnas": 10,
        "creado_en": "2025-10-12T12:00:00Z"
    }
    datasets.append(nuevo)
    return jsonify(nuevo), 201


@routes.route('/api/datasets/<int:id>', methods=['DELETE'])
def eliminar_dataset(id):
    global datasets
    datasets = [d for d in datasets if d["id"] != id]
    return jsonify({"message": "Dataset eliminado correctamente"}), 200


# ===========================
#   RUTAS DE EXPERIMENTOS
# ===========================

@routes.route('/api/experimentos', methods=['GET'])
def obtener_experimentos():
    return jsonify([
        {"id": 1, "nombre": "Experimento A", "precision": 0.89},
        {"id": 2, "nombre": "Experimento B", "precision": 0.92}
    ])




@routes.route('/api/experimentos/<id>', methods=['GET'])
def obtener_experimento(id):
    # Si el ID es 'undefined' o algo no numérico, devolvemos un mensaje claro
    if id == "undefined" or not id.isdigit():
        return jsonify({"error": "ID de experimento no válido"}), 400

    id = int(id)
    experimento = next((e for e in [
        {"id": 1, "nombre": "Experimento A", "precision": 0.89},
        {"id": 2, "nombre": "Experimento B", "precision": 0.92}
    ] if e["id"] == id), None)

    if experimento:
        return jsonify(experimento)
    return jsonify({"error": "Experimento no encontrado"}), 404



@routes.route('/api/experimentos/recientes', methods=['GET'])
def obtener_experimentos_recientes():
    return jsonify([
        {"id": 1, "nombre": "Experimento reciente", "fecha": "2025-10-12"}
    ])

# ===========================
#   RUTA PARA COLUMNAS DEL DATASET
# ===========================

@routes.route('/api/datasets/<int:id>/columnas', methods=['GET'])
def obtener_columnas_dataset(id):
    dataset = next((d for d in datasets if d["id"] == id), None)
    if not dataset:
        return jsonify({"error": "Dataset no encontrado"}), 404

    # Simulación de columnas del dataset
    columnas = [
        {"nombre": "edad", "tipo": "numérico"},
        {"nombre": "ingresos", "tipo": "numérico"},
        {"nombre": "genero", "tipo": "categoría"},
        {"nombre": "pais", "tipo": "categoría"}
    ]
    return jsonify(columnas)

# ===========================
#   RUTA DE ESTADÍSTICAS
# ===========================

@routes.route('/api/estadisticas', methods=['GET'])
def obtener_estadisticas():
    return jsonify({
        "total_datasets": len(datasets),
        "total_experimentos": 2,
        "usuarios_activos": 5
    })

# ===========================
#   RUTA PARA INICIAR ENTRENAMIENTO
# ===========================

@routes.route('/api/entrenamiento', methods=['POST'])
def iniciar_entrenamiento():
    data = request.get_json()

    # Datos que el frontend podría enviar:
    dataset_id = data.get("dataset_id")
    modelo = data.get("modelo", "Regresión logística")

    # Simulación de un entrenamiento exitoso
    resultado = {
        "mensaje": "Entrenamiento completado correctamente ✅",
        "dataset_id": dataset_id,
        "modelo": modelo,
        "precision": 0.91,
        "recall": 0.88,
        "f1_score": 0.89,
        "tiempo": "15 segundos"
    }

    return jsonify(resultado), 200

# ===========================
#   RUTAS FALTANTES (MOCKS)
# ===========================

@routes.route('/api/datasets/<int:id>/vista-previa', methods=['GET'])
def vista_previa_dataset(id):
    """Simula devolver las primeras filas del dataset"""
    vista_previa = [
        {"edad": 25, "ingresos": 2500, "genero": "M", "pais": "Perú"},
        {"edad": 30, "ingresos": 3200, "genero": "F", "pais": "Chile"},
        {"edad": 28, "ingresos": 2900, "genero": "M", "pais": "México"}
    ]
    return jsonify(vista_previa)


@routes.route('/api/datasets/<int:id>/distribucion-clases', methods=['GET'])
def distribucion_clases(id):
    """Simula la distribución de clases del dataset"""
    clases = [
        {"clase": "Aprobado", "cantidad": 60},
        {"clase": "Reprobado", "cantidad": 40}
    ]
    return jsonify(clases)


@routes.route('/api/datasets/<int:id>/correlacion', methods=['GET'])
def correlacion_dataset(id):
    """Simula una matriz de correlación"""
    correlacion = {
        "edad": {"ingresos": 0.75, "genero": 0.12, "pais": 0.05},
        "ingresos": {"edad": 0.75, "genero": 0.10, "pais": 0.07}
    }
    return jsonify(correlacion)


@routes.route('/api/datasets/<int:id>/limpiar', methods=['POST'])
def limpiar_dataset(id):
    """Simula la limpieza del dataset"""
    return jsonify({"mensaje": f"Dataset {id} limpiado exitosamente ✅"}), 200


# ⚠️ CORREGIR NOMBRE DE RUTA DE ENTRENAMIENTO (el front usa /api/entrenamientos)
@routes.route('/api/entrenamientos', methods=['POST'])
def iniciar_entrenamiento_plural():
    data = request.get_json()
    dataset_id = data.get("dataset_id")
    modelo = data.get("modelo", "Regresión logística")

    resultado = {
        "mensaje": "Entrenamiento completado correctamente ✅",
        "dataset_id": dataset_id,
        "modelo": modelo,
        "precision": 0.91,
        "recall": 0.88,
        "f1_score": 0.89,
        "tiempo": "15 segundos"
    }
    return jsonify(resultado), 200