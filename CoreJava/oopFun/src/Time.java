
public class Time {
    private int date;
    private int month;
    private int year;
    private int hours;
    private int minutes;
    private int seconds;
    
    Time(int d, int m, int y, int h, int min, int s){
        date = d;
        month = m;
        year = y;
        hours = h;
        minutes = min;
        seconds = s;
    }
    
    @Override
    public String toString(){
        return String.format("%02d:%02d:%02d %02d.%02d.%d", hours, minutes, seconds, date, month, year);
    }
}
