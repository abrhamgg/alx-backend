#!/usr/bin/env python3
"""0-simple_helper_function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ that takes two integer arguments page and page_size"""
    if not page or not page_size:
        return
    start_index = (page * page_size)-page_size
    end_index = page * page_size
    return start_index, end_index
