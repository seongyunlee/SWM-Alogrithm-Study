
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Q_16434 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static long N, power, hp, min;
    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        power = Integer.parseInt(st.nextToken());
        hp = 0;
        min = 0;

        for(int i = 0; i < N; i++) {
            solution();
        }
        System.out.println((-1 * min) + 1);
    }

    private static void solution() throws IOException {
        st = new StringTokenizer(br.readLine());
        int type = Integer.parseInt(st.nextToken());
        int a = Integer.parseInt(st.nextToken());
        int h = Integer.parseInt(st.nextToken());

        // 포션방
        if(type == 2) {
            power += a;
            hp += h;

            // 최대 체력보다 높아지면 최대 체력으로 고정
            if(hp > 0) {
                hp = 0;
            }
            return;
        }

        // 몬스터방
        // 때려야 하는 횟수
        long cnt = (h + (power - 1)) / power;
        hp -= a * (cnt - 1);
        min = Math.min(min, hp);
    }
}
