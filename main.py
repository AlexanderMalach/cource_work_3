from utlis.class_print_history import PrintHistory
from utlis.functions import sorted_date
from utlis.tools import create_logger


logger = create_logger()
sort_list = sorted_date()

for i in range(5):
    copy = PrintHistory(sort_list, i)
    logger.info(
        f"\n{copy.date_print()} {copy.print_line('description')}\n{(copy.account_code('from'))} ->"
        f"{copy.account_code('to')}\n{copy.currency()}\n",
    )
