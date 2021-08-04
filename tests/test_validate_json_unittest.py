import unittest
from tests.constant_test_cases import PUBLIC_TEST_CASES
from validate import validate_json  # Импорт функции calculate из домашнего задания
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class CalculateTestCase(unittest.TestCase):
    """Такие же тестовые случаи, но реализованные через unittest."""

    def setUp(self):
        """Начальные условия для тестов."""
        self.all_test_cases = PUBLIC_TEST_CASES

    def test_validate_json(self):
        """Тесирование функции валидации по Json схеме."""
        for test_case in self.all_test_cases:
            test_input = test_case.get("test_input")
            expected = test_case.get("expected")

            self.assertEqual(validate_json(test_input), expected)
