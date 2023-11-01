CREATE DEFINER=`root`@`localhost` PROCEDURE `update_canteen_status`(in t time) 
begin 
 DECLARE c_status int; 
 
 if t between canteen.canteen_open_time and canteen.canteen_close_time then
	select c_status,1;
 else 
	select c_status,0;
 end if;
 
SELECT c_status AS result; 
end 