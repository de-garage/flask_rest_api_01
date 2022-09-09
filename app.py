from calendar import month
from optparse import Values
from warnings import catch_warnings
from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/enternew')
def new_student():
    return render_template('student.html')


@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            addr = request.form['addr']
            city = request.form['city']
            pin = request.form['pincode']

            with sql.connect('dbs/database_sqlite.db') as con:
                cursor = con.cursor()
                cursor.execute(
                    "INSERT INTO students (name, addr, city, pincode) VALUES (?,?,?,?)", (nm, addr, city, pin))
                con.commit()
                msg = "Record Successfully added"
        except:
            con.rollback()
            msg = "Insert Failed"
        finally:
            return render_template('result.html', msg=msg)
            con.close()


@app.route('/list')
def list_all_students():
    con = sql.connect('dbs/database_sqlite.db')
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("SELECT * from students")

    rows = cur.fetchall()

    return render_template('allstudents.html', rows=rows)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
