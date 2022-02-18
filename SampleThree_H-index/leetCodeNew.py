def hIndex(self, citations: list[int]) -> int:
    l = len(citations)
    citations.sort(reverse=True)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i