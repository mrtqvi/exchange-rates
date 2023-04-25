# requests info
BASE_URL = f"https://api.apilayer.com/fixer"

API_KEY = "GrSeL51GjEprTfDacQ4oSJ2sw2AYpYEF"

headers = {
    'apikey': API_KEY
}

# default rates
BASE_CURRENCY = "USD"
BASE_CONVERT_RATE = "IRR"

config = {
    'save_json': {
        'latest': True,
        'convert': True,
        'historical': False,
        'fluctuation': False
    },
}

# request validations
rules = {
    'latest': ['base', 'symbols'],
    'convert': ['from_rate', 'to_rate', 'amount'],
    'historical': ['date', 'from_rate', 'to_rate'],
    'fluctuation': ['start_date', 'end_date', 'base', 'to_rate']
}

# help messages
helps = {
    "help": f"'(*)' field is required and '*' is all items\n\n",

    'latest': f'latest'.ljust(15) +
              f'| default: latest base={BASE_CURRENCY} symbols=*\n\n',

    'convert': f'convert'.ljust(15) +
               f'| default: convert from_rate={BASE_CURRENCY} '
               f'to_rate={BASE_CONVERT_RATE}\n\n',

    'historical': f'historical'.ljust(15) +
                  '| default: historical date=(*) '
                  f'base_rate={BASE_CURRENCY} to_rate={BASE_CONVERT_RATE}\n\n',

    'fluctuation': f'fluctuation'.ljust(15) +
                   f'| default: historical start_date=(*)'
                   f' end_date=(*) base_rate={BASE_CURRENCY}'
                   f' to_rate={BASE_CONVERT_RATE}\n'
}
