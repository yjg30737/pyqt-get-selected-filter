# pyqt-get-selected-filter
Get selected filter string for QFileDialog

## Example
```python
### code start ###
from pyqt_get_selected_filter import getSelectedFilter

lst = ['.bmp', '.jpg', '.jpeg', '.gif', '.png']
print(getSelectedFilter(lst))
### code end ###

>> (*.bmp *.jpg *.jpeg *.gif *.png) # result
```
