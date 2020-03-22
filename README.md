# Raspberry Pi Fan MQTT Control
Python deamon for Raspberry Pi that controls a fan by a relay board through MQTT.

# INSTALLATION

### Raspberry Pi
Install the required Python modules

```shell
sudo apt install python3-paho-mqtt python3-rpi.gpio
```

### Home Assistant
https://www.home-assistant.io/integrations/fan.mqtt/

```yaml
mqtt:
  broker: [mqtt-broker-ip]

fan:
  - platform: mqtt
    name: "Mechanische ventilator"
    state_topic: "ha/fan/forced_ventilation/on/state"
    command_topic: "ha/fan/forced_ventilation/on/set"
    speed_state_topic: "ha/fan/forced_ventilation/speed/state"
    speed_command_topic: "ha/fan/forced_ventilation/speed/set"
    qos: 0
    payload_on: "true"
    payload_off: "false"
    payload_low_speed: "low"
    payload_medium_speed: "medium"
    payload_high_speed: "high"
    speeds:
      - low
      - medium
      - high
```

# RUN

```shell
python3 ./rpi-fan-mqtt-control/fan-mqtt.py [mqtt-broker-ip]
```

# MQTT TESTING

https://mosquitto.org/download/

```shell
cd "c:\Program Files\mosquitto"

mosquitto_sub -h [mqtt-broker-ip] -t ha/fan/forced_ventilation/on/state -C 1
```

# TODO

- [ ]   better documentation
- [ ]   better error handling
- [ ]   fan at low speed when script or rpi fails
