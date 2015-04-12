package com.hackbulgaria.corejava;

public class FaultyProblem3 {
    
    public String reverseEveryWordInString(String sentence){
        String[] words = sentence.split(" ");
        sentence = "";
        for (String word: words){
            //sentence = sentence.replace(word, reverse(word));
            word = word.replace(word, reverse(word));
            sentence = sentence.concat(word + " ");
        }
        return sentence.trim();
    }

    private CharSequence reverse(String word) {
        return Utils.reverseMe(word);
    }
}
