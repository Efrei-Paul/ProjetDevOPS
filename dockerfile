FROM ubuntu:latest
RUN mkdir data
COPY model_dashboard.py ./
COPY requirements.txt ./
COPY build_model.py ./
COPY regression.joblib ./
COPY data/houses.csv data
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip
RUN pip install --requirement requirements.txt
RUN python3 build_model.py
EXPOSE 8501
ENTRYPOINT ["streamlit", "run", "model_dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]