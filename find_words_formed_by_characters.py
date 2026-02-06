class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        

        _chars = Counter(chars)

        count = 0
        for word in words:
            _word = Counter(word)
            print(_chars,_word)
            if _word <= _chars:
                count += len(word)
        return count
