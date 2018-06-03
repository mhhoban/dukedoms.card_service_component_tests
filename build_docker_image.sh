#!/bin/bash
SERVICE=card_service_component_tests
docker build --build-arg service=$SERVICE \
--tag "mhhoban/dukedoms-card-service-tests:latest" .
