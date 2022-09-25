class Solution {
    public int getNumberOfBacklogOrders(int[][] orders) {
        Queue<int[]> buys = new PriorityQueue<>(1, (a,b) -> b[0] - a[0]);
        Queue<int[]> sells = new PriorityQueue<>(1, (a, b) -> a[0] - b[0]);
        for (int[] order: orders){
            if (order[2] == 0){
                if (sells.isEmpty()){
                    buys.add(order);
                } else{
                    int amount = order[1];
                    while(!sells.isEmpty() && sells.peek()[0] <= order[0]){
                        int sub = Math.min(sells.peek()[1], amount);
                        sells.peek()[1] -= sub;
                        amount -= sub;
                        if (sells.peek()[1] == 0){
                            sells.remove();
                        }
                        if (amount == 0){
                            break;
                        }
                    }
                    if (amount > 0){
                        order[1] = amount;
                        buys.add(order);
                    }
                }
            } else{
                if (buys.isEmpty()){
                    sells.add(order);
                } else {
                    int amount = order[1];
                    while(!buys.isEmpty() && buys.peek()[0] >= order[0]){
                        int add = Math.min(buys.peek()[1], amount);
                        buys.peek()[1] -= add;
                        amount -= add;
                        if (buys.peek()[1] == 0){
                            buys.remove();
                        }
                        if (amount == 0){
                            break;
                        }
                    }
                    if (amount > 0){
                        order[1] = amount;
                        sells.add(order);
                    }
                }
            }
        }
        int ret = 0;
        int mod = (int)1e9+7;
        for(int[] buy : buys){
            System.out.println(buy[1]);
            ret = (ret + buy[1])%mod;
        }
        for(int[] sell : sells){
            System.out.println(sell[1]);
            ret = (ret + sell[1])%mod;
        }
        return ret;
    }
}