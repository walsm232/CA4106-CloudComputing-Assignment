import unittest
from imageupload import uploadGet ,upload

class testClass(unittest.TestCase):
    # Test for the correct bucket naming convention
    def Test_Bucket_Name():
        assert.bucket_name == "CA4016-Images-Upload-Group-3-1394"

    # Test to ensure that the correct URL has been assigned to the bucket
    def Test_Bucket_URL():
        assert.url == "https://s3.console.aws.amazon.com/s3/buckets/1394?region=eu-west-1&tab=objects"
    
    # Test to ensure that the number of images uploaded to the VPS is equal to 5
    def Test_Number_of_Files():
        assert.files = 5

    # Test to ensure that the mimetype of the images is in our list of accepted mimetypes
    def Test_File_Types():
        assert.f.mimetype in accepted_mimetypes

    # Test to ensure that the URL to the bucket is returned correctly and opens in a new tab
    def Test_URL_Returned():
        assert.return url = True