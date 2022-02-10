FROM python:3.8

COPY espresso ./espresso
COPY requirements.txt ./
COPY certs ./certs

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "./espresso/manage.py", "runserver", "0.0.0.0:8080"]
#CMD ["/bin/bash"]