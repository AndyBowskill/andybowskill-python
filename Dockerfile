FROM python:3.9.1-slim as production

ENV PYTHONUNBUFFERED=1
WORKDIR /app/

COPY andybowskill_website/requirements/prod.txt ./requirements/prod.txt
RUN pip install -r ./requirements/prod.txt

COPY andybowskill_website/manage.py ./manage.py
COPY andybowskill_website/andybowskill_website ./andybowskill_website

EXPOSE 8000

FROM production as development

COPY andybowskill_website/requirements/dev.txt ./requirements/dev.txt
RUN pip install -r ./requirements/dev.txt

COPY . .