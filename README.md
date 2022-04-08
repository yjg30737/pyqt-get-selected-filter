# pyqt-get-selected-filter
Get selected filter string for QFileDialog

## Example
Code Sample
```python
from pyqt_get_selected_filter import getSelectedFilter

lst = ['.bmp', '.jpg', '.jpeg', '.gif', '.png']
print(getSelectedFilter(lst))
```

Result
`(*.bmp *.jpg *.jpeg *.gif *.png)`
