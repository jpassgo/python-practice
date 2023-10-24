#
# 787. Cheapest Flights Within K Stops
#
# There are n cities connected by some number of flights. You are given an array flights where
# flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.
#
# You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops.
# If there is no such route, return -1.
#
# https://leetcode.com/problems/cheapest-flights-within-k-stops/
#
from typing import List


def findCheapestPrice(
    n: int, flights: List[List[int]], src: int, dst: int, k: int
) -> int:
    flight_dict = {}
    for flight in flights:
        flight_dict[flight[1]] = {"src": flight[0], "price": flight[2]}

    price_stack = []
    src_found = False

    while src_found:
        if flight_dict[dst] == src:
            src_found = True
        else:
            price_stack.append(flight_dict[dst]["price"])
            dst = flight_dict[dst]["src"]

    return sum(price_stack)
