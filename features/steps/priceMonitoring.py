from behave import given, when, then
from pages.finance_page import FinancePage
from support.utils import get_percent_diff
import time

# Global variable to store prices
initial_price = None
prices = []


@given('I open the Google Finance {symbol} quote website')
def step_open_finance_page(context, symbol):
   try:
       context.page = FinancePage(context.driver)
       # Open the BTC page
       context.page.open_btc_page()
       context.page.wait_for_price_to_be_displayed()
       print("The BTC price is displayed")
   except Exception as error:
       print(f"The test did not run: {error}")


@when(
    'I monitor the BTC-USD price for a duration of {collect_duration:d} minutes at intervals of {poll_interval:d} seconds')
def step_monitor_prices(context, collect_duration, poll_interval):
    if poll_interval == 0:
        raise ValueError("The poll interval cannot be 0")
    collect_duration_in_seconds = collect_duration * 60
    total_price_records = collect_duration_in_seconds // poll_interval
    global prices
    prices = []
    context.page.open_btc_page()
    for _ in range(total_price_records):
        price = context.page.get_prices()
        prices.append(price)
        time.sleep(poll_interval)
    print("Prices collected")


@then('the average BTC-USD price does not vary by more than {threshold:d} %')
def step_validate_average_price_variation(context, threshold):
    initial_price = prices[0]
    if initial_price == 0:
        raise ValueError("The price cannot be 0")
    if not prices:
        raise ValueError("The collection of prices cannot be empty")
    sum_of_collected_prices = sum(prices)
    average_price = sum_of_collected_prices / len(prices)
    percentage_difference = ((average_price - initial_price) / initial_price) * 100
    is_average_price_lower_than_threshold = abs(percentage_difference) <= threshold
    assert is_average_price_lower_than_threshold, "The average price variation exceeds the threshold"

print("The average price does not vary by more than the expected threshold")


@then('there are no values that vary by more than {threshold:d} %')
def step_validate_individual_price_variations(context, threshold):
    prev_price = prices[0]
    for price in prices[1:]:
        percent_diff = get_percent_diff(prev_price, price)
        prev_price = price
        assert abs(percent_diff) <= threshold, "An individual price variation exceeds the threshold"
    print("The price variation does not exceed the expected threshold")