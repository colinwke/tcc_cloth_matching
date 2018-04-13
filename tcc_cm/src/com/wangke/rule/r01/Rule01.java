package com.wangke.rule.r01;

import com.wangke.core.Config;
import com.wangke.rule.r01.bean.ItemInfo;
import com.wangke.rule.r01.bean.ItemInfoConverter;
import com.wangke.util.CircleCounter;
import com.wangke.util.csv.CsvUtil;
import com.wangke.util.MapUtil;
import com.wangke.util.Timestamp;
import com.wangke.util.csv.SOConverter;

import java.io.IOException;
import java.util.*;

/**
 * 通过商品描述的相关性进行匹配
 * <p>
 * 通过计算商品描述前几位词相同进行排序选择
 */


public class Rule01 {
    private List<ItemInfo> itemInfoList;
    private List<ItemInfo> testItemInfoList;

    private String dataSplitFileIn = Config.ONLINE_TEST_ITEM_INFO;
    private String dataSplitFileOut = Config.ONLINE_TEST_FRONT_WORD_COUNT;

    public void setDataSplit(String fileIn, String fileOut) {
        this.dataSplitFileIn = fileIn;
        this.dataSplitFileOut = fileOut;
    }

    private void initData() throws IOException {
        CsvUtil csvUtil = CsvUtil.getCsvUtil();
        SOConverter converter = new ItemInfoConverter();
        itemInfoList = new LinkedList<>();
        testItemInfoList = new LinkedList<>();
        csvUtil.read(Config.ITEM_INFO, itemInfoList, converter, 1);
        csvUtil.read(dataSplitFileIn, testItemInfoList, converter, 1);
    }

    public void running() throws IOException {
        Timestamp ts = new Timestamp();

        // 读取数据
        initData();

        ts.cut("load data success!");

        // 进行计算
        // 对于每个训练
        List<MatchCount> matchItemList = new LinkedList<>();
        CircleCounter circleCounter = new CircleCounter(500);
        for (ItemInfo testItem : testItemInfoList) {
            circleCounter.count();
            Map<String, Integer> map = new HashMap<>();
            // 对于每个商品
            for (ItemInfo cmpItem : itemInfoList) {
                // 不相同的类别
                if (!testItem.getItemCategory().equals(cmpItem.getItemCategory())) {
                    // 进行对比计算
                    int count = 0;
                    for (int k = 0; k < Math.min(testItem.getItemDepict().length, cmpItem.getItemDepict().length); ++k) {
                        if (!testItem.getItemDepict()[k].equals(cmpItem.getItemDepict()[k])) {
                            break;
                        } else {
                            count++;
                        }
                    }
                    if (count > 0) {
                        map.put(cmpItem.getItemId(), count);
                    }
                }
            }
            map = MapUtil.sortByValue(map);
            // 只保留前面的500个
            int itemCount = 0;
            for (String key : map.keySet()) {
                if (itemCount < 500) {
                    itemCount++;
                    matchItemList.add(new MatchCount(testItem.getItemId(), key, map.get(key)));
                } else {
                    break;
                }
            }
        }

        ts.cut("count success!");

        // 写入结果
        CsvUtil csvUtil = CsvUtil.getCsvUtil();
        String columns = "item_id_x,item_id_y,front_word_count";
        csvUtil.write(matchItemList, dataSplitFileOut, columns);

        ts.end();

    }

    public static void main(String[] args) throws IOException {
        Rule01 rule = new Rule01();

        rule.running();

    }

    class MatchCount {
        public String itemTest;
        public String itemCmp;
        public int count;

        public MatchCount(String itemTest, String itemCmp, int count) {
            this.itemTest = itemTest;
            this.itemCmp = itemCmp;
            this.count = count;
        }

        public String toString() {
            return itemTest + "," + itemCmp + "," + count;
        }
    }

}
