package com.wangke.rule.r01;

import com.wangke.core.Config;

import java.io.IOException;

public class Batch {
    public static void main(String[] args) throws IOException {
        String[] fileDataSplitUnsorted = {Config.ONLINE_TEST_ITEM_INFO, Config.OFFLINE_TRAIN_ITEM_INFO, Config.OFFLINE_TEST_ITEM_INFO};
        String[] fileFrontWord = {Config.ONLINE_TEST_FRONT_WORD, Config.OFFLINE_TRAIN_FRONT_WORD, Config.OFFLINE_TEST_FRONT_WORD};
        String[] fileDataSplitSorted = {Config.ONLINE_TEST_ITEM_INFO_SORTED, Config.OFFLINE_TRAIN_ITEM_INFO_SORTED, Config.OFFLINE_TEST_ITEM_INFO_SORTED};
        String[] fileSameWord = {Config.ONLINE_TEST_SAME_WORD, Config.OFFLINE_TRAIN_SAME_WORD, Config.OFFLINE_TEST_SAME_WORD};

        for (int i = 0; i < fileFrontWord.length; ++i) {
            Rule02 rule02 = new Rule02();
            rule02.setDataSplit(fileDataSplitUnsorted[i], fileFrontWord[i]);
            rule02.running();
        }

        for (int i = 0; i < fileFrontWord.length; ++i) {
            Rule03 rule03 = new Rule03();
            rule03.setDataSplit(fileDataSplitSorted[i], fileSameWord[i]);
            rule03.running();
        }
    }
}
