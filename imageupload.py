import boto3
import webbrowser
import os
import random

s3 = boto3.resource('s3')

# Will provide the path of the desktop on any Operating System
desktop = os.path.normpath(os.path.expanduser("~/Desktop"))

# Comprehension list to create the list ['image1.jpg', 'image2.jpg', 'image3.jpg', 'image4.jpg', 'image5.jpg']
file_names = [f"image{i}.jpg" for i in range(1, 6)]

def upload_images():
    # Bucket name are public and shared among all AWS users
    bucket = f"ca4016-images-upload-group-3-{str(random.randint(1000, 9999))}"
    try:
        # Creates S3 bucket named 'ca4016-image-upload' on 'eu-west-1' region and defines URL to bucket
        s3.meta.client.create_bucket(Bucket=bucket, CreateBucketConfiguration={'LocationConstraint': 'eu-west-1'})
        url = f"https://s3.console.aws.amazon.com/s3/buckets/{bucket}?region=eu-west-1&tab=objects"
        print(f"A bucket named '{bucket}' has been created successfully")
    except s3.meta.client.exceptions.BucketAlreadyExists:
        print("A bucket with this name already exists")
    except Exception as e:
        print("The bucket could not be created")
        print(e)
    else:
        for file_name in file_names:
            try:
                # Windows uses '\' while Unix derivatives use '/' in paths. The use of os.path.join makes the code multiplatform
                file_path = os.path.join(desktop, file_name)
                print(file_path)
                s3.meta.client.upload_file(file_path, bucket, file_name)
                print(f"'{file_name}' has uploaded successfully")
            except FileNotFoundError as e:
                print(f"'{file_name}' failed to upload")
                print(e)

        webbrowser.open(url, new=0)

upload_images()