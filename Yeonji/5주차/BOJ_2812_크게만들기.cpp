#include <iostream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int n, k;
	string num, ans = "";
	cin >> n >> k >> num;
	ans += num[0];
	for(int i = 1; i < n; i++) {
		// 현재 숫자보다 작은 앞자리 숫자 다 삭제, 계속해서 k--
		while(ans.length() && ans.back() < num[i] && k) {
			ans.pop_back();
			k--;
		}
		ans += num[i];
	}
	// 다 돌았는데도 k가 0이 아니면 뒤에서 부터 삭제
	cout << ans.substr(0, ans.length()-k) << '\n';
	return 0;
}