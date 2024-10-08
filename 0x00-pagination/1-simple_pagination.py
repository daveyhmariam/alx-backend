#!/usr/bin/env python3
"""
Simple pagination sample.
"""

import csv
from typing import List, Tuple


def index_range(page, page_size):
    """
    Args:
        page (int): page num
        page_size (int): page size
    Return:
        tuple: size two, range of indece
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializes a new Server instance.
        """
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
        """_return page content
        Args:
        page (int, optional): page number. Defaults to 1.
        page_size (int, optional): page size. Defaults to 10.
        Returns:
        List[List]: list of content of page
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        data = self.dataset()
        ind = index_range(page, page_size)
        start = ind[0]
        end = ind[1]
        if start > len(data):
            return []
        return data[start: end]
