from statement import Statement
from movie import ChildrensMovie, NewReleaseMovie, RegularMovie

class TestVideoStore:
    statement = Statement('Fred')
    new_release_1 = NewReleaseMovie('New Release 1')
    new_release_2 = NewReleaseMovie('New Release 2')
    childrens = ChildrensMovie('Childrens')
    regular_1 = RegularMovie('Plan 9 from Outer Space')
    regular_2 = RegularMovie('8 1/2')
    regular_3 = RegularMovie('Eraserhead')

    def setup_method(self, _method):
        self.statement.clear()

class TestStatementTotals(TestVideoStore):
    def test_single_new_release(self):
        self.statement.add_rental(self.new_release_1, 3)
        assert self.statement.frequent_renter_points == 2
        assert self.statement.amount_owed == 9

    def test_dual_new_release(self):
        self.statement.add_rental(self.new_release_1, 3)
        self.statement.add_rental(self.new_release_2, 3)
        assert self.statement.frequent_renter_points == 4
        assert self.statement.amount_owed == 18

    def test_single_childrens(self):
        self.statement.add_rental(self.childrens, 3)
        assert self.statement.frequent_renter_points == 1
        assert self.statement.amount_owed == 1.5

    def test_multiple_regular(self):
        self.statement.add_rental(self.regular_1, 1)
        self.statement.add_rental(self.regular_2, 2)
        self.statement.add_rental(self.regular_3, 3)
        assert self.statement.frequent_renter_points == 3
        assert self.statement.amount_owed == 7.5

class TestStatementFormatting(TestVideoStore):
    def test_multiple_regular(self):
        self.statement.add_rental(self.regular_1, 1)
        self.statement.add_rental(self.regular_2, 2)
        self.statement.add_rental(self.regular_3, 3)
        assert (
                'Rental Record for Fred\n'
                '\tPlan 9 from Outer Space\t2\n'
                '\t8 1/2\t2\n'
                '\tEraserhead\t3.5\n'
                'You owed 7.5\nYou earned 3 frequent renter points\n'
        ) == self.statement.generate()

# vim:et:sw=4:sts=4:
