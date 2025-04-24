#include <iostream>

int main()
{
    int x;

    std::cin >> x;

    if (400 % x == 0)
    {
        std::cout << 400 / x << std::endl;
    }
    else
    {
        std::cout << -1 << std::endl;
    }
}