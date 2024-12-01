package pl.rzyg.syncus;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

/*
* the Command Line Interface
*
* this class willbe the future cli for syncus
*
* */
public class CLI {
    private static final Logger logger = LogManager.getLogger(Main.class);
    private final jsonHandler json = new jsonHandler();
    private final String OS;

    public CLI(String os) {
        this.OS = os;
        boolean config_load_check = false;
        if (os.equals("WINDOWS")) {config_load_check =  json.winConfig();}
        else if (os.equals("LINUX")) {config_load_check = json.linConfig();}
        else {
        logger.error("Unknown OS");
        System.out.println("CLI: Your OS is unknown. please contact help");
        }
        if (!config_load_check) {logger.error("could not load config"); System.out.println("Error loading config");}

    }

}
