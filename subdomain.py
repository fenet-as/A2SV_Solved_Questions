class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cp_domain_count = defaultdict(int)

        for pair in cpdomains:
            pair = pair.split()
            sub = pair[1].split(".")

            for i in range(len(sub)-1,-1,-1):
                l = list(sub[i:])
                sub_dom  = '.'.join(l)
                cp_domain_count[sub_dom] += int(pair[0])

        res = []
        for p in cp_domain_count:
            a = str(cp_domain_count[p])+" "+p
            res.append(a)
        return res
