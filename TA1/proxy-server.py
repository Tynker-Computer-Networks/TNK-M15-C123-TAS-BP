from flask import Flask, jsonify, Response, request, send_from_directory, render_template, redirect
from flask_cors import CORS
import requests
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

app = Flask(__name__)
# Enable CORS so that we can make cross origin calls from server


# Create target_url variable and set it to login page of a website


@app.route('/', methods=['GET', 'POST'])
def serve_index():
    return render_template('index.html')

# Create a /proxy route

# Define proxy() function

    # Use request.get() to get the login page from target_url and save it in response
    
    # return Response(response.text, status=response.status_code, content_type=response.headers['content-type'])
    
    
if __name__ == '__main__':
    app.run(port=5000)
