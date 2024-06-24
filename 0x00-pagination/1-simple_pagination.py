#!/usr/bin/env python3
"""1-simple_helper_function.py"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """
    return a tuple of size two containing a
    start index and an end index
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get page"""
        assert (isinstance(page, int) and page > 0), (
            "Page must be an integer greater than 0"
        )
        assert (isinstance(page_size, int) and page_size > 0), (
            "Page size must be an integer greater than 0"
        )
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]
