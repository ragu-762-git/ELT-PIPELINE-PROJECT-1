from flask import Flask, render_template, request, redirect
from google.cloud import storage
import os

app = Flask(__name__)

# Configure this environment variable with your GCS bucket name
GCS_BUCKET_NAME = 'sales_data_bkt'

# Initialize a GCS client
client = storage.Client()

# Define the bucket
bucket = client.get_bucket(GCS_BUCKET_NAME)


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    
    file = request.files['file']

    if file.filename == '':
        return 'No selected file', 400

    # Save the file to GCS
    blob = bucket.blob(file.filename)
    blob.upload_from_string(file.read(), content_type=file.content_type)

    return redirect('/')


if __name__ == '__main__':
    # Set the environment variable for your GCS credentials file
    #os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'path/to/your/credentials.json'
    app.run(debug=True)


#C:\Users\RAGU\Desktop\Flask-web-portal\templates\index.html