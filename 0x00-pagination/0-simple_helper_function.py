#!/usr/bin/python3
"""
Helper function that return index range of a page
"""

def index_range(page, page_size):
    """
    Args:
        page (int): page num
        page_size (int): page size
    Return:
        tuple: size two, range of indece
    """
    index = (page - 1) * page_size
    return (index, index + page_size)
