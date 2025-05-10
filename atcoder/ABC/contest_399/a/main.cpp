#include <iostream>

int main()
{
    int test;
    std::string a;
    std::string b;
    int res = 0;

    std::cin >> test;
    std::cin >> a;
    std::cin >> b;
    for (int i = 0; i < test; ++i)
    {
        if (a[i] != b[i])
        {
            res++;
        }
    }
    std::cout << res << std::endl;
}