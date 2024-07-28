#!/usr/bin/env python3
import csv
from typing import List, Tuple


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
        """_return page content

        Args:
        page (int, optional): page number. Defaults to 1.
        page_size (int, optional): page size. Defaults to 10.

        Returns:
        List[List]: list of content of page
        """
    
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Args:
        page (int): page num
        page_size (int): page size
    Return:
        tuple: size two, range of indece
    """
    index = (page - 1) * page_size
    return (index, index + page_size)

