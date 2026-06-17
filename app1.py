from flask import Flask, request, jsonify, render_template
import sqlite3



app = Flask(__name__)


# Create Database


def init_db():
    conn = sqlite3.connect('complaints.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS complaints (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        description TEXT NOT NULL,
        status TEXT DEFAULT 'Pending'
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL
    )
    ''')

    conn.commit()
    conn.close()

init_db()

# Home Route
@app.route('/')
def home():
    return render_template('index.html')


# Add Complaint
@app.route('/complaints', methods=['POST'])
def add_complaint():
    data = request.json

    conn = sqlite3.connect('complaints.db')
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO complaints(name, category, description) VALUES (?, ?, ?)",
        (data['name'], data['category'], data['description'])
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Complaint Registered Successfully"}), 201

@app.route('/register', methods=['POST'])
def register():

    data = request.json

    conn = sqlite3.connect('complaints.db')
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users(username,email,password) VALUES(?,?,?)",
        (
            data['username'],
            data['email'],
            data['password']
        )
    )

    conn.commit()
    conn.close()

    return jsonify({
        "message": "User Registered Successfully"
    })


# Get All Complaints
@app.route('/complaints', methods=['GET'])
def get_complaints():
    conn = sqlite3.connect('complaints.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM complaints")
    rows = cursor.fetchall()

    conn.close()

    complaints = []

    for row in rows:
        complaints.append({
            "id": row[0],
            "name": row[1],
            "category": row[2],
            "description": row[3],
            "status": row[4]
        })

    return jsonify(complaints)

# Update Status
@app.route('/complaints/<int:id>', methods=['PUT'])
def update_status(id):
    data = request.json

    conn = sqlite3.connect('complaints.db')
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE complaints SET status=? WHERE id=?",
        (data['status'], id)
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Status Updated"})

# Delete Complaint
@app.route('/complaints/<int:id>', methods=['DELETE'])
def delete_complaint(id):
    conn = sqlite3.connect('complaints.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM complaints WHERE id=?", (id,))

    conn.commit()
    conn.close()

    return jsonify({"message": "Complaint Deleted"})
@app.route('/users')
def users():

    conn = sqlite3.connect('complaints.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")

    rows = cursor.fetchall()

    conn.close()

    return jsonify(rows)

@app.route('/login', methods=['POST'])
def login():

    data = request.json

    conn = sqlite3.connect('complaints.db')
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email=? AND password=?",
        (
            data['email'],
            data['password']
        )
    )

    user = cursor.fetchone()

    conn.close()

    if user:
        return jsonify({
            "message": "Login Success"
        })

    return jsonify({
        "message": "Invalid Credentials"
    })








@app.route('/loginpage')
def login_page():
    return render_template('login.html')

@app.route('/registerpage')
def register_page():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
    
