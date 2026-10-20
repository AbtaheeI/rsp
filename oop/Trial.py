class Phone:
    def __init__(self, model):
        self.model = model
        self._battery = 100
        self._apps = []

    def use(self, minutes):
        self._battery -= (minutes//10)
        if self._battery < 0:
            self._battery = 0

    def charge(self):
        self._battery = 100

    def install(self, app):
        self._apps.append(app)

    def status(self):
        return f"{self.model}: {self._battery}% battery, {len(self._apps)} apps" 


phone = Phone("iPhone 15")
phone.install("Spotify")
phone.install("Maps")
phone.use(150)
print(phone.status())
phone.use(2000)
print(phone.status())
phone.charge()
print(phone.status())
phone._battery = 500
print(phone.status())