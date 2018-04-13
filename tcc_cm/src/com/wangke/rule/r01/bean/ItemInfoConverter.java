package com.wangke.rule.r01.bean;

import com.wangke.util.csv.SOConverter;

public class ItemInfoConverter implements SOConverter {
    @Override
    public Object string2object(String line) {
        return new ItemInfo(line);
    }
}
