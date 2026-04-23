from flask import Flask, render_template, jsonify
import random, time

app = Flask(__name__)

def generate_data():
    return {
        "patient_id": random.randint(1000, 1010),
        "heart_rate": random.randint(60, 140),
        "temperature": round(random.uniform(36, 40), 2),
        "oxygen": random.randint(85, 100),
        "timestamp": time.strftime("%H:%M:%S")
    }

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("index.html")

@app.route("/data")
def data():
    d = generate_data()

    if d["heart_rate"] > 120 or d["temperature"] > 38 or d["oxygen"] < 90:
        d["alert"] = "CRITICAL"
    else:
        d["alert"] = "NORMAL"

    if d["heart_rate"] > 110:
        d["prediction"] = "HIGH RISK"
    else:
        d["prediction"] = "LOW RISK"

    return jsonify(d)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
