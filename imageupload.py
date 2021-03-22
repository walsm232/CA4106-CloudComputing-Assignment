import boto3

s3 = boto3.resource('s3')

def upload_images():
    try:
        s3.meta.client.upload_file('C:/Users/Michael/Desktop/ca4016-ca/image1.jpg', 'ca4016-image-upload-bucket', 'image1.jpeg')
        s3.meta.client.upload_file('C:/Users/Michael/Desktop/ca4016-ca/image2.jpg', 'ca4016-image-upload-bucket', 'image2.jpeg')
        s3.meta.client.upload_file('C:/Users/Michael/Desktop/ca4016-ca/image3.jpg', 'ca4016-image-upload-bucket', 'image3.jpeg')
        s3.meta.client.upload_file('C:/Users/Michael/Desktop/ca4016-ca/image4.png', 'ca4016-image-upload-bucket', 'image4.png')
        s3.meta.client.upload_file('C:/Users/Michael/Desktop/ca4016-ca/image5.jpg', 'ca4016-image-upload-bucket', 'image5.jpeg')
        print ("Images have uploaded successfully")
        return True
    except FileNotFoundError:
        print ("These images were not found")
        return False

upload_images()
