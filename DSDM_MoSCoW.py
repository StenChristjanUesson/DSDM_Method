from flask import Flask, render_template_string

app = Flask(__name__)

base_template = """
<!DOCTYPE html>
<html>
<head>
    <title>TTHK</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: sans-serif; margin: 0; padding: 0; background: #f4f4f4; }
        header { background: #003366; color: white; padding: 1em; text-align: center; }
        nav { background: #0055a5; padding: 1em; text-align: center; }
        nav a { color: white; margin: 0 1em; text-decoration: none; }
        main { padding: 2em; }
        footer { background: #003366; color: white; text-align: center; padding: 1em; margin-top: 2em; }
    </style>
</head>
<body>
    <header><h1>TTHK Kooli Koduleht</h1></header>
    <nav>
        <a href="/">Avaleht</a>
        <a href="/erialad">Erialad</a>
        <a href="/uudised">Uudised</a>
        <a href="/kontakt">Kontakt</a>
    </nav>
    <main>{{ content|safe }}</main>
    <footer>&copy; 2025 TTHK</footer>
</body>
</html>
"""

@app.route("/")
def home():
    content = "<h2>Tere tulemast TTHK kodulehele</h2><p>Siit leiad info kooli ja õppimisvõimaluste kohta.</p>"
    return render_template_string(base_template, content=content)

@app.route("/kontakt")
def kontakt():
    content = "<h2>Kontakt</h2><p>Email: info@tthk.ee<br>Telefon: +372 600 1234<br>Aadress: Pärnu mnt 57, Tallinn</p>"
    return render_template_string(base_template, content=content)

@app.route("/erialad")
def erialad():
    content = "<h2>Erialad</h2><ul><li>IT-süsteemide spetsialist</li><li>Autotehnik</li><li>Elektrik</li><li>Kokk</li></ul>"
    return render_template_string(base_template, content=content)

@app.route("/uudised")
def uudised():
    content = "<h2>Uudised</h2><ul><li>04.05.2025 - Vastuvõtt on alanud</li><li>27.05.2025 - Koolilõpuaktus</li><li>01.09.2025 - Uue õppeaasta algus</li></ul>"
    return render_template_string(base_template, content=content)

if __name__ == "__main__":
    app.run(debug=True)
