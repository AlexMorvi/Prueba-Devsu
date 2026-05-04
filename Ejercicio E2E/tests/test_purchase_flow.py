import logging

import pytest

from tests.data import EXPECTED_TOTAL, PRODUCTS

logger = logging.getLogger(__name__)


@pytest.mark.e2e
@pytest.mark.smoke
def test_complete_purchase_flow(home_page, product_page, cart_page, checkout_page, customer_data):
    logger.info("Step: open home page")
    home_page.navigate_to_home()

    logger.info("Step: add first product")
    home_page.click_phones_category()
    home_page.select_product(PRODUCTS[0])
    product_name_1 = product_page.get_product_name().lower()
    assert PRODUCTS[0].lower() in product_name_1
    product_page.add_to_cart()
    product_page.go_back_to_home()

    logger.info("Step: add second product")
    home_page.click_phones_category()
    home_page.select_product(PRODUCTS[1])
    product_name_2 = product_page.get_product_name().lower()
    assert PRODUCTS[1].lower() in product_name_2
    product_page.add_to_cart()

    logger.info("Step: validate cart")
    cart_page.navigate_to_cart()
    cart_page.wait_for_items_count(2)
    cart_items = cart_page.get_cart_items()
    cart_count = cart_page.get_cart_items_count()
    total_price = cart_page.get_total_price()

    assert cart_count == 2, f"Expected 2 items, got {cart_count}"
    assert len(cart_items) == 2, f"Expected 2 items in cart list, got {len(cart_items)}"
    assert total_price == EXPECTED_TOTAL, f"Expected total {EXPECTED_TOTAL}, got {total_price}"

    cart_names = {item.name.lower() for item in cart_items}
    assert PRODUCTS[0].lower() in cart_names
    assert PRODUCTS[1].lower() in cart_names

    logger.info("Step: checkout")
    cart_page.proceed_to_checkout()
    checkout_page.wait_for_purchase_modal()
    checkout_page.fill_purchase_form(customer_data)
    checkout_page.complete_purchase()

    assert checkout_page.is_purchase_successful(), "Purchase was not successful"
    success_message = checkout_page.get_success_message()
    assert "Thank you for your purchase!" in success_message
    checkout_page.close_success_modal()


@pytest.mark.e2e
def test_add_and_remove_from_cart(home_page, product_page, cart_page):
    logger.info("Step: open home page")
    home_page.navigate_to_home()

    logger.info("Step: add product")
    home_page.click_phones_category()
    home_page.select_product(PRODUCTS[0])
    product_page.add_to_cart()

    logger.info("Step: validate cart and remove item")
    cart_page.navigate_to_cart()
    cart_page.wait_for_items_count(1)
    assert cart_page.get_cart_items_count() == 1
    cart_page.delete_item(0)
    assert cart_page.get_cart_items_count() == 0


@pytest.mark.e2e
def test_empty_cart_checkout(home_page, cart_page, checkout_page):
    logger.info("Step: open home page and cart")
    home_page.navigate_to_home()
    cart_page.navigate_to_cart()

    assert cart_page.is_cart_empty()
    cart_page.proceed_to_checkout()

    if checkout_page.is_purchase_modal_open():
        checkout_page.close_purchase_modal()
