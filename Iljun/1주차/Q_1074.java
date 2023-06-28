import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Q_1074 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int N, r, c;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        check(0, N, r, c);

    }

    public static void check(int num, int N, int r, int c) {
        if(N == 0) {
            System.out.println(num);
            return;
        }

        int length = (int)Math.pow(2, N);
        int half = length / 2;

        if(r < half && c < half) {
            check(num, N - 1, r, c);
        } else if(r < half && c >= half) {
            check(num + half * half, N - 1, r, c - half);
        } else if(r >= half && c < half) {
            check(num + half * half * 2, N - 1, r - half, c);
        } else {
            check(num + half * half * 3, N - 1, r - half, c - half);
        }
    }
}
