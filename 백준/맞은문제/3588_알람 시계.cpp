#include <iostream>
using namespace std;

int main()
{
	int a, b;

	cin >> a;
	cin >> b;

	cout << (b % 10) * a << endl;   //(3)
	cout << (((b % 100) - (b % 10)) / 10) * a << endl;   //(4)
	cout << (((b % 1000) - (b % 100)) / 100) * a << endl;   //(5)
	cout << a * b << endl;   //(6)

	return 0;
}