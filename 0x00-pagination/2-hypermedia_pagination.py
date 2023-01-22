#!/usr/bin/env python3
"""1-simple_pagination"""
from typing import List, Dict
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
            if dataset[indexes[1]]:
                return dataset[indexes[0]:indexes[1]]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ method that takes the
        same arguments (and defaults) as get_page and returns a dictionary"""
        total_dataset = self.dataset()
        returned_data = self.get_page(page, page_size)
        hyper_dict = {
            'page_size': len(returned_data),
            'page': page,
            'data': self.get_page(page, page_size)
        }
        start, end = index_range(page, page_size)
        if page > 1:
            hyper_dict['prev_page'] = page - 1
        else:
            hyper_dict['prev_page'] = None
        if page < math.ceil(len(total_dataset) / page_size):
            hyper_dict['next_page'] = page + 1
        else:
            hyper_dict['next_page'] = None
        hyper_dict['total_pages'] = math.ceil(len(total_dataset) / page_size)
        return hyper_dict
