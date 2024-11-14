FROM python:3.10-alpine3.19

WORKDIR /opt

ENV \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1

COPY ./ /opt
RUN apk add --no-cache build-base linux-headers cmake ninja
RUN pip install --no-cache-dir -r /opt/requirements.txt

CMD ["sh", "-c", "python -m api"]