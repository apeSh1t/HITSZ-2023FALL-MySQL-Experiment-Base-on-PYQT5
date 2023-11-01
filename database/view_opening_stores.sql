CREATE VIEW VIEW_OPENING_STORES_LIST (canteen_name , canteen_img , store_name) AS
    (SELECT 
        canteen.canteen_name, canteen.canteen_img, store.store_name
    FROM
        canteen, store
	WHERE 
		canteen.canteen_status=1 and store.store_status=1 and store.canteen_id=canteen.canteen_id)
        