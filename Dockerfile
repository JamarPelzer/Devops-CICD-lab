# Use the official python image 
FROM python:3.12-slim 

#Set working directory inside container
WORKDIR /app

# Copy your app code into the container 
COPY requirements.txt requirements.txt 
RUN pip install -r requirements.txt 
COPY . .

# run your script when the container starts
CMD ["python", "math_app.py"]