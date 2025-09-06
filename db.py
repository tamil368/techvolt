import pymysql
import cgi
import cgitb

cgitb.enable()


conn = pymysql.connect(host="localhost", user="root", password="", database="smart_car_system")
cur = conn.cursor()

form = cgi.FieldStorage()
name = form.getvalue("name", "").strip()
email = form.getvalue("email", "").strip()
phone = form.getvalue("phone", "").strip()
password = form.getvalue("password", "").strip()
user_type = form.getvalue("user_type", "").strip()

try:

    query = '''INSERT INTO users (name, email, phone, password, user_type)
               VALUES (%s, %s, %s, %s, %s)'''
    cur.execute(query, (name, email, phone, password, user_type))
    conn.commit()
    print("Content-type: text/html\n")
    print('<script>alert("Registration successful!"); window.location.href="index.html";</script>')
except pymysql.MySQLError as e:
    print("Content-type: text/html\n")
    print(f'<script>alert("Error: {e}"); window.location.href="signup.py";</script>')
finally:
    if conn:
        conn.close()
