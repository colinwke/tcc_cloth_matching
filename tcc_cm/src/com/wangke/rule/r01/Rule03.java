package com.wangke.rule.r01;

import com.wangke.core.Config;
import com.wangke.rule.r01.bean.ItemInfo;
import com.wangke.rule.r01.bean.ItemInfoConverter;
import com.wangke.rule.r01.bean.MatchItemSameWord;
import com.wangke.util.CircleCounter;
import com.wangke.util.MapUtil;
import com.wangke.util.Timestamp;
import com.wangke.util.csv.CsvUtil;
import com.wangke.util.csv.SOConverter;

import java.io.IOException;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

/**
 * 通过商品之间的描述相似进行统计
 * <p>
 * 通过商品描述总的相同个数的词语
 * 这里的商品描述需要先进行排序（为了减少计算时间）
 */

public class Rule03 {
    private List<ItemInfo> itemInfoList;
    private List<ItemInfo> testItemInfoList;

    private String dataSplitFileIn = Config.ONLINE_TEST_ITEM_INFO_SORTED;
    private String dataSplitFileOut = Config.ONLINE_TEST_SAME_WORD;

    public void setDataSplit(String fileIn, String fileOut) {
        this.dataSplitFileIn = fileIn;
        this.dataSplitFileOut = fileOut;
    }

    private void initData() throws IOException {
        CsvUtil csvUtil = CsvUtil.getCsvUtil();
        SOConverter converter = new ItemInfoConverter();
        itemInfoList = new LinkedList<>();
        testItemInfoList = new LinkedList<>();
        csvUtil.read(Config.ITEM_INFO_SORTED, itemInfoList, converter, 1);
        csvUtil.read(dataSplitFileIn, testItemInfoList, converter, 1);
    }


    private List<String> calcSimilarity(String[] d1, String[] d2) {
        List<String> list = new LinkedList<>();

        int i = 0;
        int j = 0;
        while ((i < d1.length) && (j < d2.length)) {
            if (d1[i].compareTo(d2[j]) > 0) {
                // d1[i] > d2[j]
                j++;
            } else if (d1[i].compareTo(d2[j]) < 0) {
                i++;
            } else {
                list.add(d1[i]);
                i++;
                j++;
            }
        }

        return list;
    }

    public void running() throws IOException {
        Timestamp ts = new Timestamp();

        // 读取数据
        initData();

        ts.cut("load data success!");

        // 进行计算
        // 对于每个训练
        List<MatchItemSameWord> matchItemList = new LinkedList<>();
        CircleCounter circleCounter = new CircleCounter(1000);
        for (ItemInfo testItem : testItemInfoList) {
            circleCounter.count();
            Map<String, Integer> map = new HashMap<>(); // 计数，用于排序
            Map<String, List<String>> mapSameWord = new HashMap<>(); // 存值
            // 对于每个商品
            for (ItemInfo cmpItem : itemInfoList) {
                // 不相同的类别
                if (!testItem.getItemCategory().equals(cmpItem.getItemCategory())) {
                    List<String> sameWord = calcSimilarity(testItem.getItemDepict(), cmpItem.getItemDepict());
                    if (sameWord.size() > 0) {
                        map.put(cmpItem.getItemId(), sameWord.size());
                        mapSameWord.put(cmpItem.getItemId(), sameWord);
                    }
                }
            }
            map = MapUtil.sortByValue(map);
            // 只保留前面的500个
            int itemCount = 0;
            for (String key : map.keySet()) {
                if (itemCount < 500) {
                    itemCount++;
                    matchItemList.add(new MatchItemSameWord(testItem.getItemId(), key, mapSameWord.get(key)));
                } else {
                    break;
                }
            }
        }

        ts.cut("count success!");

        // 写入结果
        CsvUtil csvUtil = CsvUtil.getCsvUtil();
        String columns = "item_id_x,item_id_y,same_word,same_word_count";
        csvUtil.write(matchItemList, dataSplitFileOut, columns);

        ts.end();

    }

    public static void main(String[] args) throws IOException {
        Rule03 rule = new Rule03();

        rule.running();

    }
}
