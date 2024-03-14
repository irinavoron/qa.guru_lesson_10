import allure
from selene import browser, by, be


def test_github_with_allure_steps():
    with allure.step('Open main page'):
        browser.open('/')

    with allure.step('Search repository'):
        browser.element('.search-input').click()
        browser.element('#query-builder-test').type('irinavoron/qa.guru_lesson_10').press_enter()

    with allure.step('Open repository'):
        browser.element(by.link_text('irinavoron/qa.guru_lesson_10')).click()

    with allure.step('Open Issues tab'):
        browser.element('#issues-tab').click()

    with allure.step('Check issue with "homework" in the title'):
        browser.element(by.partial_text('homework')).should(be.visible)
