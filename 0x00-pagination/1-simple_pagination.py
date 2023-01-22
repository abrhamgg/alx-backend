#!/usr/bin/env python3
"""1-simple_pagination"""
from typing import List
import math
import csv
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get_page that takes two integer arguments page with default value
        1 and page_size with default value 10"""
        assert type(page) is int
        assert type(page_size) is int
        assert page_size > 0
        assert page > 0
        indexes = index_range(page, page_size)
        dataset = self.dataset()
        try:
            return dataset[indexes[0]:indexes[1]+1]
        except IndexError:
            return []
