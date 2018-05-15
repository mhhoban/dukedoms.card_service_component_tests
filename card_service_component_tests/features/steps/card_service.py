from behave import given, then, when
from bravado.exception import HTTPNotFound
from hamcrest import assert_that, equal_to, is_not, greater_than, has_item
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

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
    catalog, result = context.clients.card_service.cardInfo.get_card_catalog()
    import pdb
    pdb.set_trace()
