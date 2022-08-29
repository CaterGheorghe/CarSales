CREATE TABLE carsales.TblCars (
   `id` BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (`id`),
    body_type varchar(100),
    brand varchar(100),
    model varchar(100),
    fuel varchar(100),
	year int,
    kilometres int,
    price float
);
INSERT INTO TblCars VALUES (1,'suv','dacia','Duster','diesel', 2018, 20000,15000);
INSERT INTO TblCars VALUES (2,'sedan','BMW','F10','diesel', 2013, 200000,14500);

