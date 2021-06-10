FROM python:3.9.5-slim

WORKDIR /app

#Copy all files from current folder to the folder on Container
COPY . .
# install dependencies
RUN pip install -r requirements.txt

# command to run on container start
CMD [ "python", "./app.py" ]
