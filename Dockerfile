FROM python:3.10

WORKDIR /CS333-Final-Project

COPY . /CS333-Final-Project

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "final_project.py"]