import numpy as np

def test_function():
  x = np.random.randn(3,3)
  return x
  
if __name__ == "__main__":
  a = 3
  b = 3
  x = test_functional(a, b)
  
  print(x)
