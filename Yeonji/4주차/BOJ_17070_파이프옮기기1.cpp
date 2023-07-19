#include <iostream>

using namespace std;

int n;
int board[16][16];
int dp[16][16][3]; // 그 위치를 끝으로 하는 파이프를 가로 세로 대각선 으로 놓을 수 있는 방법

// 가로 dp[i][j][0] == dp[i][j-1][0] + dp[i][j-1][2]
// 세로 dp[i][j][1] == dp[i-1][j][1] + dp[i-1][j][2]
// 대각선 dp[i][j][2] == dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cin >> n;
	for(int i = 0; i < n; i++){
		for(int j = 0; j < n; j++){
			cin >> board[i][j];
		}
	}
	// 첫 행 가로는 벽이 없다면 모두 갈 수 있으므로 1로 초기화
	for(int i = 1; i < n && !board[0][i]; i++) dp[0][i][0] = 1; 
	// 첫 열 세로는 모두 갈 수 없으므로 0

	// 첫 행과 첫 열을 제외하고 진행
	for(int i = 1; i < n; i++) {
		for(int j = 1; j < n; j++) {
			// 가로 세로는 그 위치만 벽의 유무를 체크하면 된다.
			if(!board[i][j]) {
				dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2];
				dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2];
				if(!board[i-1][j] && !board[i][j-1])
					dp[i][j][2] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2];
			}
		}
	}
	cout << dp[n-1][n-1][0] + dp[n-1][n-1][1] + dp[n-1][n-1][2] << '\n';
	return 0;
}