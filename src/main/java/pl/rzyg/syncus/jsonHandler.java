package pl.rzyg.syncus;
/* TODO:
done - add code to generate JSON config files when they weren't found (in FileNotFoundException)
- add cote to return Config file instance.
 */
import com.google.gson.Gson;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.net.URISyntaxException;
import java.net.URL;
import java.util.ArrayList;
import java.util.Scanner;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import pl.rzyg.syncus.json.PrivateConfig;
import pl.rzyg.syncus.json.Config;

import static java.lang.System.out;
//class to handle json config files
public class jsonHandler {
    private static final Logger logger = LogManager.getLogger(Main.class);
    Gson gson = new Gson();
    StringBuilder json = new StringBuilder();
    Config config ;
    PrivateConfig BuiltInConfig = new PrivateConfig();

    public jsonHandler() {
        URL BuiltIn = getClass().getClassLoader().getResource("files.json");
        assert BuiltIn != null;
        try {
            Scanner FilesConfigurationReader = new Scanner(new File(BuiltIn.toURI()));
            StringBuilder BuiltInConfigJSON = new StringBuilder();

            while (FilesConfigurationReader.hasNextLine()) {
                BuiltInConfigJSON.append(FilesConfigurationReader.nextLine());
            }

            BuiltInConfig = gson.fromJson(BuiltInConfigJSON.toString(), PrivateConfig.class);

        } catch (URISyntaxException | FileNotFoundException e) {logger.error(e.getStackTrace());}

    }
    public String getLogs(String OS) {
        if (OS.equals("WINDOWS")) {
            return this.BuiltInConfig.getWindowsLogsLocation();
        } else if (OS.equals("LINUX")) {
            return this.BuiltInConfig.getLinuxLogsLocation();
        }else {
            out.println("Error recognizing os while getting logs location");
            return "";
        }
    }
    //load in Windows config file
    boolean winConfig() {
        try {
            //add path from built in config
            File jsonFile = new File(this.BuiltInConfig.getWindowsConfigFilesLocation());
            Scanner fileReader = new Scanner(jsonFile);
            while (fileReader.hasNextLine()) {
                this.json.append(fileReader.nextLine());
            }
        } catch (FileNotFoundException e) {
            out.println("file not found");
            this.config = new Config("WINDOWS","1.0", new ArrayList<String[]>());
            if (!writeConfig("Windows")){
                out.println("Could not create new config");}
        }

        this.config = this.gson.fromJson(json.toString(), Config.class);
        return this.config.getOStype().equals("Windows");
    }

    //load in Linux config
    boolean linConfig() {
        try {
            //add path from built in config
            File jsonFile = new File(this.BuiltInConfig.getLinuxConfigFilesLocation());
            Scanner fileReader = new Scanner(jsonFile);
            while (fileReader.hasNextLine()) {
                this.json.append(fileReader.nextLine());

            }
        } catch (FileNotFoundException e) {
            out.println("file not found");
            this.config = new Config("LINUX","1.0", new ArrayList<String[]>());
            if (!writeConfig("LINUX")){
                out.println("Could not create new config");}
        }

        this.config = this.gson.fromJson(this.json.toString(), Config.class);
        return this.config.getOStype().equals("LINUX");
    }

    boolean writeConfig(String os) {
        boolean success = false;
        if (os.equalsIgnoreCase("WINDOWS")) {
            try {
                File newFile = new File(this.BuiltInConfig.getWindowsConfigFilesLocation());
                if (newFile.createNewFile()) {
                    FileWriter myWriter = new FileWriter(this.BuiltInConfig.getWindowsConfigFilesLocation());
                    myWriter.write(this.gson.toJson(this.config, pl.rzyg.syncus.json.Config.class));
                    success = true;
                }

            } catch (IOException e) {
                out.println("Error");
                logger.error(e.getStackTrace());
            }
        } else if (os.equalsIgnoreCase("LINUX")) {
            try {
                File newFile = new File(this.BuiltInConfig.getLinuxConfigFilesLocation());
                if (newFile.createNewFile()) {
                    FileWriter myWriter = new FileWriter(this.BuiltInConfig.getLinuxConfigFilesLocation());
                    myWriter.write(this.gson.toJson(this.config, pl.rzyg.syncus.json.Config.class));
                    success = true;
                }

            } catch (IOException e) {
                out.println("Error");
                logger.error(e.getStackTrace());
            }
        }
        return success;
    }

}