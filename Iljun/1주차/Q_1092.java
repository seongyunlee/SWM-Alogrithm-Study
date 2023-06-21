
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Q_1092 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int N, M;
    static ArrayList<Integer> craneList, boxList;

    public static void main(String[] args) throws IOException {

        // 크레인 입력
        N = Integer.parseInt(br.readLine());
        craneList = new ArrayList<>();
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < N; i++) {
            craneList.add(Integer.parseInt(st.nextToken()));
        }
        Collections.sort(craneList, Collections.reverseOrder());

        // 박스 입력
        M = Integer.parseInt(br.readLine());
        boxList = new ArrayList<>();
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < M; i++) {
            boxList.add(Integer.parseInt(st.nextToken()));
        }
        Collections.sort(boxList, Collections.reverseOrder());

        solution();
    }

    private static void solution() {

        // 만약 크레인의 최대 무게가 박스의 최소 무게보다 작다면 -1 출력
        if(boxList.get(0) > craneList.get(0)) {
            System.out.println(-1);
            return;
        }

        int time = 0;
        // 박스가 모두 비워질 때까지 반복
        while(!boxList.isEmpty()) {
            time++;
            for(int i = 0; i < craneList.size(); i++) {
                //크레인 하나당 박스 돌면서 확인
                for(int j = 0; j < boxList.size(); j++) {
                    if(craneList.get(i) >= boxList.get(j)) {
                        boxList.remove(j);
                        break;
                    }
                }
            }
        }

        System.out.println(time);
    }
}
