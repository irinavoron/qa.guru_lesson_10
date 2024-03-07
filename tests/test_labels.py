import allure
from allure_commons.types import Severity


def test_dynamic_labels():
    allure.dynamic.tag('web')
    allure.dynamic.feature('Задача')
    allure.dynamic.story('Неавторизованный пользователь не может создать задачу в репозитории')
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.link('https://github.com/', name="Testing")
    pass

@allure.tag('web')
@allure.label('owner', 'eroshenkoam')
@allure.feature('Задача')
@allure.story('Авторизованный пользователь может создать задачу в репозитории')
@allure.severity(Severity.CRITICAL)
@allure.link('https://github.com/', name="Testing")
def test_decarator_labels():
    pass