import allure
from allure_commons.types import Severity


def test_dynamic_labels():
    allure.dynamic.tag('web')
    allure.dynamic.label('owner', 'irinavoron')
    allure.dynamic.link('https://github.com')
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.feature('Issues')
    allure.dynamic.story('Not authorized user can`t create an issue')


@allure.tag('web')
@allure.link('https://github.com')
@allure.label('owner', 'irinavoron')
@allure.severity(Severity.BLOCKER)
@allure.feature('Issues')
@allure.story('Authorized user can create issues')
def test_decorator_labels():
    pass
