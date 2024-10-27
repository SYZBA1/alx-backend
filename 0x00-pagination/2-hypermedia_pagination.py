#!/usr/bin/env python3
"""Simple pagination"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns start and end index"""
    start = (page_size * page) - page_size
    end = page_size * page

    return (start, end)


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
        """Fetch data on a page based on the page number and page size"""
        rows = []

        assert (isinstance(page, int) and isinstance(page_size, int))
        assert (page > 0 and page_size > 0)

        indexes = index_range(page, page_size)  # get start and end index
        dataset = self.dataset()  # get dataset

        for row in dataset[indexes[0]: indexes[1]]:
            rows.append(row)

        return rows

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size) if data else 0

        prev_page = None if page <= 1 else page - 1
        next_page = page + 1 if page < total_pages else None

        if data == []:
            page_size = 0
        else:
            page_size = len(data)

        return {'page_size': page_size, 'page': page, 'data': data,
                'next_page': next_page, 'prev_page': prev_page,
                'total_pages': total_pages}
