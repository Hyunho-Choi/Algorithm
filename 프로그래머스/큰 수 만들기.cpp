#include <string>
#include <vector>

using namespace std;

string solution(string number, int k) {
	string answer = "";

	int howLong = number.size();
	int ansSize = howLong - k;

	for (int i = 0; i < ansSize; i++)
	{
		int searchSize = number.size();
		searchSize -= (ansSize-i);
		int search;
		int max = 0;
		int bigj = 0;

		for (int j = 0; j < searchSize+1; j++)
		{
			if (number[j] > max)
			{
				max = number[j];
				bigj = j;
			}
		}
		search = max;
		number.erase(0, bigj+1);
		answer += (char)search;
	}
	return answer;
}
