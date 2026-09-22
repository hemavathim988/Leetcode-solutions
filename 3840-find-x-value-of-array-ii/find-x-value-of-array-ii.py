class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)
        prod = [0] * (4 * n)
        cnt = [[0] * k for _ in range(4 * n)]

        def merge(p):
            l = p * 2
            r = l + 1
            prod[p] = (prod[l] * prod[r]) % k
            cnt[p] = cnt[l][:]
            for x in range(k):
                cnt[p][(prod[l] * x) % k] += cnt[r][x]

        def build(p, l, r):
            if l == r:
                v = nums[l] % k
                prod[p] = v
                cnt[p][v] = 1
                return
            m = (l + r) // 2
            build(p * 2, l, m)
            build(p * 2 + 1, m + 1, r)
            merge(p)

        def update(p, l, r, idx, val):
            if l == r:
                v = val % k
                prod[p] = v
                cnt[p] = [0] * k
                cnt[p][v] = 1
                return
            m = (l + r) // 2
            if idx <= m:
                update(p * 2, l, m, idx, val)
            else:
                update(p * 2 + 1, m + 1, r, idx, val)
            merge(p)

        def query(p, l, r, ql, qr):
            if ql <= l and r <= qr:
                return prod[p], cnt[p]

            m = (l + r) // 2

            if qr <= m:
                return query(p * 2, l, m, ql, qr)

            if ql > m:
                return query(p * 2 + 1, m + 1, r, ql, qr)

            lp, lc = query(p * 2, l, m, ql, qr)
            rp, rc = query(p * 2 + 1, m + 1, r, ql, qr)

            res = lc[:]

            for x in range(k):
                res[(lp * x) % k] += rc[x]

            return (lp * rp) % k, res

        build(1, 0, n - 1)

        ans = []

        for index, value, start, x in queries:
            update(1, 0, n - 1, index, value)
            _, c = query(1, 0, n - 1, start, n - 1)
            ans.append(c[x])

        return ans