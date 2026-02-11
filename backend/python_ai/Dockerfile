FROM python:3.11


WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --upgrade pip

RUN pip install -r /code/requirements.txt

# Expose port
EXPOSE 8000

COPY ./ /code/app
ENV PYTHONPATH=/code/app
CMD ["fastapi", "dev", "/code/app/main.py", "--host", "0.0.0.0", "--port", "8000"]