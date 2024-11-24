package pl.rzyg.syncus;
/* TODO:
- add code to generate JSON config files when they weren't found (in FileNotFoundException)
- add cote to return Config file instance.
 */
import com.google.gson.Gson;
import java.io.File;
import java.io.FileNotFoundException;
import java.net.URISyntaxException;
import java.net.URL;
import java.util.ArrayList;
import java.util.Scanner;

//class to handle json config files
public class jsonHandler {
    Gson gson = new Gson();
    String json = "";
    Config config ;
    PrivateConfig BuiltInConfig;

    public jsonHandler() {
        URL BuiltIn = getClass().getClassLoader().getResource("files.json");
        assert BuiltIn != null;
        try {
            Scanner FilesConfigurationReader = new Scanner(new File(BuiltIn.toURI()));
            String BuiltInConfigJSON ="";

            while (FilesConfigurationReader.hasNextLine()) {
                BuiltInConfigJSON = BuiltInConfigJSON + FilesConfigurationReader.nextLine();
            }

            BuiltInConfig = gson.fromJson(BuiltInConfigJSON, PrivateConfig.class);

        } catch (URISyntaxException | FileNotFoundException e) {e.printStackTrace();}

    }

    //load in Windows config file
    void winConfig() {
        try {
            //add path from built in config
            File jsonFile = new File(BuiltInConfig.getWindowsConfigFilesLocation());
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
            File jsonFile = new File(BuiltInConfig.getLinuxConfigFilesLocation());
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

//the classes below where created to handle built in JSON config (in Resources)

// class for program config data structure
class Config {
    private final String osType ;
    private final String Version ;
    private ArrayList<String[]> Files;

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

    void setFiles(ArrayList<String[]> a) {
        this.Files = a;
    }
}

// class for program files location data structure
class PrivateConfig {
    private final ConfigFilesLocation CfgFiles;

    public PrivateConfig(ConfigFilesLocation Config) {
        this.CfgFiles = Config;
    }

    //passing config location
    String getWindowsConfigFilesLocation() {
        return this.CfgFiles.getWindows();
    }

    //passing config location
    String getLinuxConfigFilesLocation() {
        return this.CfgFiles.getLinux();
    }
}

//class related to PrivateConfig for holding configuration files location on different OSes
class ConfigFilesLocation {
    private final String Linux;
    private final String Windows ;

    public ConfigFilesLocation(String lin, String win) {
        this.Linux = lin;
        this.Windows = win;
    }

    //get linux configuration files location
    String getLinux() {
        return this.Linux;
    }

    //get windows configuration files location
    String getWindows() {
        return this.Windows;
    }
}