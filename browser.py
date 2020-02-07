from selenium import webdriver
import time

class Browser:
    def __init__(self, chromepath):
        self.window = webdriver.Chrome(executable_path=chromepath)
        self.window.set_window_size(400, 400)

    def get_page(self, queue_object):
        self.window.get(queue_object['url'])

    def scrape_links(self, queue_object):
        self.get_page(queue_object)
        return self.window.find_elements_by_css_selector(queue_object['links_selector'])

    def scrape_text(self, queue_object):
        return self.window.find_element_by_css_selector(queue_object['links_selector'])

    def scroll_window(self):
        self.window.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
