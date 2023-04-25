class resp():
    status = 200
    message = ''
    data = []
    def __init__(self, message, status, data):
        self.message = message
        self.status = status
        self.data = data