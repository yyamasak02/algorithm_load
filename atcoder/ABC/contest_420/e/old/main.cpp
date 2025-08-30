#include <iostream>
#include <vector>

class UnionFind {
private:
    std::vector<int> par;
    std::vector<int> siz;
    std::vector<int> blacks;
    std::vector<bool> colors;

public:
    UnionFind(int n): par(n+1, -1), siz(n+1, 1), blacks(n+1, 0), colors(n+1, false) {}

    int root(int v) {
        while(this->par[v] != -1)
            v = this->par[v];
        return v;
    }

    void unite(int u, int v) {
        int uRoot = this->root(u);
        int vRoot = this->root(v);

        if (uRoot == vRoot) return;
        if (uRoot > vRoot) {
            this->par[vRoot] = uRoot;
            this->siz[uRoot] += vRoot;
            this->blacks[uRoot] += this->blacks[vRoot];
        } else {
            this->par[uRoot] = vRoot;
            this->siz[vRoot] += uRoot;
            this->blacks[vRoot] += this->blacks[uRoot];
        }
    }

    void add(int v) {
        int val = 1;
        if (this->colors[v] == true)
            val = -1;
        this->colors[v] = !this->colors[v];
        this->blacks[this->root(v)] += val;
    }

    bool hasBlack(int v) {
        return this->blacks[this->root(v)] > 0;
    }

    void ft_print() {
        std::cout << "par: ";
        for (int v : par) {
            std::cout << v << " ";
        }
        std::cout << std::endl;
    }
};

int main() {
    int n, q;

    std::cin >> n >> q;
    UnionFind uf = UnionFind(n);
    for (int i = 0; i < q; i++) {
        int query;
        std::cin >> query;
        if (query == 1) {
            int u, v;
            std::cin >> u >> v;
            uf.unite(u, v);
        } else if (query == 2) {
            int u;
            std::cin >> u;
            uf.add(u);
        } else {
            int u;
            std::cin >> u;
            if (uf.hasBlack(u) == true) {
                std::cout << "Yes" << std::endl;
            } else {
                std::cout << "No" << std::endl;
            }
        }
    }

    return;
}
