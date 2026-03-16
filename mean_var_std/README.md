# Matrix Statistics Calculator

A Python function that computes descriptive statistics on a 9-element list interpreted as a 3×3 matrix.

## Requirements

- Python 3.x
- NumPy

Install dependency:
```bash
pip install numpy
```

## Usage

```python
from calculate import calculate

result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
print(result)
```

## Input

A flat list of **exactly 9 numbers**. It is reshaped internally into a 3×3 matrix:

```
[0, 1, 2, 3, 4, 5, 6, 7, 8]

→  [[0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]]
```

Raises a `ValueError` if the list does not contain exactly 9 elements.

## Output

Returns a dictionary with the following keys:

| Key        | Description                          |
|------------|--------------------------------------|
| `mean`     | Arithmetic mean                      |
| `variance` | Population variance                  |
| `std`      | Population standard deviation        |
| `max`      | Maximum value                        |
| `min`      | Minimum value                        |
| `sum`      | Sum of values                        |

Each key maps to a list of **three values**:

```
[along columns (axis=0), along rows (axis=1), over flattened matrix]
```

### Example Output

```python
calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])

{
  'mean':     [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.666..., 0.666..., 0.666...], 6.666...],
  'std':      [[2.449, 2.449, 2.449], [0.816, 0.816, 0.816], 2.581],
  'max':      [[6, 7, 8], [2, 5, 8], 8],
  'min':      [[0, 1, 2], [0, 3, 6], 0],
  'sum':      [[9, 12, 15], [3, 12, 21], 36]
}
```

## Error Handling

```python
calculate([1, 2, 3])
# ValueError: List must contain nine numbers.
```
