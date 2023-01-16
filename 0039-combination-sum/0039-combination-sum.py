class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res =[]
        temp=[]
        def backTrack(i,total):
            if total == 0:
                res.append(temp.copy())
                return
            if  total<0 or i==len(candidates):
                return
            backTrack(i+1,total)
            temp.append(candidates[i])
            backTrack(i,total-candidates[i])
            temp.pop()
        backTrack(0,target)
        return res
    '''
     res =[]
        def backTrack(target,i,m,temp):
            if target == 0:
                res.append(temp.copy())  # copy because temp may change in the future so it will be modified
                return
            if  target<0 or i==len(candidates):
                return
            temp.append(candidates[i])
            backTrack(target - candidates[i],i,len(candidates),temp)
            temp.pop()
            backTrack(target,i+1,len(candidates),temp)
        backTrack(target,0,len(candidates),[])
        return res
    '''
    '''
    all values are positive
     2+2+3 = 7
     3+2+2 = 7
     they arenot unique so we add only one of them .
     that means we need combinations not permuations 
     height of the tree at most will be equal to the target so time complexity is O(2^t)
    '''
    '''
    check if there is a sum that equal to target 
    
    canSum ( targetSum , numbers) 
        if targetSum ==0 :
            return True
        if targetSum <0:
            return False
        for num in numbers:
            remainder = targetSum - num
            if canSum(remainder,numbers , memo) === True:
            return True
        return False # that will return if thereisnot exist targetsum
        
        #memoization solution 
    canSum ( targetSum , numbers) 
            if targetSum in memo:
            return memo[targetSum]
            if targetSum ==0 :
                return True
            if targetSum <0:
                return False
            for num in numbers:
                remainder = targetSum - num
                if canSum(remainder,numbers , memo) === True:
                    memo[targetSum] = True
                    return True
            memo[targetSum] = False
            return False
    '''
    '''
    how many ways to form number of four digits from 1 to 6 without repetition
     = 6*5*4*3 = 6!/2!
     generally p(n,k) = n!/(n-k)!
     if repetition allowed then result will be 6^4
     for permutations order matter  {1,2,5} != {2,5,1}
     for combinations order doesnot matter {1,2,5} == {2,5,1}
      if we have 4 students how many ways to select two students 
      C(4,2) => we used combinations because order doesnot matter 
      C = p/k! = n!/k!(n-k)!
      rule of symmetry 
      c(n,k) = c(n,n-k)
    '''