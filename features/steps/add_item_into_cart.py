from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from time import sleep

ADD_TO_CART_BT = (By.ID, "add-to-cart-button")
CART_ICON = (By.ID, "nav-cart")


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')


@when('The search phrase "{product_name}" is entered')
def search_for_product(context, product_name):
    search_bar = (By.XPATH, "//input[@id='twotabsearchtextbox']")
    context.driver.find_element(*search_bar).send_keys(product_name.lower(), Keys.ENTER)


@then('Results containing "{product_name}" are shown')
def result_page(context, product_name):
    results = context.driver.find_elements(By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")
    # Create a list that has results containing product name
    results_product_name = [p.text for p in results if
                            all(item in p.text.lower().split() for item in product_name.lower().split())]
    assert len(results_product_name) > 0, f"There's no result containing {product_name}."


@when('Click on one containing "{product_name}", which has the largest number of reviews')
def click_the_largest_reviews(context, product_name):
    results = context.driver.find_elements(By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")
    # Create a list having elements containing product name
    links = [p for p in results if all(item in p.text.lower().split() for item in product_name.lower().split())]
    # Create an empty list to store the number of reviews
    reviews = []

    for p in links:
        try:
            # Store the number of reviews to the list
            reviews.append(
                int(p.find_element(By.XPATH, "./../../../..//span[@class='a-size-base']").text.replace(",", "")))
        # if there's no review, append 0
        except NoSuchElementException:
            reviews.append(0)

    # click the link that has the largest number of reviews
    links[reviews.index(max(reviews))].click()


@then('The product page is shown, and it has an add to cart button')
def product_page(context):
    add_to_cart = context.driver.find_elements(*ADD_TO_CART_BT)
    assert add_to_cart, "There's no Add to Cart button"


@then('Click on the Add to Cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BT).click()
    sleep(4)
    popover = context.driver.find_elements(By.XPATH, "//button[@data-action='a-popover-close']")
    if popover:
        popover[0].click()


@when('Click on the Cart icon')
def click_cart(context):
    context.driver.find_element(*CART_ICON).click()


@then('Verify "{product_name}" is in the cart')
def verify_cart(context, product_name):
    empty_message = context.driver.find_elements(By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']//h2")
    assert empty_message == [], "Your cart is empty"

    item = context.driver.find_element(By.XPATH, "//span[@class='a-size-medium sc-product-title a-text-bold']").text
    qty = context.driver.find_element(By.XPATH, "//span[@class='sc-non-editable-quantity-right']").text

    print(f"{item}\n{qty}")
