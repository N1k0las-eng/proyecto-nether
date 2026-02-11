from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Proyecto Nether</title>
        <style>
            body {
                background-color: black;
                color: white;
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 30px;
                transition: 0.5s;
            }

            h1 {
                color: #00ff00;
            }

            h2 {
                color: #00ff00;
                margin-top: 40px;
            }

            button {
                background-color: #00ff00;
                color: black;
                padding: 15px 25px;
                border: none;
                font-size: 18px;
                cursor: pointer;
                margin-top: 40px;
            }

            button:hover {
                background-color: #00cc00;
            }

            .gamer-mode {
                background-color: #0f0f0f;
                color: #00ff00;
            }

            .historia {
                max-width: 800px;
                margin: auto;
                text-align: left;
                line-height: 1.6;
            }

            ul {
                text-align: left;
                display: inline-block;
            }
        </style>
    </head>
    <body>

        <h1>🔥 Proyecto Nether 🔥</h1>

        <div class="historia">

        <h2>🧱 Mi Historia – Proyecto Nether</h2>

        <p>
        Hola, soy Nicolás Gabriel Fierro Ortega.<br><br>

        Bienvenido a la primera versión oficial de Proyecto Nether.
        No sé cuántas veces actualizaré esta página, pero esta es la versión 1, donde todo comenzó.<br><br>

        Esta página incluye:<br>
        - Mi historia<br>
        - Tips Pro de Minecraft<br>
        - Zona Secreta Gamer<br><br>

        Me gustan los videojuegos, programar y dominar Minecraft como un verdadero pro.
        Y esta es mi primera página web creada con Python.
        </p>

        <h2>🌍 Cómo empezó todo</h2>

        <p>
        Hace 6 años creé mi primer mundo en Minecraft junto a mi papá.
        Durante los primeros 2 o 3 años jugábamos juntos, explorando, sobreviviendo y construyendo nuestras propias aventuras.<br><br>

        Después me pasé a celular y estuve aproximadamente 2 años jugando ahí.
        Mi hermana me descargaba Minecraft en versión APK (seguramente ese celular terminó con 500 virus 😅).<br><br>

        Pero desde el primer año que jugué Minecraft, tenía un objetivo claro:
        algún día jugaría en PC.
        </p>

        <h2>💻 El cambio a PC</h2>

        <p>
        Empecé a ahorrar poco a poco.
        En el último año logré comprar una computadora HP.<br><br>

        Más adelante, mi hermana me la intercambió por otra que tenía más espacio.
        Y ahí todo cambió.<br><br>

        Los juegos corrían mejor.
        Se sentía más rápido.
        Más fluido.
        Más pro.<br><br>

        Y este último año me pasé definitivamente a PC.
        </p>

        <h2>⚔️ Presente</h2>

        <p>
        Actualmente juego en launcher porque no tengo la versión premium,
        pero eso no me detuvo.<br><br>

        Un clan increíble me recibió con respeto y buena onda,
        y estos últimos días le he estado metiendo todo el empeño.<br><br>

        Gracias Atherion.<br>
        Gracias Just_Glep.<br><br>

        Y gracias a mi tío, que me enseñó Python y me ayudó a empezar en el mundo de la programación.<br><br>

        Proyecto Nether no es solo una página web.
        Es el inicio de mi camino como programador y gamer.<br><br>

        Y esto recién empieza.
        </p>

        </div>

        <h2>🎮 Tips Pro de Minecraft</h2>

        <ul>
            <li>Usa escudo en PvP para bloquear ataques críticos.</li>
            <li>Siempre lleva cubeta de agua para evitar daño por caída.</li>
            <li>Aprende el timing del hacha en combate.</li>
            <li>Usa perlas de ender para escapar.</li>
            <li>Encanta tu armadura con Protección IV.</li>
            <li>Consigue encantamientos fuertes con aldeanos.</li>
            <li>Haz granjas automáticas para subir más rápido.</li>
            <li>Practica PvP constantemente.</li>
        </ul>

        <br>

        <button onclick="activarModoGamer()">😈 Botón Secreto Gamer</button>

        <h3 style="margin-top:20px;">Próximamente...</h3>

        <script>
            function activarModoGamer() {
                document.body.classList.toggle("gamer-mode");
                alert("🔥 MODO PRO ACTIVADO 🔥");
            }
        </script>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
