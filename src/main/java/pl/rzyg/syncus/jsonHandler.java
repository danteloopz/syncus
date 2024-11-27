package pl.rzyg.syncus;
/* TODO:
- add code to generate JSON config files when they weren't found (in FileNotFoundException)
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
    boolean winConfig() {
        try {
            //add path from built in config
            File jsonFile = new File(BuiltInConfig.getWindowsConfigFilesLocation());
            Scanner fileReader = new Scanner(jsonFile);
            while (fileReader.hasNextLine()) {
                json = json + fileReader.nextLine();
            }
        } catch (FileNotFoundException e) {
            System.out.println("file not found");
            config = new Config("WINDOWS","1.0", new ArrayList<String[]>());
            if (!writeConfig("Windows")){System.out.println("Could not create new config");}
        }

        config = gson.fromJson(json, Config.class);
        return config.getOStype().equals("Windows");
    }

    //load in Linux config
    boolean linConfig() {
        try {
            //add path from built in config
            File jsonFile = new File(BuiltInConfig.getLinuxConfigFilesLocation());
            Scanner fileReader = new Scanner(jsonFile);
            while (fileReader.hasNextLine()) {
                json = json + fileReader.nextLine();

            }
        } catch (FileNotFoundException e) {
            System.out.println("file not found");
            config = new Config("LINUX","1.0", new ArrayList<String[]>());
            if (!writeConfig("LINUX")){System.out.println("Could not create new config");}
        }

        config = gson.fromJson(json, Config.class);
        return config.getOStype().equals("LINUX");
    }

    boolean writeConfig(String os) {
        boolean success = false;
        if (os.toUpperCase().equals("WINDOWS")) {
            try {
                File newFile = new File(BuiltInConfig.getWindowsConfigFilesLocation());
                if (newFile.createNewFile()) {
                    FileWriter myWriter = new FileWriter(BuiltInConfig.getWindowsConfigFilesLocation());
                    myWriter.write(gson.toJson(config, Config.class));
                    success = true;
                }

            } catch (IOException e) {
                System.out.println("Error");
                e.printStackTrace();
            }
        } else if (os.toUpperCase().equals("LINUX")) {
            try {
                File newFile = new File(BuiltInConfig.getLinuxConfigFilesLocation());
                if (newFile.createNewFile()) {
                    FileWriter myWriter = new FileWriter(BuiltInConfig.getLinuxConfigFilesLocation());
                    myWriter.write(gson.toJson(config, Config.class));
                    success = true;
                }

            } catch (IOException e) {
                System.out.println("Error");
                e.printStackTrace();
            }
        }
        return success;
    }

}

//the classes below where created to handle built in JSON config (in Resources)

// class for program config data structure
class Config {
    private final String osType ;
    private String Version ;
    private ArrayList<String[]> Files;

    public Config(String OS, String ConfigVersion, ArrayList<String[]> SyncFiles){
        this.osType = OS.toUpperCase();
        this.Version = ConfigVersion;
        this.Files = SyncFiles;
    }

    String getOStype() {
        return this.osType;
    }

    String getConfigVersion() {
        return this.Version;
    }

    void setConfigVersion(String version) {
        this.Version = version;
    }

    ArrayList<String[]> getFiles() {
        return this.Files;
    }

    void setFiles(ArrayList<String[]> array) {
        this.Files = array;
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