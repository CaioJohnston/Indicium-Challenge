select
*
from public.orders
where order_date between TO_DATE('START_DATE','YYYY-MM-DD') AND TO_DATE('END_DATE','YYYY-MM-DD')