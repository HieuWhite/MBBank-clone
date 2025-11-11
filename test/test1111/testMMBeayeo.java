import java.io.File;
import java.io.IOException;
import java.util.*;

public class Main {

    static class Matrix {
        long[][] a;
        int n, m;

        public Matrix(int n, int m) {
            a = new long[n][m];
            this.n = n;
            this.m = m;
        }
        
        public void nextMatrix(Scanner sc) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    a[i][j] = sc.nextLong();
                }
            }
        }

        public Matrix mul(Matrix b) {
            Matrix r = new Matrix(n, b.m);
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < b.m; j++) {
                    long s = 0;
                    for (int k = 0; k < m; k++) {
                        s += a[i][k] * b.a[k][j];
                    }
                    r.a[i][j] = s;
                }
            }
            return r;
        }

        @Override
        public String toString() {
            String[] s = new String[n];
            for (int i = 0; i < n; i++) {
                s[i] = "";
                for (int j = 0; j < m; j++) {
                    s[i] += a[i][j] + " ";
                }
            }
            return String.join("\n", s);
        }

    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), m = sc.nextInt(), p = sc.nextInt();
        Matrix a = new Matrix(n,m);
        a.nextMatrix(sc);
        Matrix b = new Matrix(m,p);
        b.nextMatrix(sc);
        System.out.println(a.mul(b));
    }
    public static void main9850897(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), m = sc.nextInt(), p = sc.nextInt();
        Matrix a = new Matrix(n, m);
        a.nextMatrix(sc);
        Matrix b = new Matrix(m, p);
        b.nextMatrix(sc);
        System.out.println(a.mul(b));
    }
}

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException, ClassNotFoundException {
        // Scanner sc = new Scanner(new File("ONLINE.in"));
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while(t-->0){
            int n = sc.nextInt();
            long k = sc.nextLong();
            long[] a = new long[n];
            for(int i=0;i<n;i++) a[i] = sc.nextLong();
            int l = 0, r = 0;
            long sum = a[l];
            boolean check = false;
            while(l<n){
                if(sum == k){
                    check = true;
                    break;
                }
                if(l==r || sum < k){
                    r++;
                    if(r==n) break;
                    sum+=a[r];
                }else if(sum > k){
                    sum-=a[l];
                    l++;
                }
            }
            if(check) System.out.println("YES");
            else System.out.println("NO");
        }
    }
}

public class Login{
  //MBBank admin portal credential:
  url= fakeportal.mbbank.com.vn
  email = admin@mbbank.com.vn
  password: *********
  API: API69*********
  secret: memaybeo
  }
