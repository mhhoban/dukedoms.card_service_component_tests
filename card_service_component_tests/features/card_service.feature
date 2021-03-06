@card_service
Feature: Card Service

  Scenario: Fetch Card Catalog
    When card service receives request for card catalog
    Then card service returns the expected card catalog

  Scenario: Card Info Request
    When card service receives request for card info for card ids:
      | card id |
      | 1       |
    Then card service returns card info:
      | card id | name        | category | type     | cost | actions | value | victory points |
      | 1       | Bronze Coin | treasure | treasure | 0    | None    | 1     | 0              |

  @foo
  Scenario: Set and Retrieve Card List
    Given an empty card service database
    When card service receives request to create card list record with data:
      | game id | treasure card list | victory card list | action card list |
      | 1337    | 1,2,3              | 4,5,6             | 7,8,9            |
    Then the request is successful
    When card service receives request for card list for game id "1337"
    Then card service returns card list with data:
      | game id | treasure card list | victory card list | action card list |
      | 1337    | 1,2,3              | 4,5,6             | 7,8,9            |
