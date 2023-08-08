class Solution {
    public int countTriples(int n) {
        //         counter = 0
        // for i in range(1,n+1,1):
        //     for j in range(1,n+1,1):
        //             if sqrt(i*i + j*j).is_integer() and  sqrt(i*i + j*j) <=n:
        //                 counter +=1
        // return counter 
        int counter = 0;
        for(int i = n; i >= 1; i--){
            for(int j = n; j>= 1; j--){
                double c = Math.sqrt(i*i + j*j);
                if (c == (int)c && c <=n ){
                    counter+=1;
                }
            }
        }
        return counter;
    }
}