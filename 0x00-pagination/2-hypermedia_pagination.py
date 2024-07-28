#!/usr/bin/env python3
import csv
import math
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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Takes 2 integer arguments and returns requested page from the dataset
        Args:
            page (int): required page number. must be a positive integer
            page_size (int): number of records per page. must be a +ve integer
        Return:
            list of lists containing required data from the dataset
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        dataset = self.dataset()
        data_length = len(dataset)
        try:
            index = index_range(page, page_size)
            return dataset[index[0]:index[1]]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
                Returns a page of the dataset.
        Args:
            page (int): The page number.
            page_size (int): The page size.
        Returns:
            List[List]: The page of the dataset.
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        hyper = {}
        dataset = self.dataset()
        data = self.get_page(page, page_size)
        current_size = len(data)
        total_pages = len(dataset) // page_size

        next_page = page + 1 if page < total_pages else None
        previous_page = page - 1 if page > 1 else None
        hyper = {"page_size": current_size,
                 "page": page,
                 "data": data,
                 "next_page": next_page,
                 "prev_page": previous_page,
                 "total_pages": total_pages
                 }
        return hyper
