package com.wangke._test.objectlize;

public class BoughtCreate implements Objectlizer {

    @Override
    public Object objectlize(String[] elements) {
        return new Bought(elements);
    }
}
