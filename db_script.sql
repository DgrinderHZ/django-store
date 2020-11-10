
create table Product(
  id integer not null primary key,
  title char(50),
  img char(100),
  details varchar(500),
  brand char(50)
  );
  
  create table User(
  id integer not null primary key,
  f_name char(50),
  l_name char(50),
  username char(50),
  email char(70),
  password char(70)
);

-- drop table Cart;
create table Cart(
  id integer not null primary key,
  id_user integer not null,
  foreign key(id_user) references user(id)
);

-- drop table orders;
create table orders(
id integer not null primary key,
id_cart integer not null,
foreign key(id_cart) references cart(id),
id_product integer not null,
foreign key(id_product) references product(id)
)


