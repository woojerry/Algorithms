#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;

int main()
{
    int N;
    cin >> N;

    vector<int> nums;
    vector<int> sums;

    for (int i = 0; i < N; i++)
    {
        int num;
        cin >> num;
        nums.push_back(num);
    }
    sort(nums.begin(), nums.end());

    for (int i = 0; i < N; i++)
    {
        for (int j = i + 1; j < N; j++)
        {
            sums.push_back(nums[i] + nums[j]);
        }
    }
    sort(sums.begin(), sums.end());

    map<int, int> find;
    for (int i = 0; i < N; i++)
    {
        for (int j = i + 1; j < N; j++)
        {
            find[nums[i] - nums[j]] = max(find[nums[j] - nums[i], nums[j]]);
        }
    }

    int answer = 0;
    for (auto &i : find)
    {
        if (find.count(i))
        {
            answer = max(answer, find[i]);
        }
    }
    cout << answer;
}