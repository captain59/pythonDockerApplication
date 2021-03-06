FROM python:3.7-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
ENV PYTHONPATH "${PYTHONPATH}:/usr/src/app/application"

EXPOSE 80

CMD [ "python", "./restAPI.py" ]