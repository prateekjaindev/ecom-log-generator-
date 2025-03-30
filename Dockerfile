FROM python:3.9-slim AS builder

WORKDIR /app
COPY ecom_log_generator.py .

FROM python:3.9-slim AS runtime

WORKDIR /app
COPY --from=builder /app/ecom_log_generator.py .

VOLUME ["/var/log"]

CMD ["python", "ecom_log_generator.py"]