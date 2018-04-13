package com.wangke._test;

import com.wangke.util.csv.CsvUtil;

import java.util.*;

/**
 * Created by colin on 2017/3/22.
 */
public class MapTest {
    public static void main(String[] args) {
//        Map<Integer, Integer> map = new HashMap<>();
//
//        map.put(1, 3);
//        map.put(2, 9);
//        map.put(3, 2);
//        map.put(5, 0);
//
//        System.out.println(map.toString());
//        map = MapUtil.sortByValue(map);
//        System.out.println(map.toString());

        List<Integer> list = new LinkedList<>();

        String columns = "col";

        for (int i = 0; i < 10; ++i) {
            list.add(i * 7 + 6);
        }

        CsvUtil csvUtil = CsvUtil.getCsvUtil();
        csvUtil.write(list, "csvUtilTest.txt", columns);

    }

}
