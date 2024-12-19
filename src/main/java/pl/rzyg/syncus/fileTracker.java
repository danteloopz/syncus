package pl.rzyg.syncus;

import org.apache.logging.log4j.Logger;

import java.util.ArrayList;
import java.util.logging.LogManager;

public class fileTracker {
    jsonHandler json = new jsonHandler();


    public boolean addFile(String[] loc, String OS, Logger logger) {
        ArrayList<String[]> trackedFiles;
        boolean success = false;
        switch (OS){
            case "WINDOWS":
                json.winConfig();
                trackedFiles = json.config.getFiles();
                trackedFiles.add(loc);
                json.config.setFiles(trackedFiles);
                success = json.writeConfig(OS);
                break;
            case "LINUX":
                json.linConfig();
                trackedFiles = json.config.getFiles();
                trackedFiles.add(loc);
                success = json.writeConfig(OS);
                break;
            default:
                logger.error("OS type not recognized");
                System.out.println("Error: could not recognize os type");
        }
        if (!success) {
            logger.error("couldn't save config file");
        }
        return success;
    }
}
