# funnytest

存放各種有趣演算法的測試專案。

## 專案內容

### bubble_sort

冒泡排序 (Bubble Sort) 的 Python 實作。

#### 演算法說明

透過重複遍歷列表，比較相鄰元素並交換位置，直到列表排序完成。

#### 複雜度

- 時間複雜度: O(n²)
- 空間複雜度: O(1)

#### 使用方式

```python
from bubble_sort import bubble_sort

numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubble_sort(numbers)
print(sorted_numbers)  # [11, 12, 22, 25, 34, 64, 90]
```

## 授權

MIT License