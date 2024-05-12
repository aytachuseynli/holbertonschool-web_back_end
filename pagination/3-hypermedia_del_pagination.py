#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return hypermedia pagination info for the given index.
        """
        assert index is None or (isinstance(index, int) and 0 <= index < len(self.indexed_dataset())), \
            "index must be None or an integer in the valid range"
        assert isinstance(page_size, int) and page_size > 0, "page_size must be a positive integer"

        dataset = self.indexed_dataset()
        if index is None:
            index = 0
        next_index = index + page_size

        return {
            "index": index,
            "data": [dataset[i] for i in range(index, min(next_index, len(dataset)))],
            "page_size": page_size,
            "next_index": next_index if next_index < len(dataset) else None
        }


if __name__ == "__main__":
    # Test cases
    server = Server()

    print(server.get_hyper_index(300000, 100))  # Should raise AssertionError

    index = 3
    page_size = 2

    print("Nb items: {}".format(len(server.indexed_dataset())))

    # 1- request first index
    res = server.get_hyper_index(index, page_size)
    print(res)

    # 2- request next index
    print(server.get_hyper_index(res.get('next_index'), page_size))

    # 3- remove the first index
    del server._Server__indexed_dataset[res.get('index')]
    print("Nb items: {}".format(len(server._Server__indexed_dataset)))

    # 4- request again the initial index -> the first data retrieves is not the same as the first request
    print(server.get_hyper_index(index, page_size))

    # 5- request again initial next index -> same data page as the request 2-
    print(server.get_hyper_index(res.get('next_index'), page_size))
