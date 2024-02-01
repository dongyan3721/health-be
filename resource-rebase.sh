#!/bin/bash

file="$(pwd)/app/framework/config/ApplicationProperties.py"
property_file="$(pwd)/resource/application.yaml"
replacement="APPLICATION_PROPERTIES = YamlReader('${property_file}').original_data"

sed -i "s#APP.*data#${replacement}#g" "${file}"
echo "done"
