import csv
from typing import List, Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Args:
        page (int): page number
        page_size (int): page size
    Returns:
        tuple: size two, range of indices
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)

class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get a page of the dataset"""
        assert isinstance(page, int) and page > 0, "Page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer"

        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)
        
        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]
