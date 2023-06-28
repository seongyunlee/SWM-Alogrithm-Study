#include <string>
#include <vector>

using namespace std;
vector<vector<int>> key, lock;
int ls, ks;

bool isMatched(vector<vector<int>> target) { // 열렸는 지 체크
    for(int i = ks-1; i < ls+ks-1; i++) {
        for(int j = ks-1; j < ls+ks-1; j++) {
            if(target[i][j] == 0) return false;
        }
    }
    return true;
}

bool match(int si, int sj) { // 열기 시도
    vector<vector<int>> lab = lock;
    for(int i = si; i < si+ks; i++) {
        for(int j = sj; j < sj+ks; j++) {
            if(i < ks-1 || i > ks+ls-1 || j < ks-1 || j > ks+ls-1 ) continue;
            if(lab[i][j] == 1 && key[i-si][j-sj] == 1) return false;
            lab[i][j] += key[i-si][j-sj];
        }
    }
    return isMatched(lab);
}

void rotation() { // 열쇠 돌리기
    vector<vector<int>> result;
    for(int i = 0; i < ks; i++) {
        vector<int> v;
        for(int j = 0; j < ks; j++) {
            v.push_back(key[ks-1-j][i]);
        }
        result.push_back(v);
    }
    key = result;
}

bool move() { // 열쇠 움직이기
    vector<vector<int>> lab = lock;
    for(int i = 0; i < ls+ks; i++) {
        for(int j = 0; j < ls+ks; j++) {
            if(match(i, j)) return true;
        }
    }
    return false;
}

bool solution(vector<vector<int>> k, vector<vector<int>> l) {
    ks = k.size();
    ls = l.size();
    key = k;

    for(int i = 0; i < ls+2*ks-2; i++) { // 넓은 곳에 자물쇠 놓기(?)
        vector<int> v;
        for(int j = 0; j < ls+2*ks-2; j++) {
           if(i < ks-1 || i > ls+ks-2 || j < ks-1 || j > ls+ks-2) v.push_back(0);
           else v.push_back(l[i-ks+1][j-ks+1]);
       }
       lock.push_back(v);
    }
    if(move()) return true;
    for(int k = 0; k < 3; k++) {
       rotation();
       if(move()) return true;
    }
    return false;
}