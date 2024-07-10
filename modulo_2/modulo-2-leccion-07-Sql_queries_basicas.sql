/* Realiza una consulta SELECT que obtenga los nombres, teléfonos y direcciones de todas las empresas cliente de la tabla customers.

Realiza una consulta que obtenga los teléfonos y direcciones de aquellas empresas de la tabla customers que se encuentren en USA (es su país).

Realiza una consulta que obtenga los nombres y apellidos de las personas de contacto en cada empresa que no tenga segunda linea de dirección.

Busca aquellos registros de la tabla customers que tengan un valor guardado para el campo state. Este atributo solo es valido para ciertos países por lo que habrá varias entradas con valor NULL.

Busca aquellos registros de la tabla customers que correspondan a clientes de USA pero que no tengan un valor guardado para el campo state.

Selecciona el país (country) correspondiente a los registros de clientes con un límite de crédito (credit_limit) mayor que $10000.

*/

-- Ejercicio 1
SELECT 
    customer_name, 
    phone, 
    address_line1, 
    address_line2
FROM 
    customers;

-- Ejercicio 2
SELECT 
    phone, 
    address_line1, 
    address_line2
FROM
    customers
WHERE
    country = 'USA';

-- Ejercicio 3
SELECT 
    contact_first_name,
    contact_last_name
FROM
    customers
WHERE 
    address_line2 IS NULL;

-- Ejercicio 4
SELECT * FROM customers
WHERE
    state IS NOT NULL;

-- Ejercicio 5
SELECT * FROM customers
WHERE country = 'USA' AND state IS NULL;

-- Ejercicio 6
SELECT DISTINCT country FROM customers
WHERE credit_limit > 10000;



-- ORDER TO WRITE COMMANDS (NOT THE SAME AS EXECUTION ORDER!!!)

-- SELECT column1, column2, ...
-- FROM table_name
-- WHERE condition
-- GROUP BY column
-- HAVING condition
-- ORDER BY column1 [ASC|DESC] ...
-- LIMIT number;