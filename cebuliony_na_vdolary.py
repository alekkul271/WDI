import requests
from bs4 import BeautifulSoup


def getting_exchange_rate():

    # getting an URL address
    url = 'https://www.nbp.pl'

    # Trying to get data from a specified resource
    response = requests.get(url)

    # Need to parse into html file
    soup = BeautifulSoup(response.text, "html.parser")

    # Need to get to a table with exchange rates.
    result = soup.find('div', attrs={'id':'rightSide'})
    result = result.find_all('table') # searching for tables

    # Finding all <tr>
    result = result[1].find_all("tr")

    # Asking user to choose a currency.
    chosen_currency = "USD"

    # Searching for asked currency in a table
    for currency in result:

        # Find method returns -1 if searched value hasn't been found,
        # checking if specified item is the one we search for
        if str(currency.contents[0].contents[0]).find(chosen_currency) != -1:

            # Returning an item after conversion to float number,
            # originally it would look like this:
            # <td>1 EUR</td>
            # <td>4,2775</td>
            # contents method extracts just a string with exchange rate.
            return float(str(currency.contents[1].contents[0]).replace(',', '.'))


def converter(converted_usd_exchange_rate):
    v_dollar_in_usd = 1000/9.99
    cebulion = 10
    quantity = int(input("Jaka ilosc cebulionow chcialbys przeliczyc:"))
    print('Po przeliczeniu wychodzi: {:.2f} v-dolarow.'.format(quantity / cebulion / converted_usd_exchange_rate * v_dollar_in_usd))


converter(getting_exchange_rate())
