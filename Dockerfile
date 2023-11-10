# Inherit python image
FROM registry.access.redhat.com/ubi8/python-39:latest

# Set up directories

WORKDIR /application

# Copy python dependencies and install these
COPY example.py /application
COPY app.py /application
COPY templates/* /application/templates/
COPY requirements.txt /application
RUN pip3 install -r requirements.txt


# Environment variables
ENV PYTHONUNBUFFERED 1

# EXPOSE port 8000 to allow communication to/from server
EXPOSE 8001
STOPSIGNAL SIGINT

ENTRYPOINT ["python"]
CMD ["flask_app.py"]
