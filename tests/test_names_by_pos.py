"""
test_names_by_pos.py
Elijah Ahlstrom
March 31, 2020
"""

import unittest
from problems.transformdata import TransformData


class TestNamesByPos(unittest.TestCase):
    """
    TestCase for the names_by_pos method
    """
    def setUp(self):
        """
        Define object tst of type TransformData
        """
        self.tst = TransformData()
    def test_league(self):
        self.tst.names = [
            'Stephen Curry', 'Russell Westbrook', 'Chris Paul', 'James Harden',
            'Blake Griffin', 'Gordon Hayward', 'Kyle Lowry', 'Paul George',
            'Mike Conley', 'Kevin Durant', 'Paul Millsap', 'Al Horford',
            'Damian Lillard', 'DeMar DeRozan', 'Otto Porter Jr.',
            'Jrue Holiday', 'CJ McCollum', 'Joel Embiid', 'Andrew Wiggins',
            'Bradley Beal', 'Anthony Davis', 'Hassan Whiteside',
            'Nikola Jokic', 'Steven Adams', 'Giannis Antetokounmpo',
            'Marc Gasol', 'Kevin Love', 'Chandler Parsons', 'Harrison Barnes',
            'Nicolas Batum', 'Rudy Gobert', 'Kawhi Leonard', 'DeAndre Jordan',
            'LaMarcus Aldridge', 'Serge Ibaka', 'Aaron Gordon',
            'Danilo Gallinari', 'Victor Oladipo', 'Jimmy Butler',
            'Ryan Anderson', 'Kyrie Irving', 'Jabari Parker', 'Zach LaVine',
            'Tyler Johnson', 'John Wall', 'Jeff Teague', 'George Hill',
            'Klay Thompson', 'Enes Kanter', 'Wesley Matthews'
        ]
        self.tst.salaries = [
            37457154, 35654150, 35654150, 35650150, 32088932, 31214295,
            31200000, 30560700, 30521115, 30000000, 29230769, 28928709,
            27977689, 27739975, 26011913, 25976111, 25759766, 25467250,
            25467250, 25434263, 25434263, 25434262, 24605181, 24157303,
            24157303, 24119025, 24119025, 24107258, 24107258, 24000000,
            23241573, 23114067, 22897200, 22347015, 21666667, 21590909,
            21587579, 21000000, 20445779, 20421546, 20099189, 20000000,
            19500000, 19245370, 19169800, 19000000, 19000000, 18988725,
            18622514, 18622514
        ]
        self.tst.positions = [
            'PG', 'PG', 'PG', 'PG', 'PF', 'SF', 'PG', 'SF', 'PG', 'SF', 'PF',
            'PF', 'PG', 'SG', 'SF', 'PG', 'SG', 'PF', 'SF', 'SG', 'PF', 'C',
            'C', 'C', 'PF', 'C', 'PF', 'SF', 'SF', 'SG', 'C', 'SF', 'C', 'PF',
            'PF', 'PF', 'SF', 'SG', 'SG', 'PF', 'PG', 'PF', 'PG', 'SG', 'PG',
            'PG', 'PG', 'SG', 'C', 'SG'
        ]
        actual_result=self.tst.names_by_pos()
        expected_result = {
            'PG' : ['Stephen Curry', 'Russell Westbrook', 'Chris Paul',
            'James Harden', 'Kyle Lowry', 'Mike Conley', 'Jrue Holiday',
            'Kyrie Irving', 'Zach LaVine', 'John Wall', 'Jeff Teague',
            'George Hill'],
            'PF' : ['Blake Griffin', 'Paul Millsap', 'Al Horford',
            'Joel Embiid', 'Anthony Davis', 'Giannis Antetokounmpo',
            'Kevin Love', 'LaMarcus Aldridge', 'Serge Ibaka', 'Aaron Gordon',
            'Ryan Anderson', 'Jabari Parker'],
            'SF' : ['Gordon Hayward', 'Paul George', 'Kevin Durant',
            'Otto Porter Jr.', 'Andrew Wiggins', 'Chandler Parsons',
            'Harrison Barnes', 'Kawhi Leonard', 'Danilo Gallinari'],
            'C' : ['Hassan Whiteside', 'Nikola Jokic', 'Steven Adams',
            'Marc Gasol', 'Rudy Gobert', 'DeAndre Jordan', 'Enes Kanter']
        }
        self.assertEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()
