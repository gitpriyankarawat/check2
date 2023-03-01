import pytest
import time
import os

from selenium.webdriver.common.by import By


@pytest.mark.smoke
def test_login(driver):
    driver.switch_to.window(driver.window_handles[0])
    driver.implicitly_wait(2)
    assert "Startup: Open Budgets" in driver.title


@pytest.mark.smoke
def test_create_new_blank_budget(driver):
    """ Create new blank budget """
    driver.switch_to.window(driver.window_handles[0])
    assert "Startup: Open Budgets" in driver.title
    new_budget_field = driver.find_element_by_css_selector('.ui.inline.dropdown .dropdown.icon')
    new_budget_field.click()
    time.sleep(2)
    new_blank_budget = driver.find_element_by_xpath('//span[@class="text" and (text()="New Blank Budget")]')
    new_blank_budget.click()
    time.sleep(2)
    # assert 'Untitled Budget' in created_new_budget.text
    new_budget_field.click()


@pytest.mark.smoke
def test_create_budget_using_template(driver):
    """ Create new budget using template """
    new_budget_from_template = driver.find_element_by_xpath('//span[contains(@class,"text") and contains(text(),'
                                                                 '"New Budget From Template")]')
    new_budget_from_template.click()
    time.sleep(2)

    focused = driver.find_element_by_xpath('//a[contains(@class,"active item") and '
                                                'contains(text(),"Templates")]')
    assert focused.text == 'TEMPLATES'
    time.sleep(2)

    select_template_create_budget = driver.find_element_by_css_selector('.grid .grid-body .row:nth-child(1)')
    select_template_create_budget.click()
    time.sleep(2)

    # create_new_budget_from_template = driver.find_element_by_xpath('//button[contains'
    #                                                                     '(@class,"ui small button primary") and '
    #                                                                     'contains(text(),"New Budget From Template")]')
    create_new_budget_from_template = driver.find_element_by_css_selector('div > div.action-buttons.no-select > div > '
                                                                          'a:nth-child(1) > i')
    create_new_budget_from_template.click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)

    submit_renaming = driver.find_element_by_xpath('//button[@class = "ui primary button" and contains(text(),'
                                                   '"Submit")]')
    submit_renaming.click()
    time.sleep(4)

    archive_budget = driver.find_element_by_xpath('//i[contains(@class,"archive icon")]')
    archive_budget.click()
    time.sleep(2)

@pytest.mark.smoke
def test_import_budget_file(driver):
    """Import budget file"""
    new_budget_dropdown = driver.find_element_by_css_selector('.ui.inline.dropdown .dropdown.icon')
    new_budget_dropdown.click()
    time.sleep(1)

    import_mmb7_budget_template = driver.find_element_by_xpath('//span[contains(@class,"text") and '
                                                                    'contains(text(),"Import MMB7 Budget / Template")]')
    import_mmb7_budget_template.click()
    #driver.find_element(By.CLASS_NAME, "download icon").click()
    time.sleep(2)
    os.system("C:\FileUpload.exe")

    time.sleep(5)
