FROM ubuntu:latest
COPY model_dashboard.py ./
COPY requirements.txt ./
COPY build_model.py ./
COPY regression.joblib ./
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip
RUN pip install --requirement requirements.txt