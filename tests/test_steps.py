import allure
from selene import browser, by, be


def test_decorator_steps():
    open_main_page()
    search_for_repository('irinavoron/qa.guru_lesson_10')
    open_repo('irinavoron/qa.guru_lesson_10')
    open_issues_tab()
    should_have_issue_with_text('homework')


@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open('/')


@allure.step('Ищем репозиторий {repo}')
def search_for_repository(repo):
    browser.element('.search-input').click()
    browser.element('#query-builder-test').type(repo).press_enter()


@allure.step('Переходим по ссылке репозитория {repo}')
def open_repo(repo):
    browser.element(by.link_text(repo)).click()


@allure.step('Открываем таб Issues')
def open_issues_tab():
    browser.element('#issues-tab').click()


@allure.step('Проверяем наличие issue с текстом {text}')
def should_have_issue_with_text(text):
    browser.element(by.partial_text(text)).should(be.visible)
