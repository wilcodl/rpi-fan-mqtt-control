# Raspberry Pi Fan MQTT Control
Python deamon for Raspberry Pi that controls a fan by a relay board through MQTT.

# INSTALLATION

### Raspberry Pi
Install the required Python modules

```shell
sudo apt install python3-paho-mqtt python3-rpi.gpio python3-yaml
```

Clone the repository

```shell
sudo apt install git
git clone https://github.com/wilcodl/rpi-fan-mqtt-control.git
```

Create and edit the config file
```shell
cd rpi-fan-mqtt-control
cp config-example.yml config.yml
vi config.yml
```

Make file executable
```shell
chmod +x fan-*
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

### Physical installation

![rPi-relay-fan](https://raw.githubusercontent.com/wilcodl/rpi-fan-mqtt-control/master/IMG_20200328_215258.jpg)

# RUN

Test version:

```shell
./fan-manual.py
```

MQTT version:

```shell
./fan-mqtt.py
```

Start MQTT deamon with log file:

```shell
python3 -u fan-mqtt.py > fan-mqtt.log &
watch cat fan-mqtt.log
```

# MQTT TESTING

https://mosquitto.org/download/

```shell
cd "c:\Program Files\mosquitto"

.\mosquitto_pub.exe -h [mqtt-broker-ip] -t ha/fan/forced_ventilation/on/set -m true
```

# TODO

- [x]   better documentation
- [ ]   better error handling
- [x]   improve log
- [x]   fan at low speed when script or rpi fails
