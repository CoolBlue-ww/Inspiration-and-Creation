import java.time.LocalTime;

public class DaffodilsNumber {
    public static void main(String[] args) {
        for (int x = 1; x < 10; x++) {
            for (int y = 0; y < 10; y++) {
                for (int z = 0; z < 10; z++) {
                    if (x * x * x + y * y * y + z * z *z == x * 100 + y * 10 + z) {
                        int total = x * 100 + y + 10 + z;
                        String formatted = String.format("%d 是水仙花数！", total);
                        System.out.println(formatted);
                    }
                }
            }
        }
    }
}
