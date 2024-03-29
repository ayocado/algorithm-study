import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class 부분합 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int S = Integer.parseInt(st.nextToken());

        int[] arr = new int[N];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i ++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        ArrayList<Integer> li = new ArrayList<>();
        int sum = 0;
        Queue<Integer> q = new ArrayDeque<>();
        for (int i = 0; i < N; i ++) {
            sum += arr[i];
            q.add(arr[i]);
            while(sum >= S) {
                li.add(q.size());
                sum -= q.poll();
            }
        }
        Collections.sort(li);
        if (li.isEmpty()) System.out.println(0);
        else System.out.println(li.get(0));
    }
}
