package com.wangke.rule.r01.bean;


public class ItemInfo {
    private String itemId;
    private String itemCategory;
    private String[] itemDepict;

    public ItemInfo(String line) {
        String[] elements = line.split(",");

        this.itemId = elements[0];
        this.itemCategory = elements[1];
        this.itemDepict = elements[2].split("-");
    }

    public String getItemId() {
        return itemId;
    }

    public void setItemId(String itemId) {
        this.itemId = itemId;
    }

    public String getItemCategory() {
        return itemCategory;
    }

    public void setItemCategory(String itemCategory) {
        this.itemCategory = itemCategory;
    }

    public String[] getItemDepict() {
        return itemDepict;
    }

    public void setItemDepict(String[] itemDepict) {
        this.itemDepict = itemDepict;
    }

    public String toString() {
        String str = "";
        for (int i = 0; i < itemDepict.length; ++i) {
            if (i < (itemDepict.length - 1)) {
                str = str + itemDepict[i] + "-";
            } else {
                str += itemDepict[i];
            }
        }
        str = itemId + "," + itemCategory + "," + str;

        return str;
    }
}