package com.wangke.rule.r04;

import com.wangke.core.Config;
import com.wangke.rule.r04.bean.BoughtCase;
import com.wangke.rule.r04.bean.BoughtCaseCreator;
import com.wangke.util.csv.CsvUtil;
import com.wangke.util.csv.SOConverter;

import java.io.IOException;
import java.util.LinkedList;
import java.util.List;

/**
 * 通过用户的购买记录生成匹配对
 * 1. 通过（用户， 日期）进行group
 * 2. 找出group中的测试商品
 * 3. 对每个group生成匹配对
 * 3. 通过
 */

public class Rule04 {
    private String fileBH = Config.FILE_USER_BOUGHT_HISTORY;
    private List<BoughtCase> bh = new LinkedList<>();

    private void initData() throws IOException {
        CsvUtil csvUtil = CsvUtil.getCsvUtil();
        SOConverter converter = new BoughtCaseCreator();
        csvUtil.read(fileBH, bh, converter, 1);
    }


    public static void main(String[] args) throws IOException {
        Rule04 rule04 = new Rule04();
        rule04.initData();

    }

}
