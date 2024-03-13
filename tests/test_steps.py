import allure
from selene import browser, by, be


def test_github():
    with allure.step('Открываем главную страницу'):
        browser.open('/')

    with allure.step('Ищем репозиторий'):
        browser.element('.search-input').click()
        browser.element('#query-builder-test').type('irinavoron/qa.guru_lesson_10').press_enter()

    with allure.step('Переходим по ссылке репозитория'):
        browser.element(by.link_text('irinavoron/qa.guru_lesson_10')).click()

    with allure.step('Открываем таб Issues'):
        browser.element('#issues-tab').click()

    with allure.step('Проверяем наличие issue с текстом homework'):
        browser.element(by.partial_text('homework')).should(be.visible)
