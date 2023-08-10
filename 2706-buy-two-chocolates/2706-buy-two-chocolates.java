class Solution {
    public int buyChoco(int[] prices, int money) {
        int Min1 = 101;
        int Min2 = 101;
        for(int price:prices){
            if (price < Min1){
                int temp = Min1;
                Min1 = price;
                Min2 = temp;
            } else if(price < Min2){
                Min2 = price;
            }
        }
        int remainder = money - (Min1+Min2);
        return remainder >= 0 ? remainder : money;
    }
}