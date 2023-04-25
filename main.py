from config import BASE_URL, BASE_CURRENCY, BASE_CONVERT_RATE, rules,\
    headers, helps, config
import requests
import sys
import os
import json
from datetime import datetime


def send(address):
    """
        The task of sending a request to the api

        Arguments:
        address (str): In fact, it is the same url that we are going to send a request to

        Returns: dict | str
    """
    try:
        response = requests.request("GET", address, headers=headers)
        if response.status_code == 200:
            return json.loads(response.text)

        elif response.status_code == 429:
            print("you have submitted too many requests")
            exit()

    except (Exception, ConnectionError):
        print("a network error has occurred. please check your connection.")
        exit()


def latest(base=BASE_CURRENCY, symbols=None):
    """
        Return the latest exchange rates

        Arguments:
        base (str): Is the base rate. the price of other currencies is determined accordingly (default: USD)
        symbols (str): We can perform this operation only on the currencies of our choice for example (CAD,IRR,JPY). (default: all currency rates)

        Returns: dict | None
    """
    url = f"{BASE_URL}/latest&base={base.upper()}"
    if symbols is not None:
        url += f"&symbols={symbols.upper()}"

    return send(url)


def convert(from_rate=BASE_CURRENCY, to_rate=BASE_CONVERT_RATE, amount=1):
    """
        To convert one currency to another

        Arguments:
        from_rate (str): The base rate is the conversion on which the result is returned
        to_rate (str): The rate to be converted
        amount (int): The amount to be converted

        Returns: dict | None
    """
    url = f"{BASE_URL}/convert&from={from_rate.upper()}&" \
          f"to={to_rate.upper()}&amount={amount}"

    return send(url)


def historical(date, base_rate=BASE_CURRENCY, to_rate=BASE_CONVERT_RATE):
    """
        Returns the conversion rate on the date we specify

        Arguments:
        date (str): The date you find the exchange rates
        base_rate (str): The base rate is the conversion on which the result is returned
        to_rate (str): The rate to be converted

        Returns: dict | None
    """
    url = f"{BASE_URL}/{date}&base={base_rate.upper()}&" \
          f"symbols={to_rate.upper()}"

    return send(url)


def fluctuation(
        start_date, end_date, base=BASE_CURRENCY, to=BASE_CONVERT_RATE):
    """
        Returns the fluctuation of currencies based on the time period

        Arguments:
        start_date (str): Date of starting fluctuation (format: YYYY-mm-dd)
        end_date (str): Date of ending fluctuation (format: YYYY-mm-dd)
        base (str): Changes are made in relation to this currency.
        to_rate (str): The rate that has changed in this period

        :return: dict | None
    """
    url = f"{BASE_URL}/fluctuation&start_date={start_date}" \
          f"&end_date={end_date}&base={base.upper()}&symbols={to.upper()}"

    return send(url)


def check_parameters():
    """
        Checking whether the input parameters are valid or not

        :return: dict | False
    """
    method = sys.argv[1]
    parameters = sys.argv[2:]

    if method not in rules:
        return False

    args = {}
    for param in parameters:
        arg = param.split('=')
        if arg[0] not in rules[method]:
            return False

        args.update({arg[0]: arg[1]})

    return {
        'method': method,
        'args': args
    }


def help_message():
    """
        Provide guidance based on input parameters

        :return: str
    """
    try:
        if len(sys.argv) == 3:
            parameter = sys.argv[2]
            return helps[parameter]

        messages = ""
        for help_msg in helps.values():
            messages += help_msg

        return messages

    except KeyError:
        print('your request invalid, please check inputs')
        return False


def run():
    """
        Presentation based on user input requests

        :return: dict | false
    """
    try:
        if sys.argv[1] == '-h':
            return help_message()

        res = check_parameters()
        if res:
            method = eval(res['method'])
            data = method(**res['args'])
            if data is not None:
                return {"action": res['method'], **data}

        return False
    except (Exception, NameError, ValueError):
        print('your request invalid, please check inputs')
        return help_message()


def save_as_json(data):
    """
        Save the file as an archive

        :param data: dict
        :return: void
    """

    now = datetime.now().strftime("%m-%d-%Y-%H:%M:%S")
    filename = data['action'] + "-" + now

    data = json.dumps(data)

    if not os.path.exists("archive"):
        os.mkdir("archive")

    with open("archive/" + filename + ".json", 'w') as file:
        file.write(data)

    print(f'The file was saved as {filename}')


if __name__ == "__main__":
    result = run()

    if result is not False:
        if type(result) == str:
            print(result)
            exit()

        # Checking that these results need to be stored in a json file
        action = result.get('action', None)
        if config['save_json'][action]:
            save_as_json(result)
