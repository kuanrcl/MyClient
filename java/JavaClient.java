// package mysql.demo;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import com.mysql.cj.jdbc.Driver;
import org.apache.commons.cli.*;


public class JavaClient {

    private static long ttltime=0;
    private static String driver = "com.mysql.cj.jdbc.Driver";
    private static String database = "test";
    private static String baseUrl = "jdbc:mysql://";
    private static String user = "demo";
    private static String password = "demo";
    private static String dbhostport = "localhost:3306";
    private static int nthread = 1;
    private static int nloop = 1;

    public static void main(String[] args) throws Exception {

	Options options = new Options();

        Option myhostport = new Option("h", "hostport", true, "Host:Port");
        myhostport.setRequired(true);
        options.addOption(myhostport);

        Option myuser = new Option("u", "user", true, "user");
        myuser.setRequired(true);
        options.addOption(myuser);

        Option mypwd = new Option("p", "password", true, "password");
        mypwd.setRequired(true);
        options.addOption(mypwd);

        Option mythreads = new Option("t", "thread", true, "num of threads");
        mythreads.setRequired(false);
        options.addOption(mythreads);

        Option myloop = new Option("l", "loop", true, "num of loop per thread");
        myloop.setRequired(false);
        options.addOption(myloop);

        CommandLineParser parser = new DefaultParser();
        HelpFormatter formatter = new HelpFormatter();
        CommandLine cmd=null;

        try {
            cmd = parser.parse(options, args);
        } catch (ParseException e) {
            System.out.println(e.getMessage());
            formatter.printHelp("JavaClient", options);

            System.exit(1);
        }

        dbhostport = cmd.getOptionValue("hostport");
        user = cmd.getOptionValue("user");
        password = cmd.getOptionValue("password");
	if ( cmd.getOptionValue("thread") != null)
        	nthread = Integer.valueOf(cmd.getOptionValue("thread"));
	if ( cmd.getOptionValue("loop") != null)
        	nloop = Integer.valueOf(cmd.getOptionValue("loop"));


        createTable();
        long mystart = System.currentTimeMillis();
        ArrayList<Thread> threads = new ArrayList<Thread>(10);;
        for (int i=0;i<nthread;i++) {
            Thread t = new Thread(new Repeater());
            t.start();
            threads.add(t);
        }

        System.out.println("Spawned threads : " + threads.size());
        for(int i=0;i<threads.size();i++) {
            ((Thread) threads.get(i)).join();
        }
        System.out.println("Exxecution - " + ttltime / 1000.0 + " seconds");
        long duration = System.currentTimeMillis() - mystart;
        System.out.println("Elapsed - " + duration / 1000.0 + " seconds");


    }

    private static void createTable() throws ClassNotFoundException, SQLException {
        Connection c = getNewConnection();

         try {
                c.setAutoCommit(false);
                Statement s = c.createStatement();
                s.executeUpdate("create database if not exists test;");
                s.executeUpdate("create table if not exists test.mytable (f1 int auto_increment not null primary key, f2 varchar(200)) engine=innodb;");
                c.commit();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        c.close();

    }

    static Connection getNewConnection( ) throws SQLException, ClassNotFoundException {
        java.util.Properties pp = new java.util.Properties();

        pp.setProperty("user", user);
        pp.setProperty("password", password);
        // black list for 60seconds
        pp.setProperty("loadBalanceBlacklistTimeout", "60000");
        pp.setProperty("autoReconnect", "false");
        Class.forName(driver);
	String myurl = baseUrl + dbhostport;
        return DriverManager.getConnection(myurl, pp);

    }

    static void executeSimpleTransaction(Connection c, int conn, int trans){
        try {
            c.setReadOnly(false);
            c.setAutoCommit(false);
            Statement s = c.createStatement();

            s.executeUpdate("insert into test.mytable (f2) values ('Connection: " + conn + ", transaction: " + trans +"');" );
            c.commit();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

     public static class Repeater implements Runnable {
            public void run() {
                for(int i=0; i < nloop; i++){
                    try {
                        Connection c = getNewConnection();
                        long mystart, myend, myduration=0;
                        for(int j=0; j < 10; j++){
                            // To register the start time
                            mystart = System.currentTimeMillis();
                            executeSimpleTransaction(c, i, j);
                            // To time the execution time and save it onto the totaltime
                            myend = System.currentTimeMillis();
                            myduration = (myend - mystart);
                            incTTL(myduration);

                            Thread.sleep(Math.round(100 * Math.random()));
                        }

                        c.close();
                        Thread.sleep(200);
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                }
            }
        }

     public synchronized static void incTTL(long m) {
         ttltime += m;
     }
}
