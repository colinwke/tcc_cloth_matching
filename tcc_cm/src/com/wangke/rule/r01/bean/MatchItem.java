package com.wangke.rule.r01.bean;

import java.util.List;

public class MatchItem {
    private String itemTest;
    private String itemMatch;
    private List<String> sameWord;

    public MatchItem(String itemTest, String itemMatch, List<String> sameWord) {
        this.itemTest = itemTest;
        this.itemMatch = itemMatch;
        this.sameWord = sameWord;
    }

    public String getItemTest() {
        return itemTest;
    }

    public void setItemTest(String itemTest) {
        this.itemTest = itemTest;
    }

    public String getItemMatch() {
        return itemMatch;
    }

    public void setItemMatch(String itemMatch) {
        this.itemMatch = itemMatch;
    }

    public String toString() {
        String str = "";

        int i = 0;
        for (String s : sameWord) {
            if (i != sameWord.size() - 1) {
                str += s + "-";
            } else {
                str += s;
            }
            i++;
        }
        return itemTest + "," + itemMatch + "," + str + "," + sameWord.size();
    }
}
