package pl.rzyg.syncus.json;

import java.util.ArrayList;


// class for program config data structure related to tracked files
public class Config {
    final String osType ;
    String Version ;
    ArrayList<String[]> Files;
    int SyncRefreshSeconds ;

    public Config(String OS, String ConfigVersion, ArrayList<String[]> SyncFiles, int sec){
        this.osType = OS.toUpperCase();
        this.Version = ConfigVersion;
        this.Files = SyncFiles;
        this.SyncRefreshSeconds = sec;
    }

    public String getOSType() {
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

    public int getRefresh() {return this.SyncRefreshSeconds;}
}
