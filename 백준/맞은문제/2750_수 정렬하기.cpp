#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
using namespace std;

int main()
{
	srand(static_cast<unsigned int>(std::time(0)));	//난수 생성 (srand())

	vector<int> num;	//벡터 선언

	int size = 0;		//벡터 사이즈 변수

	cin >> size;

	for (int i = 0; i < size; i++)
	{
		int number;

		cin >> number;

		num.push_back(number);
	}
	
	for (int i = 0; i < size; i++)	//num[] 선택 정렬 시작
	{
		for (int j = i; j < size; j++)
		{
			if (num[i] > num[j])
			{
				int temp = num[j];
				num[j] = num[i];
				num[i] = temp;
			}
		}
	}

	//출력
	for (int i = 0; i < size; i++)
	{
		cout << num[i] << endl;
	}

	return 0;
}