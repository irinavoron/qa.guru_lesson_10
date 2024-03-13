from selene import browser, by, be


def test_github():
    browser.open('/')

    browser.element('.search-input').click()
    browser.element('#query-builder-test').type('irinavoron/qa.guru_lesson_10').press_enter()
    browser.element(by.link_text('irinavoron/qa.guru_lesson_10')).click()
    browser.element('#issues-tab').click()

    browser.element(by.partial_text('homework')).should(be.visible)
