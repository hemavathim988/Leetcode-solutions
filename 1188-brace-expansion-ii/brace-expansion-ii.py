class Solution:
    def braceExpansionII(self, expression):
        def parse(i):
            res = set()
            cur = {""}

            while i < len(expression) and expression[i] != '}':
                if expression[i] == '{':
                    sub, i = parse(i + 1)
                elif expression[i].isalpha():
                    sub = {expression[i]}
                    i += 1
                else:
                    i += 1
                    continue

                cur = {a + b for a in cur for b in sub}

                if i < len(expression) and expression[i] == ',':
                    res |= cur
                    cur = {""}
                    i += 1

            res |= cur

            if i < len(expression) and expression[i] == '}':
                i += 1

            return res, i

        result, _ = parse(0)
        return sorted(result)