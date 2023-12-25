FROM python:3.11.5

WORKDIR /usr/src/hotro_backend/
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y --no-install-recommends netcat-traditional

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/hotro_backend/entrypoint.sh
RUN chmod +x /usr/src/hotro_backend/entrypoint.sh

# copy project
COPY . .
CMD ["gunicorn", "hotro_backend.wsgi:application", "--bind","0.0.0.0:8000"]
# run entrypoint.sh
# ENTRYPOINT ["/usr/src/backend/entrypoint.sh"]