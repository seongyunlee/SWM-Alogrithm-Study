package Baekjoon;

import java.io.*;
import java.util.*;

class node {
    int x;
    int y;
    int move;

    node(int x, int y, int move){
        this.x = x;
        this.y = y;
        this.move = move;
    }
}

public class Q_14940 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int N, M;
    static boolean[][] check;
    static int[][] route;
    static int[][] map;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        route = new int[N][M];
        map = new int[N][M];
        check = new boolean[N][M];

        for(int i=0; i<N; i++){
            for(int j=0; j<M; j++){
                route[i][j] = -1;
            }
        }

        Queue<node> q = new LinkedList<>();

        for(int i=0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<M; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                if(map[i][j]==2){
                    check[i][j] = true;
                    route[i][j] = 0;
                    q.add(new node(i, j, 0));
                }
            }
        }

        while(!q.isEmpty()){
            node node = q.remove();
            int x = node.x;
            int y = node.y;
            int move = node.move;
            route[x][y] = move;

            for(int d = 0; d < 4; d++){
                int nx = x + dx[d];
                int ny = y + dy[d];

                if(nx<0 || ny<0 || nx>=N || ny>=M) continue;
                if(check[nx][ny] || map[nx][ny]==0) continue;
                check[nx][ny] = true;

                q.add(new node(nx, ny, (move+1)));
            }
        }

        for(int i=0; i<N; i++){
            for(int j=0; j<M; j++){
                if(map[i][j] == 0) route[i][j] = 0;
            }
        }

        for(int i=0; i<N; i++){
            for(int j=0; j<M; j++){
                sb.append(route[i][j]).append(" ");
            }sb.append("\n");
        }
        System.out.println(sb);
    }
}


