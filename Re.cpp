#include<iostream>
using namespace std;

class Solution(){
public:
	int a[10]={2,1,4,7,4,8,3,6,4,7}
	bool ans(int x){
		int i;
		while(x){
			if(x%10 > a[i]){
				return true;
			}
			x /= 10;
			i++;
		}
		return false;
	}
	int reverse(int x){
		int tmp = 1;
		int ans = 0;
		m = x;
		if(x / 1000000000 > 0){
			if(ans(x)){
				return 0;
			}
			x = m;
		}
		if(x < 0 && (abs(x) / 1000000000 > 0)){
			x = abs(x);
			while(x){
				if(ans(x)){
					return 0;
				}
			}
		}
		k = abs(m);
		while(k){
			ans += k%10;
			if(tmp<10){
				ans *= 10;
			}
			tmp++;
		}
		if(tmp==11){
			printf("%d\n",ans);
		}else{
			printf("%d\n",ans/10);
		}
	}
};
int main(){

	return 0;
}
