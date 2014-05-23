class konto(object):

    zinsen=1.03

    def __init__(self, start):
        self.geld = start

    def abheben(self, geld):
        if self.geld-geld < 0:
            raise ValueError("Zu viel abgehoben")
        else:
            self.geld -= geld

    def getZinsen(self):
        return self.geld*self.__class__.zinsen

    zinsen = property(get_zinsen, set_zinsen)

Konto = konto(200)
Konto.abheben(100)
print konto.zinsen
print Konto.getZinsen()
Konto.abheben(1000000)
