import unittest
from random import randint
from DSA.algos.recursive.merge_sort import merge_sort


class MergeSort(unittest.TestCase):

    def test_merge_sort_recursive(self):
        failures = list()
        for test_number in range(100):
            arr_length = randint(1, 1000)
            random_list = list()
            for _ in range(arr_length):
                element = randint(1, 10000)
                random_list.append(element)
            sorted_array = merge_sort(random_list)
            system_sorted = sorted(random_list)
            if sorted_array != system_sorted:
                failures.append("Failed")

        self.assertEqual([], failures)

if __name__ == "__main__":
    unittest.main()






