package com.hackbulgaria.corejava;

public class FaultyProblem6 {
    public static long pow(int a, int b) {
        if (b == 0 || a == 1){
            return 1;
        }
        if (b == 1){
            return a;
        }
        if (b % 2 == 1) {
            return a * pow(a*a, (b - 1)/2);
        } else {
            long power = pow(a, b / 2);
            return power * power;
        }
    }
}
