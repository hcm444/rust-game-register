from flask import Flask, render_template, request, flash, redirect, url_for
import socket
import json

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this to a secure secret key in production

# TCP client setup
TCP_IP = 'localhost'
TCP_PORT = 4520

def send_to_elixir_server(data):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((TCP_IP, TCP_PORT))
            json_data = json.dumps(data)
            s.sendall(json_data.encode())
            response = s.recv(1024).decode()
            return json.loads(response)
    except Exception as e:
        return {"error": str(e)}

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_data = {
            'username': request.form.get('username'),
            'email': request.form.get('email'),
            'password': request.form.get('password')
        }
        
        # Validate input
        if not all(user_data.values()):
            flash('All fields are required!', 'error')
            return redirect(url_for('register'))
        
        # Send data to Elixir server
        response = send_to_elixir_server(user_data)
        
        if 'error' in response:
            flash(f'Registration failed: {response["error"]}', 'error')
        else:
            flash('Registration successful!', 'success')
            
        return redirect(url_for('register'))
    
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
