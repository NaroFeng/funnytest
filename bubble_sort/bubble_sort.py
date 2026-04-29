"""
冒泡排序 (Bubble Sort)
通过重复遍历列表，比较相邻元素并交换位置，直到列表排序完成
时间复杂度: O(n²)
空间复杂度: O(1)
"""


def bubble_sort(arr):
    """
    冒泡排序函数
    
    参数:
        arr: 待排序的列表
    
    返回:
        排序后的列表
    """
    n = len(arr)
    
    # 外层循环: 需要遍历 n 次
    for i in range(n):
        
        # 内层循环: 比较相邻元素
        # n - i - 1: 每次遍历后,最大的元素已经排到最后,不需要再比较
        for j in range(0, n - i - 1):
            
            # 如果前一个元素大于后一个元素,则交换位置
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr


if __name__ == "__main__":
    # 测试数据
    numbers = [64, 34, 25, 12, 22, 11, 90]
    
    print("原始数组:", numbers)
    sorted_numbers = bubble_sort(numbers)
    print("排序后:", sorted_numbers)