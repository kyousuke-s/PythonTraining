public class ArgsTest{
	public static void main(String[] args){
		addNums(1,2,3,4);
		addNums(1,2,3,4,5,6,7);
		addNums(5);
	}
	static void addNums(int n,int... nums){//int n は必須引数
		int sum=n;
		for(int i:nums){
			sum+=i;
		}
		System.out.println("合計は"+sum+"です");
	}
}
