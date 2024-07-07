USE tienda;


-- Ejercicio 1: Obtener el número identificativo de cliente más bajo de la base de datos.
SELECT MIN(customer_number) AS IDMenor   
	FROM customers;

-- Ejercicio 2: Seleccionar el límite de crédito medio para los clientes de España.
SELECT AVG(credit_limit) AS limite_credito_medio_espana
	FROM customers
	WHERE country = 'Spain';
	
-- Ejercicio 3: Seleccionar el número de clientes en Francia.
SELECT COUNT(customer_number) AS numero_clientes_francia
	FROM customers
	WHERE country = 'France';
	
-- Ejercicio 4: Seleccionar el máximo de crédito que tiene cualquiera de los clientes del empleado con número 1323.
SELECT MAX(credit_limit) AS max_cred
	FROM customers
	WHERE sales_rep_employee_number = 1323;
	
-- Ejercicio 5: ¿Cuál es el número máximo de empleado de la tabla customers?
SELECT MAX(sales_rep_employee_number) AS max_empleado
	FROM customers;

-- Ejercicio 6: Realiza una consulta SELECT que seleccione el número de cada empleado de ventas, así como el numero de clientes distintos que tiene cada uno.
SELECT DISTINCT sales_rep_employee_number, COUNT(customer_number) AS numero_clientes
	FROM customers
	GROUP BY sales_rep_employee_number;
 -- ORDER BY sales_rep_employee_number;
	
-- Respuesta correcta:
-- SELECT sales_rep_employee_number, COUNT(DISTINCT customer_number) AS numero_clientes
-- 	FROM customers
-- 	GROUP BY sales_rep_employee_number;

-- En el ejercicio 6 me salió el mismo resultado de la solución, pero fuera de orden, para que saliera igual tendría que añadir el order by. Está correcta mi solución? 

	
-- Ejercicio 7: Selecciona el número de cada empleado de ventas que tenga más de 7 clientes distintos.
SELECT sales_rep_employee_number, COUNT(DISTINCT customer_number) AS numero_clientes
	FROM customers
	GROUP BY sales_rep_employee_number
	HAVING numero_clientes > 7;


-- Ejercicio 8: Selecciona el número de cada empleado de ventas, así como el numero de clientes distintos que tiene cada uno. 
-- Asigna una etiqueta de "AltoRendimiento" a aquellos empleados con mas de 7 clientes distintos.
SELECT sales_rep_employee_number, COUNT(DISTINCT customer_number) AS numero_clientes,
	CASE
	WHEN COUNT(DISTINCT customer_number) > 7 THEN 'AltoRendimiento'
	ELSE NULL
	END AS Rendimiento
FROM customers
GROUP BY sales_rep_employee_number;


-- Ejercicio 9:Selecciona el número de clientes en cada pais.
SELECT COUNT(customer_number) AS numero_clientes, country
FROM customers
GROUP BY country;
-- En la solución está como COUNT(*), el mío también está correcto? El resultado es el mismo, solo cambia el orden.


-- Ejercicio 10:Selecciona aquellos países que tienen clientes de más de 3 ciudades diferentes.
SELECT country
FROM customers
GROUP BY country 
HAVING COUNT(DISTINCT city) > 3;