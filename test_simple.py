from selene.support.shared import browser
from selene import be, have
import pytest

@pytest.fixture
def config_browser(open_base_url):
    browser.config.window_width = 768
    browser.config.window_height = 1024
    return browser

@pytest.fixture
def open_base_url():
    browser.open('https://google.com')


def test_google_positive(config_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    assert browser.element('[id="search"]').should(have.text('yashaka/selene: '
                                                             'User-oriented Web UI browser tests in Python'))

def test_google_negative(config_browser):
    browser.element('[name="q"]').should(be.blank).type('agadfgvadfgertherth').press_enter()
    assert browser.element('.card-section').should(have.text('По запросу agadfgvadfgertherth ничего не найдено.'))