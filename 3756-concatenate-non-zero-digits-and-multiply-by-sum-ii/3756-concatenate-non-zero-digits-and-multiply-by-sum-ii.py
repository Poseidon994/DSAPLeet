class Solution(object):
    def sumAndMultiply(self, s, queries):
        MOD = 10**9 + 7
        n_len = len(s)

        val = [0] * (n_len + 1)
        nz_count = [0] * (n_len + 1)
        prefix_sum = [0] * (n_len + 1)
        pow10 = [1] * (n_len + 1)

        for i in range(n_len):
            d = int(s[i])
            if d != 0:
                val[i+1] = (val[i] * 10 + d) % MOD
                nz_count[i+1] = nz_count[i] + 1
            else:
                val[i+1] = val[i]
                nz_count[i+1] = nz_count[i]
            prefix_sum[i+1] = prefix_sum[i] + d
            pow10[i+1] = (pow10[i] * 10) % MOD

        answer = []
        for l, r in queries:
            digit_sum = prefix_sum[r+1] - prefix_sum[l]
            cnt = nz_count[r+1] - nz_count[l]
            n = (val[r+1] - val[l] * pow10[cnt]) % MOD
            answer.append((n * digit_sum) % MOD)
        return answer