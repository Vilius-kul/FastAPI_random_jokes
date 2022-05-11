FROM python:3


COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

RUN chmod +x start_server.sh


ENTRYPOINT [ "bash", "./start_server.sh"]


