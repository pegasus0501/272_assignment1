FROM python:3.10-slim

WORKDIR /app

COPY . /app

# Install packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# exposing port 5005
EXPOSE 5005

# Define environment variable
ENV FLASK_APP=world.py

#this command runs world.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0", "--port=5005"]