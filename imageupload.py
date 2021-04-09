import boto3
import botocore
import os
import random

from flask import Flask, request, render_template, redirect, url_for, send_from_directory
app = Flask(__name__)

accepted_mimetypes = ["image/jpg", "image/jpeg", "image/png", "image/gif", "image/bmp"]
s3 = boto3.resource('s3')

bucket_name = f"CA4016-Images-Upload-Group-3-{str(random.randint(1000, 9999))}"
# bucket_name = "CA4016-Images-Upload-Group-3-1394"
url = f"https://s3.console.aws.amazon.com/s3/buckets/{bucket_name}?region=eu-west-1&tab=objects"

try:
    # Creates S3 bucket named 'ca4016-image-upload' on 'eu-west-1' region and defines URL to bucket
    s3.meta.client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': 'eu-west-1'})
    url = f"https://s3.console.aws.amazon.com/s3/buckets/{bucket_name}?region=eu-west-1&tab=objects"
    print(f"A bucket named '{bucket_name}' has been created successfully")
except s3.meta.client.exceptions.BucketAlreadyExists:
    print("A bucket with this name already exists")
except s3.meta.client.exceptions.BucketAlreadyOwnedByYou:
    print("You already own this bucket")
except Exception as e:
    print("The bucket could not be created")
    print(e)
    exit()
    
bucket = s3.Bucket(bucket_name)
bucket.Acl().put(ACL='public-read')

@app.route("/", methods=["GET"])
def uploadGet():
    return render_template('index.html')

@app.route("/upload", methods=["POST"])
def upload():
    files = request.files.getlist("file")
    for f in files:
        if f.mimetype in accepted_mimetypes:
            s3.meta.client.put_object(
                Body=f, 
                Bucket=bucket_name, 
                Key=f.filename,
                ContentType=f.mimetype,
                ACL='public-read'
            )
    return url
