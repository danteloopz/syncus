package pl.rzyg.syncus.json;

import java.util.ArrayList;


// class for program config data structure related to tracked files
public class Config {
    private final String osType ;
    private String Version ;
    private ArrayList<String[]> Files;

    public Config(String OS, String ConfigVersion, ArrayList<String[]> SyncFiles){
        this.osType = OS.toUpperCase();
        this.Version = ConfigVersion;
        this.Files = SyncFiles;
    }

    public String getOStype() {
        return this.osType;
    }

    public String getConfigVersion() {
        return this.Version;
    }

    public void setConfigVersion(String version) {
        this.Version = version;
    }

    public ArrayList<String[]> getFiles() {
        return this.Files;
    }

    public void setFiles(ArrayList<String[]> array) {
        this.Files = array;
    }
}
