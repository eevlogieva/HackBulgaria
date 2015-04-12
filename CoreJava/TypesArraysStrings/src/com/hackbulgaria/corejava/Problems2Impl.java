package com.hackbulgaria.corejava;
import java.lang.reflect.Array;
import java.util.Arrays;

public class Problems2Impl implements Problems2 {

    @Override
    public boolean isOdd(int number) {
        return number % 2 == 1 || number % 2 == -1;
    }

    @Override
    public boolean isPrime(int number) {
        for (int i = 2; i < number / 2; i++){
            if (number % i == 0){
                return false;
            }
        }
        return true;
    }

    @Override
    public int min(int... array) {
        int minElem = array[0];
        for (int i = 0; i < array.length; i++){
            if (array[i] < minElem){
                minElem = array[i];
            }
        }
        return minElem;
    }

    @Override
    public int kthMin(int k, int[] array) {
        int minElem = array[0], indexMin = 0;
        for (int i = 0; i < array.length; i++){
            for (int j = i; j < array.length; j++){
                if (array[j] < minElem){
                    indexMin = j;
                }
            }
            int temp = array[0];
            array[0] = array[indexMin];
            array[indexMin] = temp;
        }
        return array[k-1];
    }

    @Override
    public float getAverage(int[] array) {
        float sum = 0;
        for (int i = 0; i < array.length; i++){
            sum += array[i];
        }
        return sum / array.length;
    }

    @Override
    public long getSmallestMultiple(int upperBound) {
        boolean isFound = false;
        long i = upperBound;
        while (! isFound){
            int j;
            for (j = 1; j < upperBound; j++){
                if (i % j != 0){
                    break;
                }
            }
            if(j == upperBound){
                isFound = true;
            }
            i++;
        }
        return i - 1;
    }
    
    @Override
    public long getLargestPalindrome(long N) {
        boolean found = false;
        while (! found){
            found = isPalindrome(N-1);
            N -= 1;
        }
        return N;
    }

    @Override
    public int[] histogram(short[][] image) {
        int[] result;
        result = new int[256];
        for (int index = 0; index <= 255; index++){
            int counter = 0;
            for (int i = 0; i < image.length; i++){
                for (int j = 0; j < image[0].length; j++){
                    if (image[i][j] == (short) index){
                        counter ++;
                    }
                }
            }
            result[index] = counter;
        }
        return result;
    }

    public long fact(long n) {
        if (n == 1){
            return 1;
        }
        return n * fact(n-1);
    }
    
    @Override
    public long doubleFac(int n) {
        return fact(fact(n));
    }

    @Override
    public long kthFac(int k, int n) {
        long result = fact(n);
        for(int i = 1; i <k; i++){
            result = fact(result);
        }
        return result;
    }

    @Override
    public int getOddOccurrence(int[] array) {
        Arrays.sort(array);
        int counter = 1;
        for(int i = 1; i < array.length; i++){
            if(array[i-1] == array[i]){
                counter++;
            }
            else{
                if(counter % 2 != 0){
                    return array[i-1];
                }
                else{
                    counter = 1;
                }
            }
        }
        return 0;
    }

    @Override
    public long pow(int a, int b) {
        if (a == 0){
            return 0;
        }
        if (b == 0 || a == 1){
            return 1;
        }
        if (b % 2 == 0){
            return pow(a*a, b/2);
        }
        else{
            return a * pow(a*a, (b-1)/2);
        }
    }

    @Override
    public long maximalScalarSum(int[] a, int[] b) {
        Arrays.sort(a);
        Arrays.sort(b);
        long maxScalar = 0;
        for(int i = 0; i < a.length; i++){
            maxScalar += a[i]*b[i];
        }
        return maxScalar;
    }

    @Override
    public int maxSpan(int[] array) {
        int maxSpan = 1;
        int[] visited = new int[array.length];
        for (int i = 0; i < array.length; i++){
            boolean isVisited = false;
            for(int k = 0; k < visited.length; k++){
                if (visited[k] == array[i]){
                    isVisited = true;
                    break;
                }
            }
            if (! isVisited){
                for(int j = array.length - 1; j >i; j--){
                    if(array[j] == array[i] && j - i + 1> maxSpan){
                        maxSpan = j - i + 1;
                    }
                }
            }
        }
        return maxSpan;
    }

    @Override
    public int sumArray(int start, int end, int[] array){
        int sum = 0;
        for (int i = start; i <= end; i++){
            sum += array[i];
        }
        return sum;
    }
    @Override
    public boolean canBalance(int[] array) {
        for (int i = 0; i < array.length; i++){
            if(sumArray(0, i, array) == sumArray(i+1, array.length - 1, array)){
                return true;
            }
        }
        return false;
    }

    @Override
    public int[][] rescale(int[][] original, int newWidth, int newHeight) {
        
        return null;
    }

    @Override
    public String reverseMe(String argument) {
        // TODO Auto-generated method stub
        return null;
    }

    @Override
    public String copyEveryChar(String input, int k) {
        // TODO Auto-generated method stub
        return null;
    }

    @Override
    public String reverseEveryWord(String arg) {
        // TODO Auto-generated method stub
        return null;
    }

    @Override
    public boolean isPalindrome(String argument) {
        // TODO Auto-generated method stub
        return false;
    }

    @Override
    public boolean isPalindrome(long N) {
        String number = String.valueOf(N);
        for (int i = 0; i <= number.length() / 2; i ++){
            if (number.charAt(i) != number.charAt(number.length() - 1 - i)){
                return false;
            }
        }
        return true;
    }

    @Override
    public int getPalindromeLength(String input) {
        // TODO Auto-generated method stub
        return 0;
    }

    @Override
    public int countOcurrences(String needle, String haystack) {
        // TODO Auto-generated method stub
        return 0;
    }

    @Override
    public String decodeURL(String input) {
        // TODO Auto-generated method stub
        return null;
    }

    @Override
    public int sumOfNumbers(String input) {
        // TODO Auto-generated method stub
        return 0;
    }

    @Override
    public boolean areAnagrams(String A, String B) {
        // TODO Auto-generated method stub
        return false;
    }

    @Override
    public boolean hasAnagramOf(String string, String string2) {
        // TODO Auto-generated method stub
        return false;
    }

}
