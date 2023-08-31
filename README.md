# mqtt-republisher
A super simple script I threw toghether as I needed to get my DSMR Reader plugin in Home Assistant to work with the topics the smartgateway.nl produces.
It will just add a prefix (same for all) topics that are listened to.

## Configuration
These environment variables are available

`BROKER` The IP/FQDN of the broker to connect to
`PORT` The port to connect to
`TOPICS` Topics are json string arrays, e.g. ["dsmr/reading/electricity_delivered", "dsmr/reading/electricity_returned"]
`NEW_TOPIC_SUFFIX` Suffix to add to the listed topics, setting it to `_1` would produce dsmr/reading/electricity_delivered_1 and the data is just copied over
`DEBUG` Enable debug logging

## How to build and run

Build it first;
```
docker build -t mqtt-republisher . 
```

Then run it using
```
docker run -it --rm \
    --name my-running-app \
    -e BROKER=host.docker.internal \
    -e TOPICS='[\"dsmr/reading/electricity_delivered\", \"dsmr/reading/electricity_returned\"]' \
    mqtt-republisher
```