FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /app/pretrained_models && chmod -R 777 /app/pretrained_models
RUN mkdir -p /app/cache && chmod -R 777 /app/cache
RUN mkdir -p /app/wav2vec2_checkpoints && chmod -R 777 /app/wav2vec2_checkpoints
RUN mkdir -p /app/audio_cache && chmod -R 777 /app/audio_cache

ENV HF_HOME=/app/cache/hf_home
ENV SPEECHBRAIN_PRETRAINED_DIR=/app/pretrained_models
ENV XDG_CACHE_HOME=/app/cache

COPY requirements.txt ./
COPY src/ ./src/

RUN pip3 install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "src/streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]