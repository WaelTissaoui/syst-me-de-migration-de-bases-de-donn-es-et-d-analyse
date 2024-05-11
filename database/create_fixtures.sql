CREATE TABLE IF NOT EXISTS Category (
    id serial  primary key not null ,
    category_name varchar(255),
    category_description varchar(255),
    creation_date timestamp,
    update_date timestamp
);



CREATE TABLE IF NOT EXISTS Product (
    id serial primary key not null,
    category_id int not null,
    product_name varchar(255),
    price float ,
    stock_quantity int,
    creation_date timestamp,
    update_date timestamp,
    foreign key (category_id) references Category(id)
);


CREATE TABLE IF NOT EXISTS Customer (
    id serial primary key not null,
    customer_name varchar(255),
    adresse varchar(255),
    gender char(1),
    creation_date timestamp,
    update_date timestamp
);


CREATE TABLE IF NOT EXISTS Sales (
    id serial primary key not null,
    product_id int not null ,
    customer_id int not null,
    total_price float,
    sale_date date,
    creation_date timestamp,
    update_date timestamp,
    foreign key (product_id) references  Product(id),
    foreign key (customer_id) references Customer(id)
    
);