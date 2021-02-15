import java.util.*;
public class Warikan{
	public static void main(String[] args){
		System.out.print("料金を入力>>");
		int price=new Scanner(System.in).nextInt();
		System.out.print("人数を入力>>");
		int number=new Scanner(System.in).nextInt();
		int payment=price/number;
		System.out.println("お支払いは"+payment+"円です");
	}
}
