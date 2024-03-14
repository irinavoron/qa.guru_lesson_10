import allure
from selene import browser, by, be


@allure.step('Open main page')
def open_main_page():
    browser.open('/')


@allure.step('Search repository {repo}')
def search_repository(repo):
    browser.element('.search-input').click()
    browser.element('#query-builder-test').type(repo).press_enter()


@allure.step('Go to the repo {repo}')
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step('Open Issues tab')
def open_issues_tab():
    browser.element('#issues-tab').click()


@allure.step('Check issue with text in it {text}')
def should_have_text(text):
    browser.element(by.partial_text(text)).should(be.visible)


def test_github_with_decorator_allure_step():
    open_main_page()
    search_repository('irinavoron/qa.guru_lesson_10')
    go_to_repository('irinavoron/qa.guru_lesson_10')
    open_issues_tab()
    should_have_text('homework')
