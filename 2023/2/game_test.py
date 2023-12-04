import unittest
from game import Game, Round, Match, Bag


class TestGame(unittest.TestCase):
    def test_round_feasible(self):
        round = Round({"red": 4, "blue": 3, "green": 0})
        bag = Bag({"red": 12, "blue": 14, "green": 13})
        self.assertTrue(round.isPossible(bag), "Round should be possible")

    def test_round_notFeasible(self):
        round = Round({"red": 20, "blue": 6, "green": 8})
        bag = Bag({"red": 12, "blue": 14, "green": 13})
        self.assertTrue(not round.isPossible(bag), "Round should be impossible")

    def test_game_feasible(self):
        game = Game(
            1,
            [
                Round({"red": 4, "blue": 3, "green": 0}),
                Round({"red": 1, "blue": 6, "green": 2}),
                Round({"red": 0, "blue": 0, "green": 2}),
            ],
        )
        bag = Bag({"red": 12, "blue": 14, "green": 13})
        self.assertTrue(game.isPossible(bag), "Game should be possible")

    def test_game_notFeasible(self):
        game = Game(
            1,
            [
                Round({"red": 20, "blue": 6, "green": 8}),
                Round({"red": 4, "blue": 5, "green": 13}),
                Round({"red": 1, "blue": 0, "green": 5}),
            ],
        )
        bag = Bag({"red": 12, "blue": 14, "green": 13})
        self.assertTrue(not game.isPossible(bag), "Game should not be possible")

    def test_match_score(self):
        match = Match.loadstr(
            """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
        )
        bag = Bag({"red": 12, "blue": 14, "green": 13})
        self.assertEqual(match.score(bag), 8, "Match score should be 8")

    def test_game_power(self):
        game = Game(
            1,
            [
                Round({"red": 4, "blue": 3, "green": 0}),
                Round({"red": 1, "blue": 6, "green": 2}),
                Round({"red": 0, "blue": 0, "green": 2}),
            ],
        )
        min_bag = game.minimum_bag()
        self.assertEqual(min_bag.power(), 48, "Game power should be 48")

    def test_match_power(self):
        match = Match.loadstr(
            """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
        )
        self.assertEqual(match.power(), 2286, "Match power should be 2286")


if __name__ == "__main__":
    unittest.main()
