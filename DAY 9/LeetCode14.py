def LongestCommonPrefix(self,strs):
    prefix=str[0]
# ["Flower","Flow","Flight"]   
    for s in str[1:]:
        while not s.startswith(prefix):
            prefix=prefix[:-1]


            if prefix == "":
                return ""
            
            
            
    return prefix  

# main 
prefix = ["flower","flow","flight"]
print(LongestCommonPrefix(prefix))
