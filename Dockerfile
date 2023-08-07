FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt .

RUN apk update \
    && apk add --no-cache gcc musl-dev linux-headers

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu


COPY . .

ENV PYTHONUNBUFFERED=1

EXPOSE 8080

CMD ["python", "bot.py"]
