from selenium.webdriver.common.by import By
from behave import given, then

LINKS_BESTSELLERS = (By.XPATH, "//div[@id='zg_tabs']//a")


@given('Open Amazon Best Sellers page')
def open_amazon_best_sellers_page(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('Verify if there are {expected_num_of_links} links')
def search_keyword(context, expected_num_of_links):
    number_of_links = len(context.driver.find_elements(*LINKS_BESTSELLERS))
    assert number_of_links == int(
        expected_num_of_links), f"Expected {expected_num_of_links} links there, but there are {number_of_links} links. "
