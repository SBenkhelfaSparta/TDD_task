# Creating and testing modulo

```python
class Modulo:

    def mod(self, x, y):
        return x%y

    def positive(self, x, y):
        if (x >= 0) and (y >= 0):
            return True
        else:
            return False
```

This is the class and method for modulo (%) along with a method to check for positive values

We need to test if it is working first, so to do that I used an example input of 10%2 with an expected output of 0:

```python
self.assertEqual(self.modu.mod(10, 2), 0)
```

I also created two other tests to check if the positive() method is working:

```python
self.assertEqual(self.modu.positive(-21, 9), False)
self.assertEqual(self.modu.positive(21, 9), True)
```