class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if not chars:
            return 0

        count = 1
        preChar = chars[0]
        index = 0

        for i in range(1, len(chars)):
            if preChar == chars[i]:
                count += 1
            else:
                chars[index] = preChar
                index += 1
                if count > 1:
                    count_str = str(count)
                    for j in range(len(count_str)):
                        chars[index] = count_str[j]
                        index += 1
                preChar = chars[i]
                count = 1

        chars[index] = preChar
        index += 1
        if count > 1:
            count_str = str(count)
            for j in range(len(count_str)):
                chars[index] = count_str[j]
                index += 1

        # 반환값은 chars 배열의 수정 후 길이
        return index