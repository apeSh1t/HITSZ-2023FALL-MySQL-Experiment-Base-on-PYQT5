CREATE VIEW VIEW_DISH_LIST (canteen_img , canteen_name , store_name , dish_name , dish_cost , dish_gradients , dish_description) AS
    SELECT 
        canteen.canteen_img,
        canteen.canteen_name,
        store.store_name,
        dish.dish_name,
        dish.dish_cost,
        dish.dish_gradients,
        dish.dish_description
    FROM
        canteen,
        store,
        dish
    WHERE
        canteen.canteen_id = store.canteen_id
            AND store.store_id = dish.store_id