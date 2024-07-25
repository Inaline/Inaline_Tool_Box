# app.py
from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - Inaline Tool Box</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f0f0f0;
        }

        .login-form {
            background-color: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            width: 300px;
        }

        label {
            display: block;
            margin-bottom: 5px;
        }

        input[type="text"],
        input[type="password"] {
            width: calc(100% - 20px);
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 3px;
        }

        button {
            width: 100%;
            padding: 10px;
            background-color: #007BFF;
            color: white;
            border: none;
            border-radius: 3px;
            cursor: pointer;
        }

        button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="login-form">
        <h2>Login - Inaline Tool Box</h2>
        <form id="loginForm">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required>
            
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>
            
            <button type="submit">Login</button>
        </form>
        <p id="message"></p>
    </div>

    <script>
        document.getElementById('loginForm').addEventListener('submit', function(event) {
            event.preventDefault(); // 阻止表单默认提交行为

            var username = document.getElementById('username').value;
            var password = document.getElementById('password').value;

            if (username === 'admin' && password === '123456') {
                document.getElementById('message').textContent = '登录成功!';
                document.getElementById('message').style.color = 'green';
            } else {
                document.getElementById('message').textContent = '登录失败，请检查用户名和密码!';
                document.getElementById('message').style.color = 'red';
            }
        });
    </script>
</body>
</html>"""

if __name__ == '__main__':
    app.run()