class leetcode{
    public static String convert(int n){
        StringBuilder ans = new StringBuilder(null);
        while(n>0){
            --n;
            int d = n %26;
            n /= 26;
            ans.append((char)('A'+d));

        }
        ans.reverse();
        return ans.toString();

    }
    public static void main(String[] args) {
        System.out.println(convert(34));
    }

}