FROM python:3.7-alpine
WORKDIR /project
COPY . .
RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip install -r requirements.txt
EXPOSE 5000

CMD ["python3", "MainScores.py"]
