class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
   
        unordered_map <int , int > m ;

        int a =-1 ;
        int b = -1 ;
             vector <int > ans ; 

        for (int i = 0 ; i < nums.size() ; i ++){
            
            a = nums [i];
            b = target - a ;

  if(m.find(b) != m.end() ){
           
                    ans.push_back (m[b]);
                     ans.push_back (i);
                return ans ;
            }

            

            if(m.find(a)==m.end()){
                m[a] = i ;
            }

          
        }
    
    return ans ;

    }
};