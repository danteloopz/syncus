package pl.rzyg.syncus.other;

import pl.rzyg.syncus.jsonHandler;

import java.io.File;
import java.util.Objects;
import java.util.stream.Stream;

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
        Stream<String> log_files = Stream.of(Objects.requireNonNull(new File(logLocation).listFiles())).map(File::getName);
        System.out.println(log_files);
    }

}
