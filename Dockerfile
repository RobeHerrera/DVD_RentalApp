# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.9

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# create root directory for our project in the container
RUN mkdir /DVD_RentalApp

# Set the working directory to /DVD_RentalApp
WORKDIR /DVD_RentalApp

# Copy the current directory contents into the container at /DVD_RentalApp
ADD . /DVD_RentalApp/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# port where the Django app runs  
EXPOSE 8000  
# start server  
# CMD python DVD_RentalApp/manage.py runserver  
