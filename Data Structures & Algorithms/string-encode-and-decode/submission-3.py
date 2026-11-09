class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + "#" + s

        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_str = []

        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            lenght = int(s[i:j])

            start = j + 1
            end = start + lenght

            decoded_str.append(s[start: end])

            i = end

        return decoded_str
