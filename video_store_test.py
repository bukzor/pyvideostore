from expecter import expect
import unittest

from statement import Statement
from movie import Movie
from rental import Rental


class VideoStoreTest(unittest.TestCase):

    def setUp(self):
        self.statement = Statement('Customer Name')
        self.new_release_a = Movie('New Release A', Movie.NEW_RELEASE)
        self.new_release_b = Movie('New Release B', Movie.NEW_RELEASE)
        self.childrens = Movie('Childrens', Movie.CHILDRENS)
        self.regular_a = Movie('Regular A', Movie.REGULAR)
        self.regular_b = Movie('Regular B', Movie.REGULAR)
        self.regular_c = Movie('Regular C', Movie.REGULAR)

    def test_single_new_release_statement_totals(self):
        self.statement.add_rental(Rental(self.new_release_a, 3))
        self.statement.generate()
        expect(self.statement.total_amount) == 9
        expect(self.statement.frequent_renter_points) == 2

    def test_dual_new_release_statement_totals(self):
        self.statement.add_rental(Rental(self.new_release_a, 3))
        self.statement.add_rental(Rental(self.new_release_b, 3))
        self.statement.generate()
        expect(self.statement.total_amount) == 18
        expect(self.statement.frequent_renter_points) == 4

    def test_single_childrens_statement_totals(self):
        self.statement.add_rental(Rental(self.childrens, 3))
        self.statement.generate()
        expect(self.statement.total_amount) == 1.5
        expect(self.statement.frequent_renter_points) == 1

    def test_multiple_regular_statement_totals(self):
        self.statement.add_rental(Rental(self.regular_a, 1))
        self.statement.add_rental(Rental(self.regular_b, 2))
        self.statement.add_rental(Rental(self.regular_c, 3))
        self.statement.generate()
        expect(self.statement.total_amount) == 7.5
        expect(self.statement.frequent_renter_points) == 3

    def test_multiple_regular_statement_formatting(self):
        self.statement.add_rental(Rental(self.regular_a, 1))
        self.statement.add_rental(Rental(self.regular_b, 2))
        self.statement.add_rental(Rental(self.regular_c, 3))
        statement_text = self.statement.generate()
        expect('Rental Record for Customer Name\n'
               '\tRegular A\t2\n'
               '\tRegular B\t2\n'
               '\tRegular C\t3.5\n'
               'You owed 7.5\n'
               'You earned 3 frequent renter points\n') == statement_text


if __name__ == '__main__':
    unittest.main()
