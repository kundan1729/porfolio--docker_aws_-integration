from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>KD Portfolio</title>
        <style>
            body {
                font-family: 'Segoe UI', sans-serif;
                background-color: #f2f2f2;
                margin: 0;
                padding: 40px;
            }
            h1 {
                text-align: center;
                color: #333;
            }
            .container {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                gap: 20px;
                margin-top: 40px;
            }
            .card {
                background: white;
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
                padding: 20px;
                width: 300px;
                transition: transform 0.2s ease;
            }
            .card:hover {
                transform: scale(1.03);
            }
            .card h2 {
                margin-top: 0;
                color: #007acc;
            }
            ul {
                padding-left: 20px;
            }
            a {
                color: #007acc;
                text-decoration: none;
            }
        </style>
    </head>
    <body>
        <h1>👨‍💻 KD's Portfolio</h1>
        <div class="container">
            <div class="card">
                <h2>About Me</h2>
                <p>I’m a Computer Science Engineering student interested in full-stack development, DevOps, and cloud technologies.</p>
            </div>
            <div class="card">
                <h2>Projects</h2>
                <ul>
                    <li>Flask Blog App</li>
                    <li>MERN Stack E-commerce Site</li>
                    <li>DevOps CI/CD with Jenkins & Docker</li>
                </ul>
            </div>
            <div class="card">
                <h2>Contact</h2>
                <p>Email: <a href="mailto:kundan234432@gmail.com">kundan234432@gmail.com</a></p>
                <p>LinkedIn: <a href="https://linkedin.com/in/kundan1729" target="_blank">linkedin.com/in/kundan1729</a></p>
            </div>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
