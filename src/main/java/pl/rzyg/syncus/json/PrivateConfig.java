package pl.rzyg.syncus.json;

//the classes below where created to handle built in JSON config (in Resources)
public class PrivateConfig {
    ConfigFilesLocation Config;
    LogFilesLocation Logs;


    //passing config location
    public String getWindowsConfigFilesLocation() {
        return this.Config.getWindows();
    }

    public String getWindowsLogsLocation() {
        return this.Logs.getWindows();
    }

    //passing config location
    public String getLinuxConfigFilesLocation() {
        return this.Config.getLinux();
    }

    public String getLinuxLogsLocation() {
        return this.Logs.getLinux();
    }

    //class related to PrivateConfig for holding configuration files location on different OSes
    private class ConfigFilesLocation {
        String Linux;
        String Windows ;

        //get linux configuration files location
        String getLinux() {
            return this.Linux;
        }

        //get windows configuration files location
        String getWindows() {
            return this.Windows;
        }
    }


    private class LogFilesLocation {
        String Linux;
        String Windows;

        //get linux log files location
        String getLinux() {
            return this.Linux;
        }

        //get windows log files location
        String getWindows() {
            return this.Windows;
        }
    }
}
