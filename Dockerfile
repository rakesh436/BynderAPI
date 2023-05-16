FROM python:3.8-slim

COPY . /BynderAPI
WORKDIR /BynderAPI
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt
RUN ["pytest", "-v", "--junitxml=reports/result.xml"]
CMD tail -f /dev/null