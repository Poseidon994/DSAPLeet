class Solution(object):
    def findSubstring(self, s, words):
        word_len = len(words[0])
        num_words = len(words)
        window_len = word_len * num_words
        word_count = Counter(words)
        n = len(s)
        res = []

        for offset in range(word_len):
            low = offset
            window_count = Counter()
            num_matched = 0  # chunks currently in window that belong to word_count

            # slide idx by word_len each step, starting at offset
            for idx in range(offset, n - word_len + 1, word_len):
                word = s[idx:idx + word_len]

                if word in word_count:
                    window_count[word] += 1
                    num_matched += 1

                    # window has too many chunks -> shrink from left
                    while window_count[word] > word_count[word]:
                        left_word = s[low:low + word_len]
                        window_count[left_word] -= 1
                        num_matched -= 1
                        low += word_len

                    # window has exactly num_words chunks -> check
                    if num_matched == num_words:
                        res.append(low)
                        # shrink by one chunk from left to slide forward
                        left_word = s[low:low + word_len]
                        window_count[left_word] -= 1
                        num_matched -= 1
                        low += word_len
                else:
                    # invalid chunk -> whole window resets
                    window_count.clear()
                    num_matched = 0
                    low = idx + word_len

        return res