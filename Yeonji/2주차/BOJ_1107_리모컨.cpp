#include <iostream>

using namespace std;

bool num[10];
string n;
int m, tmp, ans, l;

int getdist(int i, int j) {
    return i > j? i-j: j-i;
}

void dosth(string cur) {
    if((int) cur.length() == 6) return;
    for(int i = 0; i < 10; i++) {
        if(num[i]) {
            cur += to_string(i);
            ans = min(ans, (int) cur.length() + getdist(stoi(n), stoi(cur)));
            dosth(cur);
            cur.pop_back();
        }
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    fill_n(num, 10, true);
    cin >> n >> m;
    for(int i = 0; i < m; i++) {
        cin >> tmp;
        num[tmp] = false;
    }
    ans = getdist(100, stoi(n));
    tmp = 0;
    l = (int) n.length();
    // 해당 채널의 각 자리 숫자가 열려있는지 확인
    for(int i = 0; i < l; i++) {
        if(!num[n[i]-'0']){
            tmp = 1;
            break;
        }
    }
    if(tmp == 0) ans = min(ans, l);
    dosth("");
    cout << ans << '\n';
    return 0;
}