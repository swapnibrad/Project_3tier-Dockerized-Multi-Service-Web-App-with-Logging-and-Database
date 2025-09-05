from flask import Flask, request
import mysql.connector, os

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST", "db"),
        user=os.environ.get("DB_USER", "user"),
        password=os.environ.get("DB_PASSWORD", "userpass"),
        database=os.environ.get("DB_NAME", "mydb")
    )

@app.route("/")
def index():
    client_ip = request.headers.get("X-Real-IP", request.remote_addr)
    user_agent = request.headers.get("X-User-Agent", "Unknown")

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO access_logs (client_ip, user_agent) VALUES (%s, %s)",
            (client_ip, user_agent)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return f"✅ Logged access from {client_ip} with UA: {user_agent}"
    except Exception as e:
        return f"❌ DB error: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
