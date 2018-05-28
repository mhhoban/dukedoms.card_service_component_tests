import os

from addict import Dict
from bravado.client import SwaggerClient
from bravado.swagger_model import load_file

def get_environment_variables(env):

    URLS = Dict()
    URLS.local.card_service = 'http://localhost:5005'
    URLS.local.card_service_db = 'postgresql+psycopg2://postgres:daleria@127.0.0.1:5432/card_service'

    URLS.container.card_service = 'card-service:5005'
    URLS.container.card_service_db = 'postgresql+psycopg2://dukedoms:daleria@dukedoms-rdbs:5432/card_service'

    if env == 'local':
        return URLS.local
    else:
        return URLS.container

def before_scenario(context, step):

    config = {
        'also_return_response': True,
        'validate_responses': True,
        'validate_requests': True,
        'validate_swagger_spec': True,
        'use_models': True,
        'formats': []
    }

    env = context.config.userdata.get('env')
    context.env_urls = get_environment_variables(env)
    context.clients = Dict()
    context.clients.card_service = SwaggerClient.from_spec(
        load_file(
            'specs/dukedoms_card_service_api.yaml',
        ),
        origin_url=context.env_urls.card_service,
        config=config
    )
