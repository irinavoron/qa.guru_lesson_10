import allure
from allure_commons.types import Severity
from selene import browser, by, be


@allure.tag('web')
@allure.label('owner', 'irinavoron')
@allure.severity(Severity.CRITICAL)
@allure.feature('Issues')
@allure.story('Issues are displayed on the page')
@allure.description('The issue with the text in the title should be visible')
@allure.description_html('<h3>Checking Issues tab in GitHub</h3>')
@allure.id('112')
@allure.title('The issue with the text in the title should be visible')
@allure.epic('GitHub')
@allure.suite('Issues visibility')
def test_github_with_allure_step():
    allure.dynamic.link('https://github.com')

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
