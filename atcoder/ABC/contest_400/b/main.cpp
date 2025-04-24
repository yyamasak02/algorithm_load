#include <iostream>

int main()
{
    long long int n, m;
    std::cin >> n >> m;
    long long int ans = 0;
    long long int tmp = 1;
    long long limit = 1e9;

    for (int i = 0; i <= m; i++)
    {
        ans += tmp;
        if (ans > limit)
        {
            std::cout << "inf" << std::endl;
            return 0;
        }
        tmp *= n;
    }
    std::cout << ans << std::endl;
    return 0;
}