

class Movie(object):
    points = 1
    free_period = 0
    base_price = 0
    late_fee = 1.5
    def __init__(self, title, rented=0):
        self.title = title
        self.rented = rented

    @property
    def cost(self):
        if self.rented > self.free_period:
            late_charge = (self.rented - self.free_period) * self.late_fee
        else:
            late_charge = 0
        return self.base_price + late_charge

    def __str__(self):
        return '%s\t%s' % (self.title, self.cost)


class NewReleaseMovie(Movie):
    late_fee = 3

    @property
    def points(self):
        return 2 if self.rented > 1 else 1


class ChildrensMovie(Movie):
    free_period = 3
    base_price = 1.5


class RegularMovie(Movie):
    free_period = 2
    base_price = 2


# vim:et:sw=4:sts=4:
