package pl.rzyg.syncus;
/*
* the Logger class
*
* this is the future logger class for syncus
*
* it will create new logfiles and log information to them
**/
public class Logger {
    jsonHandler json = new jsonHandler();
    String logLocation ;
    public Logger(String OS) {
        logLocation = json.getLogs(OS);
        if (logLocation.isEmpty()) {System.exit(-1);}
    }

}
