class longestsubstring:
    def lenghtofwindow(self,str):
        char_set=set()


        left = 0
        maxlen = 0
        for right in range(len(str)):
            current = str[right]
            while current in char_set:
                char_set.remove(str[left])
                left+=1
            char_set.add(current)
            maxlen=max(maxlen,right-left+1)  
        return maxlen
# main
l=longestsubstring()
print(l.lenghtofwindow("abcabcbb"))
