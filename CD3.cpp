#include<iostream>
using namespace std;

class Solution{
public:
	bool f(vector<int>& nums, int k, int t){
		long long tmp;
		if(k<1 || t<0)
			return false;
		multiset<long long> setbox;
		setbox.insert(nums[0]);
		for(int i = 1; i < nums.size(); i++){
			setbox.insert(nums[i]);
			auto it = setbox.lower_bound(nums[i] - t);
			if(it!=setbox.end()){
				long long tmp = abs(*it - num[i])	
			}
		}

	}
};
