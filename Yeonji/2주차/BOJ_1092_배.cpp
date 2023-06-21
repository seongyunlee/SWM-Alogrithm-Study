#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n, m, tmp, ans = 0;
    vector<int> crane, item;
    cin >> n;
    for(int i = 0; i < n; i++) {
        cin >> tmp;
        crane.push_back(tmp);
    }
    sort(crane.rbegin(), crane.rend());
    cin >> m;
    for(int i = 0; i < m; i++) {
        cin >> tmp;
        item.push_back(tmp);
    }
    sort(item.rbegin(), item.rend());
    if(item[0] > crane[0]) {
        cout << "-1\n";
        return 0;
    }
    while(!item.empty()) {
        for(int i = 0; i < crane.size(); i++) {
            tmp = 0;
            for(int j = 0; j < item.size(); j++) {
                if(crane[i] >= item[j]) {
                    item.erase(item.begin()+j);
                    tmp = 1;
                    break;
                }
            }
            if(tmp==0) {
                crane.pop_back();
                i--;
            }
        }
        ans++;
    }
    cout << ans << '\n';
    return 0;
}