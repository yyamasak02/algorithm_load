import java.util.ArrayDeque;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

class Tuple {
    int left;
    int right;

    public Tuple(int left, int right) {
        this.left = left;
        this.right = right;
    }
    public void increment(char c) {
        if (c == '(') left++;
        else if (c == ')') right++;
    }
    public boolean isEqual() {
        return this.left == this.right;
    }

    public boolean isOver() {
        return this.right > this.left;
    }

    public Tuple copy() {
        return new Tuple(this.left, this.right);
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int Q = Integer.parseInt(br.readLine());
        ArrayDeque<Tuple> st = new ArrayDeque<>();
        st.push(new Tuple(0, 0));
        int overCount = 0;
        Tuple top;
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < Q; i++) {
            String[] parts = br.readLine().split(" ");
            int n = Integer.parseInt(parts[0]);
            if (n == 1) {
                char c = parts[1].charAt(0);
                top = st.peek().copy();
                top.increment(c);
                if (top.isOver()) overCount++;
                st.push(top);
            }
            else {
                if (st.pop().isOver()) overCount--;
            }
            sb.append((st.peek().isEqual() && overCount == 0) ? "Yes\n" : "No\n");
        }
        System.out.print(sb);
    }
}
