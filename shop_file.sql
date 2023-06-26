
--Customers
INSERT INTO customer
    (f_name, l_name, email)
VALUES
    ("Jotautas", "Treigys", "jtr@gmail.com");

INSERT INTO customer
    (f_name, l_name, email)
VALUES
    ("Laura", "Sauliene", "lsauliene@gmail.com");

INSERT INTO customer
    (f_name, l_name, email)
VALUES
    ("Laurynas", "Suodaitis", "lsuo@gmail.com");

INSERT INTO customer
    (f_name, l_name, email)
VALUES
    ("Agne", "Liete", "lietea@gmail.com");

--Status
INSERT INTO status
    (name)
VALUES
    ("Atmestas");

INSERT INTO status
    (name)
VALUES
    ("Patvirtintas");

INSERT INTO status
    (name)
VALUES
    ("Neapmoketas");

INSERT INTO status
    (name)
VALUES
    ("Atsauktas");


--Order
INSERT INTO order_
    (date_, status_id)
VALUES
    ("2020-11-14", 1);

INSERT INTO order_
    (date_, status_id)
VALUES
    ("2023-01-08", 4);

INSERT INTO order_
    (date_, status_id)
VALUES
    ("2021-03-14", 2);

INSERT INTO order_
    (date_, status_id)
VALUES
    ("2018-12-20", 3);

--Product
INSERT INTO product
    (name, price)
VALUES
    ("Tulpes", "18");

INSERT INTO product
    (name, price)
VALUES
    ("Bijunai", "25");

INSERT INTO product
    (name, price)
VALUES
    ("Protejos", "40");

INSERT INTO product
    (name, price)
VALUES
    ("Leukonijos", "11");

--Product order
INSERT INTO product_order
    (quantity)
VALUES
    ("100");

INSERT INTO product_order
    (quantity)
VALUES
    ("150");

INSERT INTO product_order
    (quantity)
VALUES
    ("50");

INSERT INTO product_order
    (quantity)
VALUES
    ("25");


--Uzklausos

SELECT customer.id, customer.l_name, customer.f_name, customer.email
FROM customer
JOIN order_
ON customer.id=order_.customer_id