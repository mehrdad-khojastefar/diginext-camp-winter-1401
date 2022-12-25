import unittest
import one, two, three


class TestQuestionOne(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.cases = [
            {"input": "abc", "count": 10, "want": "abcabcabca"},
            {"input": "qw", "count": 8, "want": "qwqwqwqw"},
            {"input": "qw", "count": 1, "want": "q"},
            {"input": "qwsafasfasf", "count": 2, "want": "qw"},
            {"input": "abcac", "count": 10, "want": "abcacabcac"},
        ]

    def test_question_one(self):
        # accepted cases
        for case in self.cases:
            self.assertTrue(
                case["want"] == one.repeatString(case["input"], case["count"])
            )


class TestQuestionTwo(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.cases = [
            {"input": "AABAAB", "want": 2},
            {"input": "AAAA", "want": 3},
            {"input": "BBBBB", "want": 4},
            {"input": "ABABABAB", "want": 0},
            {"input": "BABABA", "want": 0},
            {"input": "AAABBB", "want": 4},
            {"input": "BBBAAA", "want": 4},
        ]

    def test_question_two_proccess(self):
        for case in self.cases:
            self.assertTrue(two.proccess(case["input"]) == case["want"])


class TestQuestionThree(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.cases = [
            {"input": [7, 1, 3, 2, 4, 5, 6], "want": 5},
            {"input": [1, 5, 4, 3, 2], "want": 2},
            {"input": [4, 3, 2, 1], "want": 2},
        ]

    def test_question_three_minswap(self):
        for case in self.cases:
            self.assertTrue(three.minimum_swaps(case["input"]) == case["want"])
