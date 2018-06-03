from behave import given, then, when
from bravado.exception import HTTPNotFound
from hamcrest import assert_that, equal_to, is_not, greater_than, has_item, has_property
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from card_service_component_tests.constants import card_catalog as expected_card_catalog

@given('an empty card service database')
def clear_account_service_db(context):
    """
    drop any existing information from tables for a clean test run.
    """
    engine = create_engine(context.env_urls.card_service_db)
    Session = scoped_session(sessionmaker(bind=engine))
    session = Session()

    session.execute('TRUNCATE TABLE cardlists')
    session.commit()
    session.close()

@when('card service receives request for card catalog')
def request_card_service_catalog(context):
    """
    send request to card service for entire catalog
    """
    catalog, result = context.clients.card_service.cardInfo.get_card_catalog().result()
    assert_that(result.status_code, equal_to(200))
    context.card_catalog = catalog

@then('card service returns the expected card catalog')
def assert_card_catalog(context):
    """
    verify correct card service returned
    """
    for item in expected_card_catalog.keys():
        assert_that(
            context.card_catalog[item],
            equal_to(expected_card_catalog[item])
        )

@when('card service receives request for card info for card ids')
def request_card_info(context):
    """
    query card service for a specific card's info
    """
    card_ids = [row['card id'] for row in context.table]

    card_info, result = context.clients.card_service.cardInfo.get_card_info(
        cardIds=card_ids
    ).result()

    assert_that(result.status_code, equal_to(200))
    context.card_info = card_info

@then('card service returns card info')
def assert_card_info(context):
    """
    assert correct card info retreived
    """
    for row in context.table:
        card = context.clients.card_service.get_model('CardInfo')(
            id=int(row['card id']),
            name=row['name'],
            category=row['category'],
            type=row['type'],
            cost=int(row['cost']),
            actions=row['actions'],
            value=int(row['value']),
            victoryPoints=int(row['victory points'])
        )
        assert_that(
            context.card_info,
            has_item(card)
        )

@when('card service receives request to create card list record with data')
def create_card_list(context):
    """
    Send request to create card list for a game
    """

    for row in context.table:
        _, result = context.clients.card_service.listOperations.set_card_list(
            setCardListRequest=context.clients.card_service.get_model('SetCardListRequest')(
                gameId=int(row['game id']),
                victoryCards=[int(card) for card in row['victory card list'].split(',')],
                treasureCards=[int(card) for card in row['treasure card list'].split(',')],
                actionCards=[int(card) for card in row['action card list'].split(',')]
                )
        ).result()
        assert_that(result.status_code, equal_to(202))

@then('the request is successful')
def request_successful_pass(context):
    pass

@when('card service receives request for card list for game id "{game_id:d}"')
def fetch_card_list(context, game_id):
    """
    send request to card service to get card list for given game_id
    """
    card_list, result = context.clients.card_service.listOperations.get_card_list(
        gameId=game_id
    ).result()
    assert_that(result.status_code, equal_to(200))
    context.card_list = card_list

@then('card service returns card list with data')
def assert_card_list(context):
    """
    assert that the correct card list was returned
    """
    for row in context.table:
        expected_card_list = context.clients.card_service.get_model('CardList')(
            victoryCards=[int(card) for card in row['victory card list'].split(',')],
            treasureCards=[int(card) for card in row['treasure card list'].split(',')],
            actionCards=[int(card) for card in row['action card list'].split(',')],
        )
        assert_that(context.card_list, equal_to(expected_card_list))
