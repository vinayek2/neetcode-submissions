class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {


        //matrix 

        for (int i = 0; i < matrix.size(); i++){
            for(int j = 0; j < matrix[i].size(); j++){
                int left = 0; 
                int right = matrix[i].size(); 
                while(left <= right){
                    int middle = (right + left)/2; 
                    if (matrix[i][middle] < target){

                        left = middle + 1; 
                        
                    } else if(matrix[i][middle] > target){

                        right = middle - 1; 

                    } else if(matrix[i][middle] == target){
                        return true; 
                    }

                }
            }
        }
        return false; 

        
        
    }
};
