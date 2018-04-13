package com.wangke.util;

import java.util.Date;

public class CircleCounter {
    private int counter;
    private int frequent;

    public CircleCounter(int frequent) {
        this.counter = 0;
        this.frequent = frequent;
    }

    public void count() {
        counter++;
        if (counter % frequent == 0) {
            System.out.println(counter + " == " + new Date().toString());
        }
    }
}
