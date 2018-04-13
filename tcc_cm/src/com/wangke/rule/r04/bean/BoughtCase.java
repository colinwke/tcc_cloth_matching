package com.wangke.rule.r04.bean;

import java.util.Arrays;

public class BoughtCase {
    private String userId;
    private String itemId;
    private int date;
    private int label;

    public BoughtCase(String line) {
        String[] elements = line.split(",");

        this.userId = elements[0];
        this.itemId = elements[1];
        this.date = Integer.parseInt(elements[2]);
        this.label = Integer.parseInt(elements[3]);
    }

    public String toString() {
        return userId + "," +
                itemId + "," +
                date + "," +
                label;
    }
}
