/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2023-10-29 10:36:10                          */
/*==============================================================*/


/*==============================================================*/
/* Table: canteen                                               */
/*==============================================================*/
create table canteen
(
   canteen_id           int not null,
   canteen_manager_telephone int not null,
   canteen_name         varchar(3) not null,
   canteen_status       numeric(1,0),
   canteen_open_time    time,
   canteen_close_time   time,
   canteen_img          longblob,
   primary key (canteen_id)
);

/*==============================================================*/
/* Table: canteen_manager                                       */
/*==============================================================*/
create table canteen_manager
(
   canteen_manager_telephone int not null,
   id                   int not null,
   primary key (canteen_manager_telephone)
);

/*==============================================================*/
/* Table: dish                                                  */
/*==============================================================*/
create table dish
(
   dish_id              int not null,
   store_id             int not null,
   dish_name            varchar(10) not null,
   dish_description     varchar(20),
   dish_cost            int not null,
   dish_gradients       varchar(20),
   primary key (dish_id)
);

/*==============================================================*/
/* Table: normal_user                                           */
/*==============================================================*/
create table normal_user
(
   normal_user_telephone int not null,
   id                   int not null,
   primary key (normal_user_telephone)
);

/*==============================================================*/
/* Table: order_dish                                            */
/*==============================================================*/
create table order_dish
(
   order_dish_index     int,
   order_id             bigint,
   dish_id              int not null,
   dish_num             int not null
);

/*==============================================================*/
/* Table: orders                                                */
/*==============================================================*/
create table orders
(
   order_id             bigint not null,
   normal_user_telephone int not null,
   store_id             int not null,
   order_cost           decimal(10) not null,
   order_canteen_id     int not null,
   order_store_id       int not null,
   order_time           datetime not null,
   order_status         int not null,
   primary key (order_id)
);

/*==============================================================*/
/* Table: store                                                 */
/*==============================================================*/
create table store
(
   store_id             int not null,
   canteen_id           int not null,
   store_manager_telephone int not null,
   store_status         numeric(1,0),
   store_name           varchar(10),
   store_open_time      time,
   store_close_time     time,
   store_img            longblob,
   primary key (store_id)
);

/*==============================================================*/
/* Table: store_manager                                         */
/*==============================================================*/
create table store_manager
(
   store_manager_telephone int not null,
   id                   int not null,
   primary key (store_manager_telephone)
);

/*==============================================================*/
/* Table: user_info                                             */
/*==============================================================*/
create table user_info
(
   id                   int not null,
   passwords            varchar(20) not null,
   nickname             varchar(20) not null,
   profile_photo        longblob,
   location             varchar(20),
   user_level           int,
   primary key (id)
);

alter table canteen add constraint FK_canteen_manager_canteen foreign key (canteen_manager_telephone)
      references canteen_manager (canteen_manager_telephone) on delete restrict on update restrict;

alter table canteen_manager add constraint FK_user_info_canteen_manager foreign key (id)
      references user_info (id) on delete restrict on update restrict;

alter table dish add constraint FK_dish_store foreign key (dish_id)
      references store (store_id) on delete restrict on update restrict;

alter table normal_user add constraint FK_user_info_normal_user foreign key (id)
      references user_info (id) on delete restrict on update restrict;

alter table order_dish add constraint FK_order_dish_dish foreign key (dish_id)
      references dish (dish_id) on delete restrict on update restrict;

alter table order_dish add constraint FK_order_order_dish foreign key (order_id)
      references orders (order_id) on delete restrict on update restrict;

alter table orders add constraint FK_normal_user_order_list foreign key (normal_user_telephone)
      references normal_user (normal_user_telephone) on delete restrict on update restrict;

alter table orders add constraint FK_store_order_list foreign key (store_id)
      references store (store_id) on delete restrict on update restrict;

alter table store add constraint FK_canteen_store foreign key (canteen_id)
      references canteen (canteen_id) on delete restrict on update restrict;

alter table store add constraint FK_store_manager_store foreign key (store_manager_telephone)
      references store_manager (store_manager_telephone) on delete restrict on update restrict;

alter table store_manager add constraint FK_user_info_store_manager foreign key (id)
      references user_info (id) on delete restrict on update restrict;

