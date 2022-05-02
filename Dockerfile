FROM python:3.8
WORKDIR /questions
COPY . /questions
RUN pip3 install -r requirements.txt
ENTRYPOINT ["./docker-entrypoint.sh"]