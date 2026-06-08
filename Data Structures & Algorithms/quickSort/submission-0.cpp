// Definition for a Pair
// class Pair {
// public:
//     int key;
//     string value;
//
//     Pair(int key, string value) : key(key), value(value) {}
// };
class Solution {
public:
    vector<Pair> quickSort(vector<Pair>& pairs) {
        return quickSortHelper(0, pairs.size()-1, pairs); 
    }

    vector<Pair> quickSortHelper(int start, int end, vector<Pair>& pairs){
        if(end - start + 1 <= 1){
            return pairs; 
        }

        Pair pivot = pairs[end]; 
        int left = start; 
        
        for(int i = start; i < end; i++){
           if(pivot.key > pairs[i].key) {
            Pair tmp = pairs[left]; 
            pairs[left] = pairs[i]; 
            pairs[i] = tmp;
            left++; 
           }
        }

        pairs[end] = pairs[left]; 
        pairs[left] = pivot; 
        
        quickSortHelper(start, left-1, pairs); 
        quickSortHelper(left+1, end, pairs);
        return pairs; 
    }
};
