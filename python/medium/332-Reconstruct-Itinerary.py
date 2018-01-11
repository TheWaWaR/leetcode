#!/usr/bin/env python
# coding: utf-8


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        tmap = {}
        for ticket in tickets:
            frm, to = ticket
            if frm not in tmap:
                tmap[frm] = []
            tmap[frm].append(to)
        print tmap

        def collect(head, length):
            start = head[-1]
            if start not in tmap:
                return []
            options = sorted(tmap[start])
            results = []
            for option in options:
                result = head[:]
                result.append(option)
                for tail in collect(result, length-1):
                    if len(tail) == length - 1:
                        result.extend(tail)
                results.append(result)
        return sorted(collect(['JFK'], len(tickets)))[0]


if __name__ == '__main__':
    for tickets, expect in [
            ([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]],
             ["JFK", "MUC", "LHR", "SFO", "SJC"]),
            ([["JFK", "SFO"],
              ["JFK", "ATL"],
              ["SFO", "ATL"],
              ["ATL", "JFK"],
              ["ATL", "SFO"]],
             ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"])
    ]:
        print 'Tickets={}, Expect={}'.format(tickets, expect)
        rv = Solution().findItinerary(tickets)
        print 'Result={}'.format(rv)
        # assert rv == expect
    print '>>> [DONE]'
