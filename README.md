# Dukedoms Card Service Component Tests

### Test repo to make sure Dukedoms Card Service is playing nicely with its db and functioning appropriately

## Setup:
get service api spec with `./oas_setup.sh`
`pip install -r requirements.txt`
`pip install -e .`

## Testing:
Run local tests from within `card_service_component_tests` directory
`behave --stage=local`
