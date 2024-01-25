import pytest
from code1 import total



def test_total_raises_exception_on_non_list_arguments():
    with pytest.raises(TypeError):
         total(1)
