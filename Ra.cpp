#include<iostream>
#include<math.h>
#include<stdio.h>
using namespace std;

class Solution{
public:
	void rotate(int nums[], int n, int k){
		k = k % n;
		int ans[n];
		int i = 0;
		for(int p = (n-k); p < n; p++){
			ans[i++] = nums[p];
		}
		for(int p = 0; p < (n-k); p++){
			ans[i++] = nums[p];
		}
		for(int i=0; i < n; i++){
			nums[i] = ans[i];
			cout<<nums[i]<<endl;
		}
	}
};

int main(){
	int nums[] ={1,2,3,4,5,6,7,8,9,10,11,12,12,1,1,1,1,1,1,1,1};
	Solution s;
	s.rotate(nums, 21, 3);
	return 0;
}
