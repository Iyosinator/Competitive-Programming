#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
    int n, q;
    cin >> n >> q;

    
    vector<string> forest(n);
    for (int i = 0; i < n; ++i)
    {
        cin >> forest[i];
    }


    vector<vector<int>> prefix(n + 1, vector<int>(n + 1, 0));

    for (int row = 1; row <= n; ++row)
    {
        for (int col = 1; col <= n; ++col)
        {
            int current_cell_tree = (forest[row - 1][col - 1] == '*') ? 1 : 0;
            int top_prefix = prefix[row - 1][col];
            int left_prefix = prefix[row][col - 1];
            int overlap_prefix = prefix[row - 1][col - 1];

            prefix[row][col] = current_cell_tree + top_prefix + left_prefix - overlap_prefix;
        }
    }

    for (int i = 0; i < q; ++i)
    {
        int y1, x1, y2, x2;
        cin >> y1 >> x1 >> y2 >> x2;

        int total_area = prefix[y2][x2];
        int top_strip = prefix[y1 - 1][x2];
        int left_strip = prefix[y2][x1 - 1];
        int overlap_corner = prefix[y1 - 1][x1 - 1];

        int trees_in_rectangle = total_area - top_strip - left_strip + overlap_corner;

        cout << trees_in_rectangle << "\n";
    }

    return 0;
}
