package com.wangke.rule.r04.bean;

import com.wangke.util.csv.SOConverter;

public class BoughtCaseCreator implements SOConverter {
    @Override
    public Object string2object(String line) {
        return new BoughtCase(line);
    }
}
