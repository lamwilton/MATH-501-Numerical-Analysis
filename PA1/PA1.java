public class main {

   public static void main(String[] args) {
      singlePrecision();
      doublePrecision();
   }

   private static void singlePrecision() {
      float s = 1.0F;
      for (int k = 1; k <= 100; k++) {
         s = 0.5F * s;
         float t = s + 1.0F;
         if (t <= 1.0F) {
            s = 2.0F * s;
            System.out.println("Single-precision: k - 1 = " + (k - 1));
            System.out.println("s = " + s);
            break;
         }
      }
   }

   private static void doublePrecision() {
      double s = 1.0;
      for (int k = 1; k <= 100; k++) {
         s = 0.5 * s;
         double t = s + 1.0;
         if (t <= 1.0) {
            s = 2.0 * s;
            System.out.println("Double-precision: k - 1 = " + (k - 1));
            System.out.println("s = " + s);
            break;
         }
      }
   }
}
