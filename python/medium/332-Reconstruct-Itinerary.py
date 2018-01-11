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
                tmap[frm] = {}
            if to not in tmap[frm]:
                tmap[frm][to] = 0
            tmap[frm][to] += 1

        # print len(tickets), tmap

        def check_used(head, frm, to):
            if len(head) < 2:
                return True
            count = tmap.get(frm, {}).get(to, 0)
            for i in range(len(head) - 1):
                if head[i] == frm and head[i+1] == to:
                    # print 'check_circle faild:', head, frm, to
                    count -= 1
                    if count == 0:
                        return False
            return True

        info = {'last': None}

        def collect(head):
            if info['last'] is not None and info['last'] < head:
                return
            if len(head) == len(tickets) + 1:
                # print 'head:', head
                if info['last'] is None or info['last'] > head:
                    info['last'] = head
                return

            start = head[-1]
            if start not in tmap:
                return
            for option in sorted(tmap[start]):
                if not check_used(head, start, option):
                    continue
                # print 'new:', len(head) + 1, head[:] + [option]
                collect(head[:] + [option])
        collect(['JFK'])
        # print 'Results:', results
        return info['last']


if __name__ == '__main__':
    for tickets, expect in [
            ([["AXA","EZE"],["EZE","AUA"],["ADL","JFK"],["ADL","TIA"],["AUA","AXA"],["EZE","TIA"],["EZE","TIA"],["AXA","EZE"],["EZE","ADL"],["ANU","EZE"],["TIA","EZE"],["JFK","ADL"],["AUA","JFK"],["JFK","EZE"],["EZE","ANU"],["ADL","AUA"],["ANU","AXA"],["AXA","ADL"],["AUA","JFK"],["EZE","ADL"],["ANU","TIA"],["AUA","JFK"],["TIA","JFK"],["EZE","AUA"],["AXA","EZE"],["AUA","ANU"],["ADL","AXA"],["EZE","ADL"],["AUA","ANU"],["AXA","EZE"],["TIA","AUA"],["AXA","EZE"],["AUA","SYD"],["ADL","JFK"],["EZE","AUA"],["ADL","ANU"],["AUA","TIA"],["ADL","EZE"],["TIA","JFK"],["AXA","ANU"],["JFK","AXA"],["JFK","ADL"],["ADL","EZE"],["AXA","TIA"],["JFK","AUA"],["ADL","EZE"],["JFK","ADL"],["ADL","AXA"],["TIA","AUA"],["AXA","JFK"],["ADL","AUA"],["TIA","JFK"],["JFK","ADL"],["JFK","ADL"],["ANU","AXA"],["TIA","AXA"],["EZE","JFK"],["EZE","AXA"],["ADL","TIA"],["JFK","AUA"],["TIA","EZE"],["EZE","ADL"],["JFK","ANU"],["TIA","AUA"],["EZE","ADL"],["ADL","JFK"],["ANU","AXA"],["AUA","AXA"],["ANU","EZE"],["ADL","AXA"],["ANU","AXA"],["TIA","ADL"],["JFK","ADL"],["JFK","TIA"],["AUA","ADL"],["AUA","TIA"],["TIA","JFK"],["EZE","JFK"],["AUA","ADL"],["ADL","AUA"],["EZE","ANU"],["ADL","ANU"],["AUA","AXA"],["AXA","TIA"],["AXA","TIA"],["ADL","AXA"],["EZE","AXA"],["AXA","JFK"],["JFK","AUA"],["ANU","ADL"],["AXA","TIA"],["ANU","AUA"],["JFK","EZE"],["AXA","ADL"],["TIA","EZE"],["JFK","AXA"],["AXA","ADL"],["EZE","AUA"],["AXA","ANU"],["ADL","EZE"],["AUA","EZE"]],
             ['JFK', 'ADL', 'ANU', 'ADL', 'ANU', 'AUA', 'ADL', 'AUA', 'ADL', 'AUA', 'ANU', 'AXA', 'ADL', 'AUA', 'ANU', 'AXA', 'ADL', 'AXA', 'ADL', 'AXA', 'ANU', 'AXA', 'ANU', 'AXA', 'EZE', 'ADL', 'AXA', 'EZE', 'ADL', 'AXA', 'EZE', 'ADL', 'EZE', 'ADL', 'EZE', 'ADL', 'EZE', 'ANU', 'EZE', 'ANU', 'EZE', 'AUA', 'AXA', 'EZE', 'AUA', 'AXA', 'EZE', 'AUA', 'AXA', 'JFK', 'ADL', 'EZE', 'AUA', 'EZE', 'AXA', 'JFK', 'ADL', 'JFK', 'ADL', 'JFK', 'ADL', 'JFK', 'ADL', 'TIA', 'ADL', 'TIA', 'AUA', 'JFK', 'ANU', 'TIA', 'AUA', 'JFK', 'AUA', 'JFK', 'AUA', 'TIA', 'AUA', 'TIA', 'AXA', 'TIA', 'EZE', 'AXA', 'TIA', 'EZE', 'JFK', 'AXA', 'TIA', 'EZE', 'JFK', 'AXA', 'TIA', 'JFK', 'EZE', 'TIA', 'JFK', 'EZE', 'TIA', 'JFK', 'TIA', 'JFK', 'AUA', 'SYD']),

            ([["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]],
             ['JFK', 'AXA', 'AUA', 'ADL', 'ANU', 'AUA', 'ANU', 'EZE', 'ADL', 'EZE', 'ANU', 'JFK', 'AXA', 'EZE', 'TIA', 'AUA', 'AXA', 'TIA', 'ADL', 'EZE', 'HBA']),

            ([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]],
             ["JFK", "MUC", "LHR", "SFO", "SJC"]),

            ([["JFK", "SFO"],
              ["JFK", "ATL"],
              ["SFO", "ATL"],
              ["ATL", "JFK"],
              ["ATL", "SFO"]],
             ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]),

            ([["MUC", "LHR"],
              ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]],
             ["JFK", "MUC", "LHR", "SFO", "SJC"]),

            ([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]],
             ['JFK', 'NRT', 'JFK', 'KUL']),

            ([["EZE", "AXA"],
              ["TIA", "ANU"],
              ["ANU", "JFK"],
              ["JFK", "ANU"],
              ["ANU", "EZE"],
              ["TIA", "ANU"],
              ["AXA", "TIA"],
              ["TIA", "JFK"],
              ["ANU", "TIA"],
              ["JFK", "TIA"]],
             ["JFK", "ANU", "EZE", "AXA", "TIA",
              "ANU", "JFK", "TIA", "ANU", "TIA", "JFK"]),
    ]:
        print 'Tickets={}, Expect={}'.format(tickets, expect)
        rv = Solution().findItinerary(tickets)
        print 'Result={}'.format(rv)
        assert rv == expect
        print '=' * 40 + '\n'
    print '>>> [DONE]'
