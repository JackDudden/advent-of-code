"""
Advent of Code - Day 2
https://adventofcode.com/2023/day/2
"""

import operator
from functools import reduce


class Bag:
    def __init__(self, colours: dict[str, int]):
        self.colours = colours

    def power(self) -> int:
        return reduce(operator.mul, self.colours.values(), 1)


class Round:
    def __init__(self, colours: dict[str, int]):
        self.colours = colours

    def isPossible(self, bag: Bag) -> bool:
        for k, v in self.colours.items():
            if v > bag.colours.get(k, 0):
                return False
        return True

    @classmethod
    def loadstr(cls, input: str):
        colour_info = input.strip().split(",")
        colours = {}
        for colour in colour_info:
            num_colour_split = colour.strip().split(" ")
            colours[num_colour_split[1]] = int(num_colour_split[0])
        return Round(colours)


class Game:
    def __init__(self, id: int, rounds: list[Round]):
        self.id = id
        self.rounds = rounds

    def isPossible(self, bag: Bag) -> bool:
        for round in self.rounds:
            if not round.isPossible(bag):
                return False
        return True

    def minimum_bag(self) -> Bag:
        colours = {}
        for round in self.rounds:
            for k, v in round.colours.items():
                if colours.get(k, 0) < v:
                    colours[k] = v
        return Bag(colours)

    @classmethod
    def loadstr(cls, input: str):
        split = input.split(":")
        game_info, round_info = split[0], split[1]

        id = int(game_info.split(" ")[1])

        rounds = [Round.loadstr(x) for x in round_info.split(";")]
        return Game(id, rounds)


class Match:
    def __init__(self, games: list[Game]):
        self.games = games

    def score(self, bag: Bag) -> int:
        sum = 0
        for game in self.games:
            if game.isPossible(bag):
                sum += game.id

        return sum

    def power(self) -> int:
        return sum(x.minimum_bag().power() for x in self.games)

    @classmethod
    def loadstr(cls, input: str):
        games = [Game.loadstr(x) for x in input.splitlines()]
        return cls(games)
