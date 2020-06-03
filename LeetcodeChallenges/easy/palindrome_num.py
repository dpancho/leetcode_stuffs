# To check if number inputed is the same forwards as it is backwards AKA palindrome


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # similar to reverse an int, just compare at the end.
        # take x and store into separate array
        # reverse that number
        # is num in array == x?

        # if its a negative number, will always be false
        if x < 0:
            return False
        else:
            store = str(x)
            reversed_num = int(store[::-1])

            if x == reversed_num:
                return True
            else:
                return False


# isPalindrome(x)
