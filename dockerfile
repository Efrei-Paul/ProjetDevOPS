FROM python:3.7
EXPOSE 8501
RUN mkdir data
COPY model_dashboard.py ./
COPY requirements.txt ./
COPY build_model.py ./
COPY regression.joblib ./
COPY data/houses.csv data
RUN python3 -m pip install -r requirements.txt
RUN python3 build_model.py
CMD streamlit run model_dashboard.py
ENTRYPOINT ["streamlit", "run", "model_dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]
