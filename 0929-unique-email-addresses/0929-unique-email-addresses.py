class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for e in emails:
            local , domain = e.split("@")
            local = local.split("+")[0]  #split returns a list of string but we need only the first element 
            local = local.replace(".","")
            unique.add((local,domain))
        return len(unique)
    
    '''
    for e in emails:
        i,local = 0 , ""
        while e[i] not in ["@","+"]
            if e[i]!="."
                local+=e[i]
            i+=1
        while e[i] != "@"
            i+=1
        domain = e[i+1:]  #it means a slice from the i+1 element to the end of the array
        unique.add((local,domain))
    return len(unique)
    '''