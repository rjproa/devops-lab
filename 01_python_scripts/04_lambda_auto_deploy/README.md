# ➕ Lambda Suma de Dos Números

Este proyecto implementa una función AWS Lambda en Python que recibe dos números (`a` y `b`) mediante un evento tipo API Gateway, los suma y retorna el resultado en formato JSON. Incluye pruebas unitarias con `pytest`.

---

## 🚀 ¿Qué hace este Lambda?

La función `handler`:

1. Recibe un evento HTTP con un cuerpo JSON que contiene los campos `a` y `b`.
2. Verifica que ambos sean números (`int` o `float`).
3. Retorna la suma de `a + b` si son válidos.
4. Si hay un error, responde con código `400` y un mensaje descriptivo.

---

## 🧪 Pruebas con Pytest

Este proyecto incluye dos pruebas básicas:

| Prueba                | Descripción                                                  |
|-----------------------|--------------------------------------------------------------|
| `test_handler_ok`     | Verifica que la suma `5 + 3` dé como resultado `8`.          |
| `test_handler_error_tipo` | Verifica que si uno de los valores no es numérico, se retorna un error con mensaje adecuado. |

### ▶️ Ejecutar pruebas

```bash
pip install -r requirements.txt
pytest test_main.py
````

---

## 📦 Archivos

| Archivo            | Descripción                                                       |
| ------------------ | ----------------------------------------------------------------- |
| `main.py`          | Contiene la función principal `handler` que implementa la lógica. |
| `test_main.py`     | Pruebas unitarias usando `pytest`.                                |
| `requirements.txt` | Lista de dependencias (solo `pytest`).                            |

---

## 📌 Ejemplo de entrada (evento API Gateway)

```json
{
  "body": "{\"a\": 10, \"b\": 20}"
}
```

## ✅ Ejemplo de respuesta exitosa

```json
{
  "statusCode": 200,
  "body": "{\"resultado\": 30}"
}
```

## ❌ Ejemplo de error

```json
{
  "statusCode": 400,
  "body": "{\"error\": \"Los valores deben ser numéricos\"}"
}
```

---

## 🛠️ Ideal para practicar

* Funciones Lambda
* Manejo de errores en Python
* Testeo básico con Pytest
* Validación de entradas tipo API Gateway

