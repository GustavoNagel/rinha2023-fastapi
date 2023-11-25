FROM python:3.11
ENV PYTHONUNBUFFERED 1
WORKDIR /rinha/

COPY poetry.lock pyproject.toml ./
RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false

COPY ./pyproject.toml ./poetry.lock* /rinha/

ARG INSTALL_DEV=false
RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install ; else poetry install --without dev ; fi"

COPY . /rinha
ENV PYTHONPATH=/rinha
EXPOSE 80
CMD ["uvicorn", "--factory", "rinha.main:create_app", "--host", "0.0.0.0", "--port", "80"]