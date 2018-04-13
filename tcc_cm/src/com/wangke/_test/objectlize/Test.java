package com.wangke._test.objectlize;

import com.wangke.core.Config;

import java.io.IOException;
import java.util.LinkedList;
import java.util.List;

public class Test {

    public static void main(String[] args) throws IOException {
        String data = Config.BOUGHT_HISTORY;
        BoughtCreate create = new BoughtCreate();
        List<Bought> list = new LinkedList<>();

        CsvUtil csvUtil = CsvUtil.getCsvUtil();
        csvUtil.read(data, list, create, 1);


        int i = 0;
        for (Bought bought : list) {
            i++;
            if (i > 5) {
                break;
            }
            System.out.println(bought.toString());
        }


    }
}
