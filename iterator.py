

class Iterator:

    def __init__(self, queue, browser):
        self.queue = queue
        self.visited = self.queue.visited
        self.queue.add_to_queue({'url':'https://webscraper.io/test-sites/e-commerce/allinone'})
        self.browser = browser
        
    def make_step(self):
        self.browser.get_page(self.queue.get_first())

