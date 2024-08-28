# ELT-PIPELINE-PROJECT-1
This project involves creating a web based portal and allowing the clients to upload files from three different regions to the web portal. Extracting the data from the Web Portal to the GCS bucket and once the file hits the GCS bucket, the event arc trigger invokes the cloud function which initiates the dataflow job (GCS to BigQuery). 

# STEP -1 
Create a web portal for the clients to upload the CSV files to the GCS bucket by using the Python **FLASK** framework. This flask framework will create a web interface for uploading the files to GCS bucket. 
Note: Use the command - (gcloud auth application-default login) to get authentication from the GCP console to upload files while running the local host created by the Python flask.
Note: Always keep the 'index.html' inside the templates folder. path - flask-for-we-portal/templates/index.html ; The file **app.py** hosts the web interface while rendering the HTML file for making the UI.

# Step -2 
Set up the cloud function in GCP. The function directly writes the data to BQ by creating a table; if table already exists, the data will get appended to the table. 

# Step -3
Run SQL and derive the revenue generated by each country and visualize it in Looker
