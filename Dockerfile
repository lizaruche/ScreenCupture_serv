FROM python:3.9

RUN mkdir -p /ScreenCupture
WORKDIR /ScreenCupture

COPY . /ScreenCupture
RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "main.py"]