class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # store value in an array
        # take the value of that array and reverse it (using slice notation)
        # bounds check (32-bit num)
        # return correct value. Neg or Pos

        # store abolute value of the num
        store = str(abs(x))

        #::-1 will reverse contents of array
        reversed_num = int(store[::-1])

        # making sure num isnt larger than 32-bit allows
        if reversed_num > 2147483647 or reversed_num < -2147483647:
            return 0

        # return value
        if x > 0:
            return reversed_num
        else:
            return reversed_num * -1
