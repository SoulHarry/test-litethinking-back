FROM python:3

# Set unbuffered output for python
ENV PYTHONUNBUFFERED 1

# Create app directory
RUN mkdir /app
WORKDIR /app

# Install app dependencies
ADD requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD . /app/

# Bundle app source
COPY start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start