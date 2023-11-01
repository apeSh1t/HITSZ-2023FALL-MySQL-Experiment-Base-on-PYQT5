CREATE DEFINER=`root`@`localhost` PROCEDURE `update_store_status`(in t time)
begin 
 DECLARE s_status int; 
 
 if t between store.store_open_time and store.store_close_time and canteen.status=1 then
	select s_status,1;
 else 
	select s_status,0;
 end if;
 
SELECT s_status AS result; 
end