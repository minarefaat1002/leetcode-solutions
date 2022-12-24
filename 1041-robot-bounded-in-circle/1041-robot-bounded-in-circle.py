class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # if direction changes then ther's a cycle
        # if the position changes and directions doesnot change then there'snot a cycle
        # we can run the simulation of the structions four times and if we get back at the origin that means we have a cycle 
        dirx , diry = 0 ,1 # facing the north 
        x , y = 0 , 0 
        for d in instructions :
            if d == "G":
                x,y = x+dirx , y +diry
            elif d == "L":
                dirx , diry = -1*diry , dirx # for turning left 
            else:
                dirx , diry = diry , -1* dirx # for turning right 
        return (x,y) == (0,0) or (dirx,diry)!= (0,1)