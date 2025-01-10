class Solution {
    public double findMedianSortedArrays(int[] a, int[] b) {
        
        //Swap if a size is > b size
        if(a.length > b.length){
            return findMedianSortedArrays(b,a);
        }
        
        int alength = a.length;
        int blength = b.length;
        int total =  (a.length + b.length);
        
        int high = alength;
        int low = 0;
        
        while(low <= high){
            //amid and bmid are partition points. 
            //elements on both sides will be 
            //a[amid - 1 ] | a[amid]
            //b[bmid - 1 ] | b[bmid]
            int amid = low + (high-low)/2;
            int bmid = (total+1)/2 - amid;
            
            //Checking boundary conditions
            int a1 = (amid == 0) ? Integer.MIN_VALUE : a[amid -1];
            int b1 = (bmid == 0) ? Integer.MIN_VALUE : b[bmid -1];
            
            int a2 = (amid == alength) ? Integer.MAX_VALUE : a[amid];
            int b2 = (bmid == blength) ? Integer.MAX_VALUE : b[bmid];
            
            if(a1 <= b2 && a2 >= b1){

                double median  = 0.0;
                int lMax = Math.max(a1,b1);
                int rMin = Math.min(a2,b2);
                
                if(total%2 == 0){
                   median = (lMax + rMin)/2.0 ;
                }
                else{
                    median = lMax;
                }
                return median;
            }
            else if(a2 < b1){
                low = amid +1;
            }
            else{
                high = amid -1;
            }
        }
        return 0.0;
    }
}
