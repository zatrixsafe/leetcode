#include<iostream>
#include<vector>
#include<set>
using namespace std;

class Solution{
public:
	bool f(vector<int>& nums, int k, int t){
		if(k<1 || t<0)
			return false;
		multiset<long long> setbox;
		for(int i = 0; i < nums.size(); i++){
			if(setbox.size() >= k + 1){
				setbox.erase(setbox.find(nums[i-k-1]));
			}
			auto it = setbox.lower_bound(nums[i] - t);
			cout<<*it<<endl;
			if(it != setbox.end() && *it - nums[i] <= t){
				return true;
			}
			setbox.insert(nums[i]);
		}
		return false;
	}
};

int main(){
	Solution s;
	int nums[4] = {
		1,10,53,50
	};
	vector<int> vnums(nums, nums+4);
	bool ans = s.f(vnums, 10, 4);
	if(ans){
		cout<<"True"<<endl;
	}else{
		cout<<"False"<<endl;
	}
	return 0;
}
