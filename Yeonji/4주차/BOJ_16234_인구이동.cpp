#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int n, l, r, cnt = 0;
int board[50][50];

vector<vector<pair<int, int>>> ucs;
queue<pair<int, int>> q;

int d[4][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
bool isInBoard(int i, int j) { return i > -1 && i < n && j > -1 && j < n; }

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> l >> r;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            cin >> board[i][j];
        }
    }

    do {
        ucs.clear();
        bool vis[50][50] = {false, };
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                if(!vis[i][j]) {
                    vis[i][j] = true;
                    q.emplace(i, j);
                    vector<pair<int, int>> uc;
                    uc.emplace_back(i, j);
                    int ci, cj, ni, nj, dist, total = board[i][j];

                    while(!q.empty()) {
                        ci = q.front().first; cj = q.front().second;
                        q.pop();
                        for(int k = 0; k < 4; k++) {
                            ni = ci + d[k][0]; nj = cj + d[k][1];
                            if(isInBoard(ni, nj) && !vis[ni][nj]) {
                                dist = abs(board[ci][cj]-board[ni][nj]);
                                if(dist >= l && dist <= r) {
                                    vis[ni][nj] = true;
                                    q.emplace(ni, nj);
                                    uc.emplace_back(ni, nj);
                                    total += board[ni][nj];
                                }
                            }
                        }
                    }
                    if(uc.size() == 1) {
                        vis[i][j] = false;
                        continue;
                    }
                    uc.emplace_back(total, uc.size());
                    ucs.push_back(uc);
                }
            }
        }
        if(ucs.empty()) break;
        vector<pair<int, int>> uc;
        int cal;
        for(int i = 0; i < ucs.size(); i++) {
            uc = ucs[i];
            cal = uc[uc.size()-1].first / uc[uc.size()-1].second;
            for(int j = 0; j < uc.size()-1; j++) {
                board[uc[j].first][uc[j].second] = cal;
            }
        }
        cnt++;
    } while(!ucs.empty());

    cout << cnt << '\n';
    return 0;
}