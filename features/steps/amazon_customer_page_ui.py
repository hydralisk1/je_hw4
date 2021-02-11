from selenium.webdriver.common.by import By
from behave import given, then

@given('Open Amazon Customer Service page')
def open_amazon_customer_service(context):
    context.driver.get("https://www.amazon.com/gp/help/customer/display.html")


@then('Verify UI elements are present')
def verify_ui_elements(context):
    greetings_and_help_topics = context.driver.find_elements(By.XPATH, "//h1")
    card_menus = context.driver.find_elements(By.XPATH, "//div[@class='a-box self-service-rich-card']//h3")
    help_topics = context.driver.find_elements(By.XPATH, "//a[contains(@rel, '#help-gateway-category')]")

    assert greetings_and_help_topics, "There are no greetings and browse help topics"
    assert card_menus, "There's no card menu"
    assert help_topics, "There's no help topics"

    print(f"Greeting Message: {greetings_and_help_topics[0].text}")
    print(f"Card Menus: {', '.join([menu.text for menu in card_menus])}")
    print(f"Help Topics Title: {greetings_and_help_topics[1].text}")
    print(f"Help Topics: {', '.join([topic.text for topic in help_topics])}")
