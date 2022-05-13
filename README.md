# pyqt-get-selected-filter
Get selected filter string for QFileDialog

## Setup
`python -m pip install pyqt-get-selected-filter`

## Example
```python
### code start ###
from pyqt_get_selected_filter import getSelectedFilter

lst = ['.bmp', '.jpg', '.jpeg', '.gif', '.png']
print(getSelectedFilter(lst))
### code end ###

>> (*.bmp *.jpg *.jpeg *.gif *.png) # result
```
