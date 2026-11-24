from flask import Flask, render_template, request

app = Flask(__name__)


def calcular_promedio(nota1: float, nota2: float, nota3: float) -> float:
    return round((nota1 + nota2 + nota3) / 3, 2)


def evaluar_aprobacion(promedio: float, asistencia: float) -> str:
    if promedio >= 40 and asistencia >= 75:
        return "Aprobado"
    return "Reprobado"


def buscar_nombre_mas_largo(nombres: list[str]) -> tuple[str, int]:
    mayor = nombres[0]
    for nombre in nombres[1:]:
        if len(nombre) > len(mayor):
            mayor = nombre
    return mayor, len(mayor)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    promedio = None
    estado = None
    error = None

    if request.method == "POST":
        try:
            nota1 = float(request.form["nota1"])
            nota2 = float(request.form["nota2"])
            nota3 = float(request.form["nota3"])
            asistencia = float(request.form["asistencia"])

            if not (10 <= nota1 <= 70 and 10 <= nota2 <= 70 and 10 <= nota3 <= 70):
                error = "Cada nota debe estar entre 10 y 70."
            elif not (0 <= asistencia <= 100):
                error = "La asistencia debe estar entre 0 y 100."
            else:
                promedio = calcular_promedio(nota1, nota2, nota3)
                estado = evaluar_aprobacion(promedio, asistencia)
        except ValueError:
            error = "Ingresa números válidos en todos los campos."

    return render_template(
        "ejercicio1.html",
        promedio=promedio,
        estado=estado,
        error=error,
    )


@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    nombre_mayor = None
    cantidad_caracteres = None
    error = None

    if request.method == "POST":
        n1 = request.form["nombre1"].strip()
        n2 = request.form["nombre2"].strip()
        n3 = request.form["nombre3"].strip()

        if not n1 or not n2 or not n3:
            error = "Debes ingresar los tres nombres."
        elif len({n1.lower(), n2.lower(), n3.lower()}) < 3:
            error = "Los tres nombres deben ser diferentes."
        else:
            nombre_mayor, cantidad_caracteres = buscar_nombre_mas_largo([n1, n2, n3])

    return render_template(
        "ejercicio2.html",
        nombre_mayor=nombre_mayor,
        cantidad_caracteres=cantidad_caracteres,
        error=error,
    )


if __name__ == "__main__":
    app.run(debug=True)