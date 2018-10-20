class PrintHelper:

    def __init__(self, text):
        self.text = text

    def removeAPPLY(self):
        self.text = self.text.replace("APPLY", "")
        return self

    def removeFULLTIME(self):
        self.text = self.text.replace("FULL-TIME", "")
        return self