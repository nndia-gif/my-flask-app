from flask import Flask, render_template_string
import os

app = Flask(__name__)
latest_message = "Belum ada pesan"  # <- pastikan ada di sini

@app.route("/")
def index():
    global latest_message  # pakai global
    html = f"""
    <html>
      <head><title>Telegram → MQTT → Web</title></head>
      <body style="font-family:sans-serif;text-align:center;margin-top:50px;">
        <h2>Pesan terbaru dari Telegram:</h2>
        <h1 style="color:green;">{latest_message}</h1>
      </body>
    </html>
    """
    return render_template_string(html)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)  # jangan pakai debug=True di Railway
