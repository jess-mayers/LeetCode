from typing import List


def generate(numRows: int) -> List[List[int]]:
    res = [[1]]
    for i in range(1, numRows):
        row = [1]
        prev_row = res[i-1]
        for j in range(1, i):
            row.append(prev_row[j-1] + prev_row[j])
        row.append(1)
        res.append(row)
    return res

if __name__ == '__main__':
    print(generate(5))