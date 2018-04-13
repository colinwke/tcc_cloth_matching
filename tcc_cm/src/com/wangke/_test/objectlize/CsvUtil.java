package com.wangke._test.objectlize;

import java.io.*;
import java.util.List;


public class CsvUtil {
    private static CsvUtil csvUtil = new CsvUtil();

    private CsvUtil() {
    }

    public static CsvUtil getCsvUtil() {
        return csvUtil;
    }

    private BufferedReader readDataFile(String fileName) throws IOException {
        BufferedReader reader = null;

        try {
            reader = new BufferedReader(new FileReader(fileName));
        } catch (FileNotFoundException e) {
            // wasn't open, so don't close it
            System.err.println("Could not open " + fileName);
            System.exit(0);
        }

        return reader;
    }

    /**
     * 文件读入
     * 无格式文件读入
     */
    public void read(String fileName, List list, Objectlizer objectlizer, int numFirst) throws IOException {
        BufferedReader reader = readDataFile(fileName);

        // jump to data line
        for (int i = 0; i < numFirst; ++i) {
            reader.readLine();
        }

        String line = null;

        while ((line = reader.readLine()) != null) {
            String[] elements = line.split(",");
            list.add(objectlizer.objectlize(elements));
        }
    }

    /**
     * 文件写出
     */
    public <E> void write(List<E> list, String fileName, String columns) {
        try {
            FileWriter fileWriter = new FileWriter(fileName);
            BufferedWriter bufferedWriter = new BufferedWriter(fileWriter);
            PrintWriter printWriter = new PrintWriter(bufferedWriter);

            printWriter.println(columns);

            for (E e : list) {
                printWriter.println(e.toString());
            }

            printWriter.close();

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
