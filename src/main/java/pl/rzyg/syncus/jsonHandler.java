package pl.rzyg.syncus;

import com.google.gson.Gson;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

//class to handle json config files
public class jsonHandler {
    Gson gson = new Gson();
    String json = "";
    Config config ;

    public jsonHandler() {
        //finish this !!!
        //PrivateConfig BuiltInConfig = gson.fromJson();
    }

    //load in Windows config file
    void winConfig() {
        try {
            //add path from built in config
            File jsonFile = new File();
            Scanner fileReader = new Scanner(jsonFile);
            while (fileReader.hasNextLine()) {
                json = json + fileReader.nextLine();
            }
        } catch (FileNotFoundException e) {
            System.out.println("file not found");
        }

        config = gson.fromJson(json, Config.class);
    }

    //load in Linux config
    void linConfig() {
        try {
            //add path from built in config
            File jsonFile = new File();
            Scanner fileReader = new Scanner(jsonFile);
            while (fileReader.hasNextLine()) {
                json = json + fileReader.nextLine();

            }
        } catch (FileNotFoundException e) {
            System.out.println("file not found");
        }

        config = gson.fromJson(json, Config.class);
    }

}

class Config {
    private final String osType ;
    private final String Version ;
    private ArrayList<String[]> Files = new ArrayList<>();

    public Config(String OS, String ConfigVersion, ArrayList<String[]> SyncFiles){
        this.osType = OS;
        this.Version = ConfigVersion;
        this.Files = SyncFiles;
    }

    String getOStype() {
        return this.osType;
    }
    String getConfigVersion() {
        return this.Version;
    }
    ArrayList<String[]> getFiles() {
        return this.Files;
    }
}

class PrivateConfig {
    private final ConfigFilesLocation CfgFiles;

    public PrivateConfig(ConfigFilesLocation Config) {
        this.CfgFiles = Config;
    }

    String getWindowsConfigFilesLocation() {
        return this.CfgFiles.getWindows();
    }
    String getLinuxConfigFilesLocation() {
        return this.CfgFiles.getLinux();
    }
}

class ConfigFilesLocation {
    private final String Linux;
    private final String Windows ;

    public ConfigFilesLocation(String lin, String win) {
        this.Linux = lin;
        this.Windows = win;
    }

    String getLinux() {
        return this.Linux;
    }

    String getWindows() {
        return this.Windows;
    }
}