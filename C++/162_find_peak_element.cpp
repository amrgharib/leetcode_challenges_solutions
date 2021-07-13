class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        
        int left=0, right = nums.size()-1;
        int mid;  
        
        while (left < right)
        {
            mid = (left + right)/2;
             
            if(right == 1){
            if (nums[0] > nums[1]) {
                return 0;
            } else {
                return 1;
            } 
        }
            
            if(nums[mid] < nums[mid+1]){
                left = mid + 1;   
            } else if (nums[mid] < nums[mid-1]) {
                right = mid - 1;
            } else {
                return mid;
            }
        }
        
        return left;
        
    }
};

class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        
        int left=0, right = nums.size()-1;
        int mid;  
        
        while (left < right)
        {
            mid = (left + right)/2;
            
            if(nums[mid] > nums[mid+1]){
                right = mid;   
            } else {
                left = mid+1;
            }
        }
        
        return left;
        
    }
};
