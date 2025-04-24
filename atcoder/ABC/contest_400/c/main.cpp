#include <iostream>
#include <vector>

int main()
{
    long long int n;
    std::cin >> n;

    long long int left, right, middle, answer;
    const long long int mod = (long long)1e9;

    left = 0;
    answer = 0;
    right = mod;
    while (left + 1 < right)
    {
        middle = (left + right) / 2;
        if (middle * middle * 2 <= n)
        {
            left = middle;
        }
        else
        {
            right = middle;
        }
    }
    answer += left;
    left = 0;
    right = mod;
    while (left + 1 < right)
    {
        middle = (left + right) / 2;
        if (middle * middle * 4 <= n)
        {
            left = middle;
        }
        else
        {
            right = middle;
        }
    }
    answer += left;
    std::cout << answer << std::endl;
    return 0;
}