from selene import have, be
from selene.support.by import text
from selene.support.shared import browser
from allure import step as title


def test_search():
    with title('Type search'):
        browser.element('Search Wikipedia').tap()
        browser.element('#search_src_text').type('BrowserStack')

    with title('Verify content found'):
        browser.all('#page_list_item_title').should(have.size_greater_than(0))
        browser.element('«Software company based in India»').should(be.visible)


def test_search_positive():
    with title('Type search'):
        browser.element('org.wikipedia.alpha:id/search_container').click()
        browser.element('org.wikipedia.alpha:id/search_src_text').type('Star wars')

    with title('Verify content found'):
        browser.all('#page_list_item_title').should(have.size_greater_than(0))
        browser.element('org.wikipedia.alpha:id/page_list_item_image').should(be.visible)

    with title('Verify image is visible'):
        browser.elements('org.wikipedia.alpha:id/page_list_item_title').find_element(text('Star Wars')).click()
        browser.element('org.wikipedia.alpha:id/view_page_header_image').should(be.visible)
