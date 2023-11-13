from flask import Flask
import psycopg2
app = Flask(__name__)


class DatabaseConnection:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="host.docker.internal",
            database="postgres",
            user="postgres",
            password="postgres",
            port=5433
        )

    def close(self):
        self.conn.close()

    def count(self):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT COUNT(*) FROM public.results;")
            result = cur.fetchone()
            return str(result[0])
        finally:    
            cur.close()

    def largest(self):
        try:
            cur = self.conn.cursor()
            cur.execute(
                "SELECT original, factors, saved FROM results ORDER BY original DESC LIMIT 1;"
            )
            result = cur.fetchone()
            return str(result[0]), str(result[1]), str(result[2])
        finally:    
            cur.close()

 
@app.route('/')
def index():
    with open("index.html") as f:
        data = f.read()

    try:
        conn = DatabaseConnection()
        number = conn.count()
        largest_original, largest_factors, largest_saved = conn.largest()
        data = data.replace("NUMBER", number)
        data = data.replace("LARGEST", f"{largest_original} = {largest_factors}")
        data = data.replace('TIMESTAMP', largest_saved)
        return data
    except:
        return "Webserver is running but cannot connect to database."
 
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)