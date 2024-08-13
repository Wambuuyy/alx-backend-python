#!/usr/bin/env python3
import unittest
from utils import access_nested_map
from typing import Dict, Tuple, Union
from parameterized import parameterized



class TestAcessNestedMap(unittest.TestCase):
    """parameterized unit test to test
    different cases for access_nested_map"""

    @parameterized.expand([
        ({"a": 1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a"), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Dict, path: Tuple[str],
                               expected: Union[Dict, int]) -> None:
        """if the functions functions as intended"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
