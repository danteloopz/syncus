package pl.rzyg.syncus;

public class Main {
    public static void main(String[] args) {
        System.out.println(getOSVersion());
    }

    private static String getOSVersion() {
        String osName = System.getProperty("os.name");
        if (osName.toUpperCase().contains("WINDOWS")) {
            return  "WINDOWS";
        } else if (osName.toUpperCase().contains("LIN")) {
            return "Linux";
        } else {
            return "UNKNOWN";
        }
    }
}
