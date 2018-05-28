#!/bin/bash

#fetch card service API Spec

curl https://raw.githubusercontent.com/mhhoban/dukedoms.card_service_api/master/dukedoms_card_service_api.yaml -O
mv dukedoms_card_service_api.yaml card_service_component_tests/specs/dukedoms_card_service_api.yaml
