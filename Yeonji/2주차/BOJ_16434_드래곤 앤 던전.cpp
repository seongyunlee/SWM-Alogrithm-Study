#include <iostream>

using namespace std;

int n, atk;
int bang[123456][3];

bool go(long long hp) {
    long long tatk = atk;
    long long maxh = hp;
    for(int i = 0; i < n; i++) {
        if(bang[i][0] == 1) { //용
            hp -= bang[i][2]%tatk? (long long)bang[i][1]*(bang[i][2]/tatk): (long long)bang[i][1]*(bang[i][2]/tatk-1);
            if(hp <= 0) return false;
        } else { //포션
            tatk += bang[i][1];
            hp = min(hp+bang[i][2], maxh);
        }   
    }
    return true;
}

int main() {
    cin >> n >> atk;
    for(int i = 0; i < n; i++) {
        cin >> bang[i][0] >> bang[i][1] >> bang[i][2];
    }
    long long l = 1, r = 0x3f3f3f3f3f3f3f3f, mid;
    while(l + 1 < r) {
        mid = (l + r)/2;
        if(go(mid)) r = mid;
        else l = mid;
    }
    mid = (l + r)/2;
    if(go(mid)) cout << mid << '\n';
    else cout << r << '\n';
    return 0;
}