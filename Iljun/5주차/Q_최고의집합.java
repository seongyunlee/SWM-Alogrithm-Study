package programmers;

public class Q_최고의집합 {

    public static void main(String[] args) {
        System.out.println(solution(2, 9));
        System.out.println(solution(2, 1));
        System.out.println(solution(2, 8));
    }

    public static int[] solution(int n, int s) {
        int[] answer = new int[n];

        // 원하는 집합을 만들지 못하는 경우
        if (n > s) {
            return new int[]{-1};
        }

        // 최대한 동등하게 나눠주는 것이 가장 좋다.
        if (s % n == 0) {
            for (int i = 0; i < n; i++) {
                answer[i] = s / n;
            }
            return answer;
        }

        // 나머지가 있을 경우
        for (int i = 0; i < n; i++) {
            answer[i] = s / n;
        }
        for (int i = 0; i < s % n; i++) {
            answer[n - i - 1]++;
        }
        return answer;
    }
}
