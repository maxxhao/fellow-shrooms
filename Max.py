import numpy as np

def test_function(a, b):
  x = np.random.randn(a, b)
  return x
  
if __name__ == "__main__":
  a = 3
  b = 3
  x = test_function(a, b)
  
  print(x)
