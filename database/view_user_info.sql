CREATE VIEW VIEW_USER_INFO_LIST (ID , nickname , profile_photo) AS
    (SELECT 
        user_info.id, user_info.nickname, user_info.profile_photo
    FROM
        user_info)