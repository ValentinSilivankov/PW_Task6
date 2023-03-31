# Для VSCode
import os
import sys
sys.path.append(os.getcwd())

import unittest
import pytest
from task_1 import geo_logs_rus, geo_logs, geo_logs_true


class TestGeoLogs(unittest.TestCase):
    def test_geo_logs(self):
        self.assertEqual(geo_logs_rus(geo_logs), geo_logs_true)


class TestGeoLogs2:
    @pytest.mark.parametrize(
        "geo_logs, expected",
        [
            (
                [
                    {"visit1": ["Москва", "Россия"]},
                    {"visit2": ["Дели", "Индия"]},
                    {"visit3": ["Владимир", "Россия"]},
                    {"visit4": ["Лиссабон", "Португалия"]},
                    {"visit5": ["Париж", "Франция"]},
                    {"visit6": ["Лиссабон", "Португалия"]},
                    {"visit7": ["Тула", "Россия"]},
                    {"visit8": ["Тула", "Россия"]},
                    {"visit9": ["Курск", "Россия"]},
                    {"visit10": ["Архангельск", "Россия"]},
                ],
                [
                    {"visit1": ["Москва", "Россия"]},
                    {"visit3": ["Владимир", "Россия"]},
                    {"visit7": ["Тула", "Россия"]},
                    {"visit8": ["Тула", "Россия"]},
                    {"visit9": ["Курск", "Россия"]},
                    {"visit10": ["Архангельск", "Россия"]},
                ],
            )
        ],
    )
    def test_es(self, geo_logs, expected):
        assert geo_logs_rus(geo_logs) == expected


if __name__ == "__main__":
    unittest.main()