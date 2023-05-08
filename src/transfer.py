class Transfer:
    def __init__(self, origin, destination, value, description):
        self.origin = origin
        self.destination = destination
        self.value = value
        self.description = description

    def execute(self):
      self.origin.transfer(self.destination, self.value, self.description)
