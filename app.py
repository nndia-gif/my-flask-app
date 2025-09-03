from flask import Flask
import os

app = Flask(__name__)
latest_message = "Belum ada pesan"

@app.route("/")
def index():
    global latest_message
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
    #except Exception as e:
        #return f"Error: {e}"

    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    # penting: jangan pakai debug=True
    app.run(host="0.0.0.0", port=port)
