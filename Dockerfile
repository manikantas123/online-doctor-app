# === STAGE 1: Build stage ===
FROM python:3.10-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install --user --no-cache-dir -r requirements.txt

# === STAGE 2: Final stage ===
FROM python:3.10-slim AS final

WORKDIR /app

COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
