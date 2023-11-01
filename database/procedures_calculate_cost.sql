CREATE DEFINER=`root`@`localhost` PROCEDURE `calculate_cost`(in orderid long) 
begin 
 DECLARE total_cost int;
 
 set total_cost = ( 
 select sum(dish.dish_cost * order_dish.dish_num)
 from dish, order_dish 
 where order_dish.order_id=orderid and dish.dish_id=order_dish.dish_id
 ); 
 select total_cost as result; 
end 