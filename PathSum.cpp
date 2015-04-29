/*************************************************************************
    > File Name: PathSum.cpp
    > Author: ma6174
    > Mail: ma6174@163.com 
    > Created Time: 2015年02月05日 星期四 17时28分04秒
 ************************************************************************/

#include<iostream>
using namespace std;

struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
	bool hasPathSum(TreeNode *root, int sum){
		TreeNode p = *root;
		if(p.val == sum){
			return true;
		}
		if(p.left!=NULL){
			return hasPathSum(p.left, sum - p.val);
		}else if(p.right != NULL){
			return hasPathSum(p.right, sum - p.val);
		}
		return false;
	}
};

int main(){
	Solution a;
	TreeNode p;
	p.val = 1;

	print a.hasPathSum(p,2);
	return 0;
}
