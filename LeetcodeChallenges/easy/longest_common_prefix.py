class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # if no string, return nothing
        if len(strs) == 0:
            return ("")
        ##
        if len(strs) == 1:
            return (strs[0])

        # Starting Prefix is 1st word in list
        pref = strs[0]
        plen = len(pref)

        # loop through all other words in list. Starting from index 1 then going on
        for s in strs[1:]:
            # checks if words match, if not, shorten prefix length by 1 character.
            while pref != s[0:plen]:
                pref = pref[0:(plen-1)]
                plen -= 1

                if plen == 0:
                    return ("")

        return (pref)
