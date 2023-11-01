-- insert into dish(dish_id, store_id, dish_name, dish_description, dish_cost, dish_gradients)
-- values (1, 1, '紫薯椰奶', '生命体征维持餐', 3, '紫薯、椰奶、粥')

-- insert into canteen(canteen_id, canteen_manager_telephone, canteen_name, canteen_status)
-- values(1, 333, '1食堂', 1)

-- insert into store(store_id, canteen_id, store_manager_telephone, store_status, store_name)
-- values(1, 1, 222, 1, '温馨粥铺')

-- set foreign_key_checks = 0;

-- DROP TRIGGER TRIGGER_DELETE_NORMAL_USER

-- delete from user_info where id = 222calculate_cost

-- insert into order_dish (order_dish_index, order_id, dish_id, dish_num) values (208339, 377866, 1, 2) 

-- select store.store_name, canteen.canteen_name, store.store_status 
-- from store, store_manager, canteen 
-- where store_manager.id = 444 and store_manager.store_manager_telephone = store.store_manager_telephone and store.canteen_id = canteen.canteen_id

-- select orders.order_id, canteen.canteen_name, store.store_name, orders.normal_user_telephone, user_info.location, orders.order_time, orders.order_status 
-- from orders, canteen, store, store_manager, user_info
-- where canteen.canteen_id=orders.order_canteen_id and store.store_id=orders.order_store_id and store_manager.store_manager_telephone=store.store_manager_telephone and store_manager.id=444 and user_info.id=store_manager.id

-- insert into store values (2, 1, 444, 1, '蜜雪冰城', str_to_date('06-00-00', '%H-%i-%s'), str_to_date('17-00-00', '%H-%i-%s'), null)

-- delete from store, dish using dish inner join store where dish.store_id=store.store_id and store.store_name = '温馨粥铺'

-- delete from canteen where canteen_name = '2食堂'

-- insert into order_dish (order_dish_index, order_id, dish_id, dish_num) values (452611, 152234, 1, 8);
-- insert into order_dish (order_dish_index, order_id, dish_id, dish_num) values (452611, 152234, 2, 5)

SET SQL_SAFE_UPDATES = 1;
set foreign_key_checks = 1;
delete from user_info where id=555;