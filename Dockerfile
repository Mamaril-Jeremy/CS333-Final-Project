FROM python:3.10

WORKDIR /CS333-Final-Project

COPY . /CS333-Final-Project

RUN pip install requests

CMD ["python", "final_project.py"]