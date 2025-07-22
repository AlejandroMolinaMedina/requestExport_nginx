FROM alpine:3.14

RUN apk add --no-cache python3 py3-pip build-base zlib-dev libffi-dev

# Actualiza pip y setuptools para soportar --break-system-packages
RUN pip install --upgrade pip setuptools

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --ignore-installed -r requirements.txt

COPY . .

CMD ["python3", "requestPerMinute.py"]
