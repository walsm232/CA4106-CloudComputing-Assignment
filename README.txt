Demo server at
https://upload.soren.dreano.net
The webapp is behind a nginx reverse proxy to provide TLS encryption/https
The command I use to run the server is FLASK_APP=imageupload.py flask run
Then navigate to localhost:5000
You'll have to uncomment the bucket_name line and comment the second one, it is just that I prefer to avoid spawning 3429 buckets when coding

And something that does not work: the bucket is not public... So you have to connect to AWS, so this part does not "work" as intended
