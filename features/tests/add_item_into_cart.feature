# Created by Joonil at 2/10/21
Feature: Test Scenarios for adding a product into the cart on Amazon.

  Scenario: Search for Product user want and add the one that has the largest number of reviews on the first page into the cart
    Given Open Amazon page
    When The search phrase "Google Wifi" is entered
    Then Results containing "Google Wifi" are shown
    When Click on one containing "Google Wifi", which has the largest number of reviews
    Then The product page is shown, and it has an add to cart button
    And Click on the Add to Cart button
    When Click on the Cart icon
    Then Verify "Google Wifi" is in the cart

