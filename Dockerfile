FROM python:3.8-slim-buster
WORKDIR /app
RUN pip3 install flask boto3
COPY . .
EXPOSE 5000
#COPY ./credentials ~/.aws/credentials
ENV FLASK_APP=imageupload.py
ENV AWS_ACCESS_KEY_ID=
ENV AWS_SECRET_ACCESS_KEY=
CMD [ "flask", "run", "--host", "0.0.0.0"]
