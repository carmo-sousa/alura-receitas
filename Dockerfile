FROM python:3.10

# Criando um usuário para executar o container
RUN useradd -m metatron

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev  \
    && rm -rf /var/lib/apt/lists/*

USER metatron

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

CMD [ "tail", "-f", "/dev/null" ]
