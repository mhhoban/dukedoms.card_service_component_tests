card_catalog = {
    '1': {
        'name': 'Bronze Coin',
        'category': 'treasure',
        'type': 'treasure',
        'cost': 0,
        'actions': 'None',
        'value': 1,
        'victoryPoints': 0,
        'id': 1
    },
    '2': {
        'name': 'Silver Coin',
        'category': 'treasure',
        'type': 'treasure',
        'cost': 3,
        'actions': 'None',
        'value': 2,
        'victoryPoints': 0,
        'id': 2
    },
    '3': {
        'name': 'Gold Coin',
        'category': 'treasure',
        'type': 'treasure',
        'cost': 6,
        'actions': 'None',
        'value': 3,
        'victoryPoints': 0,
        'id': 3
    },
    '4': {
        'name': 'Hovel',
        'category': 'victory',
        'type': 'victory',
        'cost': 1,
        'actions': 'None',
        'value': 0,
        'victoryPoints': 1,
        'id': 4
    },
    '5': {
        'name': 'Estate',
        'category': 'victory',
        'type': 'victory',
        'cost': 1,
        'actions': 'None',
        'value': 0,
        'victoryPoints': 2,
        'id': 5
    },
    '6': {
        'name': 'Palace',
        'category': 'victory',
        'type': 'victory',
        'cost': 1,
        'actions': 'None',
        'value': 0,
        'victoryPoints': 3,
        'id': 6
    },
    '7': {
        'name': 'Township',
        'category': 'action',
        'type': 'action',
        'cost': 1,
        'actions': [
            {'action': 'add_draw', 'arguments': 'draws=1'},
            {'action': 'add_action', 'arguments': 'actions=1'}
        ],
        'value': 0,
        'victoryPoints': 0,
        'id': 7
    },
    '8': {
        'name': 'Maproom',
        'category': 'action',
        'type': 'action',
        'cost': 1,
        'actions': [
            {'action':'addDraw', 'arguments':'draws=2'},
            {'action':'addAction', 'arguments':'actions=1'}
        ],
        'value': 0,
        'victoryPoints': 0,
        'id': 8
    },
    '9': {
        'name': 'Forge',
        'category': 'action',
        'type': 'action',
        'cost': 1,
        'actions': [{'action':'addDraw', 'arguments':'draws=3'}],
        'value': 0,
        'victoryPoints': 0,
        'id': 9,
    },
    '10': {
        'name': 'Cosmopolitan',
        'category': 'action',
        'type': 'action',
        'cost': 1,
        'actions': [{'action': 'addBuy', 'arguments':'buys=1'}],
        'value': 0,
        'victoryPoints': 0,
        'id': 10,
    },
    '11': {
        'name': 'Manic',
        'category': 'action',
        'type': 'action',
        'cost': 1,
        'actions': [{'action': 'addAction', 'arguments':'actions=1'}],
        'value': 0,
        'victoryPoints': 0,
        'id': 11,
    },
    '12': {
        'name': 'Bazzar',
        'category': 'action',
        'type': 'action',
        'cost': 1,
        'actions': [
            {'action': 'addTempTreasure', 'arguments': 'treasure=1'},
            {'action': 'addDraw', 'arguments': 'draws=1'},
            {'action': 'addBuys', 'arguments': 'buys=1'},
            {'action': 'addAction', 'arguments': 'actions=1'}

        ],
        'victoryPoints': 0,
        'id': 12
    }

}
