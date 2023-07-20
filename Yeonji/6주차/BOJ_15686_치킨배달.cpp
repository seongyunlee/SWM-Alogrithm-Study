#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int n, m, ans = 100*2500, tmpans = 0, chidist = 0;
vector<pair<int, int>> chi, zip;
vector<bool> exist;

int main() {
    cin >> n >> m;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            cin >> tmpans;
            if(tmpans == 2) chi.emplace_back(i, j);
            if(tmpans == 1) zip.emplace_back(i, j);
        }
    }
    exist.resize(chi.size());
    fill(exist.end()-m, exist.end(), true);
    do {
        tmpans = 0;
        for(int i = 0; i < zip.size(); i++) {
            chidist = 101;
            for(int j = 0; j < chi.size(); j++) {
                if(exist[j]) {
                    chidist = min(chidist, abs(zip[i].first-chi[j].first) + abs(zip[i].second-chi[j].second));
                }
            }
            if(chidist != 101) tmpans += chidist;
        }
        ans = min(ans, tmpans);
    } while(next_permutation(exist.begin(), exist.end()));
    cout << ans << '\n';
    return 0;
}