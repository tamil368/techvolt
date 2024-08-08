import cgi
import cgitb
import pymysql

cgitb.enable()

conn = pymysql.connect(host="localhost", user="root", password="", database="smart_car_system")
cur = conn.cursor()


form = cgi.FieldStorage()
username = form.getvalue('username', '').strip()
email = form.getvalue('email', '').strip()
password = form.getvalue('password', '').strip()
user_type = form.getvalue('user_type', '').strip()

try:

    query = '''SELECT * FROM users 
               WHERE name = %s AND email = %s AND password = %s AND user_type = %s'''
    cur.execute(query, (username, email, password, user_type))
    result = cur.fetchone()

    if result:
        if user_type == "admin":
            print(f'<script>alert("AdminLogin successful"); window.location.href="admin_dashboard.py";</script>')
        elif user_type == "buyer":
            print(f'<script>alert("Hai {username} Login successful!"); window.location.href="buyer_dashboard.py";</script>')
        elif user_type == "seller":
            print(f'<script>alert("Hai {username} Login successful!"); window.location.href="seller_dashboard.py";</script>')
    else:
        print('<script>alert("Invalid Credentials."); window.location.href="login.py";</script>')

except pymysql.MySQLError as e:
    print(f'<script>alert("Error: {e}"); window.location.href="login.py";</script>')

finally:

    cur.close()
    conn.close()
