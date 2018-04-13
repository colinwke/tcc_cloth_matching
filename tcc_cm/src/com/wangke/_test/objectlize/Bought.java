package com.wangke._test.objectlize;

public class Bought {
    private String userId;
    private String itemId;
    private String date;

    public Bought(String[] elements) {
        this.userId = elements[0];
        this.itemId = elements[1];
        this.date = elements[2];
    }

    public String getUserId() {
        return userId;
    }

    public void setUserId(String userId) {
        this.userId = userId;
    }

    public String getItemId() {
        return itemId;
    }

    public void setItemId(String itemId) {
        this.itemId = itemId;
    }

    public String toString() {
        return userId + "," + itemId + "," + date;
    }
}
