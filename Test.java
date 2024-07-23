public class Test {
    public static void main(String[] args) {
        System.out.println("Hello World"); // This is Java comment
        // System.out.println(7);
        // for (int i = 0; i < 7; i++) {
        // System.out.println(i);
        // }
        int[] myNums = { 5, 1, 2, 3, 4 };
        // for (int i = 0; i < myNums.length; i++) {
        // System.out.println(myNums[i]);
        // }

        for (int x : myNums) {
            System.out.println(x);
        }
    }
}
