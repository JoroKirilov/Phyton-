class Airbag:
    def __init__(self, model: str, status="Active"):
        self.model = model
        self.status = status

    def check_airbag_system(self):
        print(f"{self.model} is {self.status}")

    def deactivate_airbag(self):
        if self.status == "Deactivate":
            self.check_airbag_system()
        else:
            self.status = "Deactivate"
            self.check_airbag_system()

    def active_airbag(self):
        if self.status == "Activate":
            self.check_airbag_system()
        else:
            self.status = "Activate"
            self.check_airbag_system()
