USE tienda;

-- Ejercicio 1: Calcula el numero de clientes por cada ciudad.
SELECT COUNT(customer_number) AS numero_clientes, city
FROM customers AS c 
GROUP BY city;

-- En esta subquery tengo todas las ciudades:
SELECT DISTINCT city 
FROM customers;

-- En la consulta principal, seleccionaremos la ciudad y contaremos los clientes en esa ciudad
-- usando la subconsulta para filtrar por las ciudades.
SELECT city, 
	(SELECT COUNT(customer_number)
	FROM customers AS c2
	WHERE c2.city = c1.city) AS numero_clientes
FROM (SELECT DISTINCT city FROM customers) AS c1;



-- Ejercicio 2: Usando la consulta anterior como subconsulta, selecciona la ciudad con el mayor numero de clientes.
SELECT city
FROM 
	(SELECT COUNT(customer_number) AS numero_clientes, city
	FROM customers AS c1 
	GROUP BY city) AS c2
ORDER BY numero_clientes DESC
LIMIT 1;



-- Ejercicio 3: Por último, usa todas las consultas anteriores para seleccionar
-- el customerNumber, nombre y apellido de las clientas asignadas a la ciudad con mayor numero de clientas.
SELECT customer_number, contact_first_name, contact_last_name, city
FROM customers AS c 
WHERE city = (
	SELECT city
	FROM 
		(SELECT COUNT(customer_number) AS numero_clientes, city
		FROM customers AS c1 
		GROUP BY city) AS c2
	ORDER BY numero_clientes DESC
	LIMIT 1);
	

	
-- Ejercicio 4: Queremos ver ahora que empleados tienen algún contrato asignado con alguno de los clientes existentes. 
-- Para ello selecciona employeeNumber como 'Número empleado', firstName como 'nombre Empleado' 
-- y lastName como 'Apellido Empleado'
SELECT DISTINCT employee_number AS NumeroEmpleado, first_name AS NombreEmpleado, last_name AS ApellidoEmpleado
FROM employees AS e 
INNER JOIN customers AS c ON e.employee_number = c.sales_rep_employee_number;
	
	

-- Ejercicio 5: Queremos ver ahora en cuantas ciudades en las cuales tenemos clientes, 
-- no también una oficina de nuestra empresa para ello: Selecciona aquellas ciudades como 'ciudad' 
-- y los nombres de las empresas como 'nombre de la empresa ' de la tabla customers, sin repeticiones, 
-- que no tengan una oficina en dicha ciudad de la tabla offices.

-- primero vemos que hay en la tabla offices
SELECT * 
FROM offices AS o 
LIMIT 10;

-- Luego selecionamos todas las distintas ciudades donde hay oficina
SELECT DISTINCT city
FROM offices AS o;

-- Ahora hacemos la query principal usando la subquery anterior para excluir las ciudades que tienen oficina
SELECT DISTINCT city AS ciudad, customer_name AS nombre_de_la_empresa
FROM customers AS c
WHERE city NOT IN (
	SELECT DISTINCT city
	FROM offices AS o);