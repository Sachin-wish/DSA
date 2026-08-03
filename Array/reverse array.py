
def reverseArray(arr):
    arr.reverse()

if __name__ == "__main__":
    arr = [1, 4, 3, 2, 6, 5]

    reverseArray(arr)
  
    print(" ".join(map(str, arr)))