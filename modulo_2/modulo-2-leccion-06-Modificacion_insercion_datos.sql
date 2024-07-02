/*
CREATE SCHEMA modificacion_insercion;
USE modificacion_insercion;

CREATE TABLE t1 (a INTEGER, b CHAR(10));

Renombra la tabla t1 a t2.
ALTER TABLE t1 RENAME TO t2

Cambia la columna a de tipo INTEGER a tipo TINYINT NOT NULL (manteniendo el mismo nombre para la columna).
ALTER TABLE t2
MODIFY COLUMN a TINYINT NOT NULL

Cambia la columna b de tipo CHAR de 10 caracteres a CHAR de 20 caracteres. Además, renombra la columna como c.
ALTER TABLE t2
MODIFY COLUMN b CHAR(20)

ALTER TABLE t2
RENAME COLUMN b TO c

Añade una nueva columna llamada d de tipo TIMESTAMP.
ALTER TABLE t2
ADD COLUMN d TIMESTAMP

Elimina la columna c que definiste en el ejercicio 3.
ALTER TABLE t2
DROP COLUMN c

Crea una tabla llamada t3 idéntica a la tabla t2 (de manera automática, no definiéndola columna a columna).
CREATE TABLE t3 LIKE t2

Elimina la tabla original t2 y en otra sentencia renombra la tabla t3 como t1.
DROP TABLE t2;
ALTER TABLE t3 RENAME TO t1

Para los siguientes ejercicios vamos a usar las tablas ya creadas llamadas customers (clientes/as) y employees, que están en la base de datos tienda.

Crea una copia de la tabla Customers, ya que vamos a modificar los datos originales de dicha tabla. Para ello ejecuta la siguiente sentencia:
CREATE TABLE IF NOT EXISTS customers_mod 
SELECT * 
FROM customers;

Vamos a desactivar el modo seguro para poder realizar los ejercicios posteriores. 
Para ello: Pestaña Editar -> Preferencias -> Editor SQL -> Deseleccionar la opción de Actualizaciones segura (rechaza UPDATEs y DELETEs sin restricciones) -> Desconéctate del servidor y vuelve a conectarte o alternativamente cierra MySQL y vuelve a abrirlo.

Realiza una inserción de datos sobre la tabla customers introduciendo la siguiente información.

customernumber: 343
customername: Adalab
contactlastname: Rodriguez
contactfirstname: Julia
phone: 672986373
addressline1: Calle Falsa 123
addressline2: Puerta 42
city: Madrid
state: España
postalcode:28000
country: España
salesrepemployeeNumber: 15
creditlimit: 20000000

INSERT INTO customers (customer_number, customer_name, contact_last_name, contact_first_name, phone, address_line1, address_line2, city, state, postal_code, country, sales_rep_employee_number, credit_limit) 
VALUES (343, 'Adalab', 'Rodriguez', 'Julia', '672986373', 'Calle Falsa 123', 'Puerta 42', 'Madrid', 'España', '28000', 'España', 15, 20000000);

Esto salta error: "Error Code: 1452. Cannot add or update a child row: a foreign key constraint fails". Este error ocurre cuando intentas insertar o actualizar una fila en una tabla que tiene una clave foránea (foreign key) que no cumple con las restricciones de la tabla referenciada.
En este caso, el error ocurre porque la clave foránea sales_rep_employee_number en la tabla customers está referenciada a la columna employee_number en la tabla employees. Esto significa que el valor que intentas insertar para sales_rep_employee_number debe existir en la columna employee_number de la tabla employees.

Realiza una inserción de datos sobre la tabla customers introduciendo la siguiente información. Fíjate que ahora no tenemos toda la información.

customernumber: 344
customername: La pegatina After
contactlastname: Santiago
contactfirsnName: Maricarmen
phone: 00000000
addressline1: Travesía del rave
addressline2: NULL
city: Palma de Mallorca
state: NULL
postalcode:07005
country: España
salesrepemployeenumber: 10
creditlimit: 45673453

INSERT INTO customers (customer_number, customer_name, contact_last_name, contact_first_name, phone, address_line1, address_line2, city, state, postal_code, country, sales_rep_employee_number, credit_limit) 
VALUES (344, 'La pegatina After', 'Santiago', 'Maricarmen', '00000000', 'Travesía del rave', 'NULL', 'Palma de Mallorca', 'NULL', '07005', 'España', 10, 45673453);

Error Code: 1062. Duplicate entry '344' for key 'customers.PRIMARY'

Introduce ahora 5 filas nuevas con la información que consideres relevante para los campos disponibles en una misma instrucción. Se recuerda que el Indice(=la clave primaria), no es necesaria especificarla. En 3 de las nuevas filas debes dejar vacio el campo 'contactFirstName'

INSERT INTO customers (customer_name, contact_last_name, contact_first_name, phone, address_line1, address_line2, city, state, postal_code, country, sales_rep_employee_number, credit_limit) 
VALUES 
('TechCorp', 'Smith', 'John', '123456789', '123 Tech St', 'Suite 100', 'New York', 'NY', '10001', 'USA', 1002, 500000),
('Innovatech', 'Doe', '', '987654321', '456 Innovation Rd', 'Floor 2', 'San Francisco', 'CA', '94105', 'USA', 1056, 250000),
('FutureWorks', 'Brown', '', '456123789', '789 Future Blvd', 'Apt 45', 'Austin', 'TX', '73301', 'USA', 1076, 300000),
('NextGen', 'Johnson', 'Emily', '321654987', '321 NextGen Ave', 'Building B', 'Seattle', 'WA', '98101', 'USA', 1088, 450000),
('AlphaTech', 'Williams', '', '789456123', '654 AlphaTech Ln', 'Unit 7', 'Boston', 'MA', '02118', 'USA', 1323, 350000);

Error Code: 1364. Field 'customer_number' doesn't have a default value


Actualiza ahora los datos faltantes correspondientes al CustomerName 'La pegatina After' con la siguiente información.

addressline1: Polígono Industrial de Son Castelló
addressline2: Nave 92
city: Palma de Mallorca
state: España
postalcode:28123
country: España
salesrepemployeenumber: 25
creditlimit: 5000000

UPDATE customers
SET 
    address_line1 = 'Polígono Industrial de Son Castelló',
    address_line2 = 'Nave 92',
    city = 'Palma de Mallorca',
    state = 'España',
    postal_code = '28123',
    country = 'España',
    sales_rep_employee_number = 1002,
    credit_limit = 5000000
WHERE customer_name = 'La pegatina After';


0 row(s) affected Rows matched: 0  Changed: 0  Warnings: 0


Vamos ahora a romper a propósito la tabla con la que estamos trabajando, para ello primero vamos a realizar una copia de la misma antes de ejecutar lo siguiente. Con el nombre customers_destroy.
Para ello hacemos uso de la herramienta de exportación de datos de MySQL, como se explicaba en las guías del módulo 0 para la exportación y la importación de datos.
Una vez creada la copia y guardada a buen recaudo, vamos a actualizar algunos de los cambios sin especificar la condición del WHERE. Para ello modifica el campo los siguientes campos de
addressline1: Vamos
addressline2: a
postalcode: fastidiar
country: la tabla :)
Tras esto restaura la tabla que has trasteado con la copia que te has creado previamente.

-- Paso 1: Crear una copia de la tabla
CREATE TABLE customers_destroy AS SELECT * FROM customers;

-- Paso 2: Actualizar la tabla sin condición WHERE
UPDATE customers
SET 
    address_line1 = 'Vamos',
    address_line2 = 'a',
    postal_code = 'fastidiar',
    country = 'la tabla :)';

-- Paso 3: Eliminar la tabla original y renombrar la copia
DROP TABLE customers;
ALTER TABLE customers_destroy RENAME TO customers;

Actualiza ahora los datos de la tabla customers_mod, para que las 10 primeras empresas sean gestionadas por la representante de ventas numero 2. El resto de empresas no deben ser modificadas.

UPDATE customers_mod
SET sales_rep_employee_number = 2
WHERE customer_number IN (
    SELECT customer_number
    FROM (
        SELECT customer_number
        FROM customers_mod
        ORDER BY customer_number
        LIMIT 10
    ) AS temp_table
);

Otra opción:
UPDATE customers_mod
	SET sales_rep_employee_number = 2
    LIMIT 5


Queremos ahora eliminar de los datos de la tabla aquellos registros que contengan un 'null' en el campo 'ContactFirstName'.

DELETE FROM customers_mod
WHERE contact_first_name IS NULL;

DELETE FROM customers_mod;

Se ha vaciado la tabla completa.

*/

-- Duda: debo de volver a activar la opción de seguridad que desactivamos? 




























