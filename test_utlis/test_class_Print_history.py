from utlis.class_Print_history import Print_history
import datetime
from utlis import f



def test_Print_history():
    assert Print_history(f.import_json()) == True
