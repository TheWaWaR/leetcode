#!/usr/bin/env python
# coding: utf-8


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        parts = []
        last_char = None
        for c in p:
            if c == '*':
                if not parts or parts[-1] != (last_char, '*'):
                    parts.append((last_char, '*'))
                last_char = None
            else:
                if last_char is not None:
                    parts.append((last_char, None))
                last_char = c
        if last_char is not None:
            parts.append((last_char, None))

        def log(s, level=0):
            pass
            # print '<{}>{}{}'.format(level, '|   '*level, s)

        def check_rest(idx, s, part_idx, parts):
            if idx == len(s):
                while part_idx < len(parts):
                    c, mode = parts[part_idx]
                    if mode != '*':
                        return False
                    part_idx += 1
                return True
            else:
                return False

        def match(s, parts, level):
            log('match(s={}, parts={})'.format(s, parts), level)
            idx = 0
            part_idx = 0
            while part_idx < len(parts) and idx < len(s):
                c, mode = parts[part_idx]
                log('c={}, mode={}, idx={}, s[idx]={}'.format(c, mode, idx, s[idx]), level)
                if mode is None:
                    if c in (s[idx], '.'):
                        idx += 1
                    else:
                        return False
                else:
                    idx_tmp = 0
                    while idx + idx_tmp < len(s):
                        if match(s[idx+idx_tmp:], parts[part_idx+1:], level+1):
                            log('>> True', level+1)
                            return True
                        else:
                            log('>> False', level+1)
                        if c not in (s[idx+idx_tmp], '.'):
                            return False
                        idx_tmp += 1
                    return check_rest(idx+idx_tmp, s, part_idx, parts)
                part_idx += 1
            log('idx={}, idxMax={}'.format(idx, len(s)), level)
            return check_rest(idx, s, part_idx, parts)

        return match(s, parts, 0)
