FROM python:3.10
    
RUN python3 -m venv /venv

ENV PATH="/venv/bin:$PATH"

RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com --no-cache-dir
ADD . /app/

EXPOSE 8000

CMD ["python", "-m streamlit run ./Home.py --server.port 8000 --server.address 0.0.0.0"]