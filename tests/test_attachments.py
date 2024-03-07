import json
import allure
from allure import attachment_type

def test_attachments():
    allure.attach('Text content', 'Text', attachment_type=attachment_type.TEXT)
    allure.attach('T<h1> hello world! </h1>', 'HTML', attachment_type=attachment_type.HTML)
    allure.attach(json.dumps({'First': 1, 'Second': 2}), 'JSON', attachment_type=attachment_type.JSON)