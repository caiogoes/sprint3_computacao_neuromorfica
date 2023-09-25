# Use uma imagem Python como base
FROM python:3.9.7

# Copie o código Python para o contêiner
COPY sprint3_computacao_neuromorfica.py /app.py
COPY stadiums.db /stadiums.db

# Instale quaisquer dependências do seu código Python
RUN pip install pandas
RUN pip install flask
RUN pip install flask-ngrok

# Exponha uma porta para o serviço Python
EXPOSE 80

# Comando para iniciar o serviço Python
CMD ["python", "/app.py"]
