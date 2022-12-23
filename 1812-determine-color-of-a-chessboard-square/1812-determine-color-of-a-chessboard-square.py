class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        horizontal = ord(coordinates[0]) -48
        vertical = ord(coordinates[1])-96
        if ((horizontal %2 ==0 )and (vertical % 2 ==0)) or (vertical %2 !=0 and horizontal %2 !=0):
            return False
        else :
            return True