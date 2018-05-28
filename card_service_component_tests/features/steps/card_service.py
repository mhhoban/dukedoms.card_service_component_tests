from behave import given, then, when
from bravado.exception import HTTPNotFound
from hamcrest import assert_that, equal_to, is_not, greater_than, has_item, has_property
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from card_service_component_tests.constants import card_catalog as expected_card_catalog

@given('an empty account database')
def clear_account_service_db(context):
    """
    drop any existing information from tables for a clean test run.
    """
    engine = create_engine(context.env_urls.card_service_db)
    Session = scoped_session(sessionmaker(bind=engine))
    session = Session()

    session.execute('TRUNCATE TABLE cardLists')
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
    card_ids = [int(row['card id']) for row in context.table]

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
