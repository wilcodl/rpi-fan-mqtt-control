# Raspberry Pi Fan MQTT Control
Python deamon for Raspberry Pi that controls a fan by a relay board through MQTT. See the wiki for extended documentation.

# INSTALLATION

Install the required Python modules

```shell
sudo apt install python3-paho-mqtt python3-rpi.gpio python3-yaml
```

Copy and edit the config file
```shell
cd rpi-fan-mqtt-control
cp config-example.yml config.yml
vi config.yml
```

# RUN

```shell
python3 fan-mqtt.py
```
