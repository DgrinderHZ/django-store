drop table product;
create table Product(
  id integer not null primary key,
  title char(50),
  img char(100),
  details varchar(500),
  brand char(50),
  price real,
  created_at date
  );
  
  -- drop table user; 
  create table User(
  id integer not null primary key,
  f_name char(50),
  l_name char(50),
  username char(50),
  email char(70),
  password char(70),
  id_cart integer not null
);

-- drop table Cart;
create table Cart(
  id integer not null primary key,
  id_user integer not null,
  foreign key(id_user) references user(id)
);

-- drop table order;
create table order_(
id integer not null primary key,
created_at date
);

create table product_cart(
id integer not null primary key auto_increment,
id_product integer not null,
id_cart integer not null, 
foreign key(id_product) references product(id),
foreign key(id_cart) references cart(id)
);

create table products_order(
id integer not null,
id_product integer not null,
id_order integer not null, 
foreign key(id_product) references product(id),
foreign key(id_order) references order_(id)
);

