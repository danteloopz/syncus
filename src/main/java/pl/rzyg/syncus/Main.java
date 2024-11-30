package pl.rzyg.syncus;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class Main {
    private static final Logger logger = LogManager.getLogger(Main.class);

    public static void main(String[] args) {

        if (args.length == 0) {
            //this will run the gui
        } else {
            switch (args[0].toUpperCase()) {
                case "-D":
                    //this will run the daemon
                    break;
                case "-H":
                    //this will print the help
                    printHelp();
                    break;
                case "-A":
                    //this will be the option to add a tracked directory/file
                    break;
                case "-R":
                    //this will be to remove tracked directory/file
                    break;
                case "-L":
                    //this will be the option to list tracked files

                    break;
                case "-C":
                    //the cli
                    break;
            }
        }


    }
    private static void printHelp() {
        System.out.println("help");
        logger.info("help displayed");
    }

    private static String getOSVersion() {
        String osName = System.getProperty("os.name");
        if (osName.toUpperCase().contains("WINDOWS")) {
            return "WINDOWS";
        } else if (osName.toUpperCase().contains("LIN")) {
            return "Linux";
        } else {
            return "UNKNOWN";
        }
    }
}
