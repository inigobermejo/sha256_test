# basic python3 image as base
FROM python:3.7

# install dependencies of the algorithm
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# copy all local files to the image
COPY . /

# execute algorithm in the container
CMD ["python", "./main.py"]