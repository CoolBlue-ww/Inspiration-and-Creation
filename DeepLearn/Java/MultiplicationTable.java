public class MultiplicationTable {
    public static void main(String[] args) {
        for (int i = 1; i <= 9; i++) {
            for (int j = 1; j <= i; j++) {
                String formatted = String.format("%d * %d = %d\t", i, j, i*j);
                System.out.print(formatted);
            }
            System.out.println();
        }
    }
}
