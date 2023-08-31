FROM python:3-slim

WORKDIR /app
COPY mqtt-republisher.py /app

RUN pip install --no-cache-dir paho-mqtt

ENV BROKER=
ENV PORT=1883
# Topics are json string arrays, e.g. ["dsmr/reading/electricity_delivered", "dsmr/reading/electricity_returned"]
ENV TOPICS=
# Suffix to add to the listed topics
ENV NEW_TOPIC_SUFFIX=_1
# Enable debug logging
ENV DEBUG=false

CMD ["python", "mqtt-republisher.py"]