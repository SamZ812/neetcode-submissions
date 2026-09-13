class BrowserHistory:

    def __init__(self, homepage: str):
        self.pointer = self
        self.url = homepage
        self.next = None
        self.prev = None
        

    def visit(self, url: str) -> None:
        newPage = BrowserHistory(url)
        previous = self.pointer
        previous.next = newPage
        newPage.prev = previous
        self.pointer = newPage


    def back(self, steps: int) -> str:
        while self.pointer.prev and steps > 0:
            self.pointer = self.pointer.prev
            steps -= 1
        return self.pointer.url
        

    def forward(self, steps: int) -> str:
        while self.pointer.next and steps > 0:
            self.pointer = self.pointer.next
            steps -= 1
        return self.pointer.url
