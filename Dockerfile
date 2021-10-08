FROM python:3.9-slim-buster
RUN apt-get update && \
    apt-get install -y curl libgomp1



ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.1.6 

#POETRY
RUN pip install "poetry==$POETRY_VERSION"

# create workdir
WORKDIR /app
COPY poetry.lock pyproject.toml ./

 # Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install --no-root 
  
COPY . .

RUN poetry run python setup.py install

# flask
EXPOSE 5000

# run the command
# RUN useradd -m myuser
# USER myuser
# WORKDIR /app/password_complexity/app

ENV FLASK_APP="password_complexity/app/app.py"


CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0"]
