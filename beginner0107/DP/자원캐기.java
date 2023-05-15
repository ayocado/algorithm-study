import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 자원캐기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[][] m = new int[N][M];
        int[][] dp = new int[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                m[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // 첫 번째 행 초기화
        dp[0][0] = m[0][0];
        for (int j = 1; j < M; j++) {
            dp[0][j] = dp[0][j - 1] + m[0][j];
        }

        // 첫 번째 열 초기화
        for (int i = 1; i < N; i++) {
            dp[i][0] = dp[i - 1][0] + m[i][0];
        }

        // 나머지 칸 계산
        for (int i = 1; i < N; i++) {
            for (int j = 1; j < M; j++) {
                dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]) + m[i][j];
            }
        }

        System.out.println(dp[N - 1][M - 1]);
    }
}
