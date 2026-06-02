from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import session

import sqlite3
import csv
from flask import Response

from cloudwatch import get_metrics

app = Flask(__name__)

app.secret_key = "cloud_dashboard_secret"


@app.route('/')
def home():
    return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        if username == "admin" and password == "admin123":

            session['user'] = username

            return redirect('/dashboard')

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():

    if 'user' not in session:
        return redirect('/login')

    data = get_metrics()

    cpu = data["cpu"]
    memory = data["memory"]
    disk = data["disk"]
    network = data["network"]

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Store metrics
    cursor.execute("""
        INSERT INTO metrics(cpu,memory,disk,network)
        VALUES(?,?,?,?)
    """, (cpu, memory, disk, network))

    alerts = []
    
    # CPU Alert
    if cpu > 80:
        message = "⚠ CPU Usage Critical"
        alerts.append(message)

        cursor.execute("""
            INSERT INTO alerts(message,severity)
            VALUES(?,?)
        """, (message, "High"))

    # Memory Alert
    if memory > 80:
        message = "⚠ Memory Usage Critical"
        alerts.append(message)

        cursor.execute("""
            INSERT INTO alerts(message,severity)
            VALUES(?,?)
        """, (message, "Medium"))

    # Disk Alert
    if disk > 80:
        message = "⚠ Disk Usage Critical"
        alerts.append(message)

        cursor.execute("""
            INSERT INTO alerts(message,severity)
            VALUES(?,?)
        """, (message, "High"))
    if cpu > 80 or memory > 80 or disk > 80:

        status = "Critical"

    elif cpu > 60:

        status = "Warning"

    else:

        status = "Healthy"
    conn.commit()
    conn.close()

    return render_template(
        'dashboard.html',
        cpu=cpu,
        memory=memory,
        disk=disk,
        network=network,
        alerts=alerts
    )

@app.route('/history')
def history():

    if 'user' not in session:
        return redirect('/login')

    search = request.args.get('search')

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    if search:

        cursor.execute("""
        SELECT * FROM metrics
        WHERE timestamp LIKE ?
        ORDER BY id DESC
        """, ('%' + search + '%',))

    else:

        cursor.execute("""
        SELECT * FROM metrics
        ORDER BY id DESC
        """)

    records = cursor.fetchall()

    conn.close()

    return render_template(
        "history.html",
        records=records
    )

@app.route('/alerts')
def alerts_page():

    if 'user' not in session:
        return redirect('/login')

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM alerts
        ORDER BY id DESC
    """)

    records = cursor.fetchall()

    conn.close()

    return render_template(
        "alerts.html",
        records=records
    )


@app.route('/reports')
def reports():

    if 'user' not in session:
        return redirect('/login')

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("""
        SELECT AVG(cpu),
               AVG(memory),
               AVG(disk),
               AVG(network)
        FROM metrics
    """)

    report = cursor.fetchone()

    conn.close()

    return render_template(
        "reports.html",
        report=report
    )
@app.route('/export_csv')
def export_csv():

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM metrics
    """)

    data = cursor.fetchall()

    conn.close()

    def generate():

        yield "ID,CPU,Memory,Disk,Network,Timestamp\n"

        for row in data:

            yield (
                f"{row[0]},"
                f"{row[1]},"
                f"{row[2]},"
                f"{row[3]},"
                f"{row[4]},"
                f"{row[5]}\n"
            )

    return Response(
        generate(),
        mimetype='text/csv',
        headers={
            "Content-Disposition":
            "attachment; filename=monitoring_report.csv"
        }
    )
@app.route('/delete_metric/<int:id>')
def delete_metric(id):

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM metrics
    WHERE id=?
    """, (id,))

    conn.commit()

    conn.close()

    return redirect('/history')
@app.route('/logout')
def logout():

    session.clear()

    return redirect('/login')


if __name__ == "__main__":

    app.run(debug=True)