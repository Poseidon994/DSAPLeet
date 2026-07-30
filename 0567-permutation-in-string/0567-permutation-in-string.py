class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False

        needed = dict()
        for c in s1:
            needed[c] = needed.get(c, 0) + 1
        required = len(needed)

        have = dict()
        formed = 0
        low = 0

        for high in range(len(s2)):
            c = s2[high]
            have[c] = have.get(c, 0) + 1
            if c in needed:
                if have[c] == needed[c]:
                    formed += 1
                elif have[c] == needed[c] + 1:
                    formed -= 1

            if high >= len(s1):
                d = s2[low]
                if d in needed:
                    if have[d] == needed[d]:
                        formed -= 1
                    elif have[d] == needed[d] + 1:
                        formed += 1
                have[d] -= 1
                low += 1

            if formed == required:
                return True

        return False