/* En este ejercicio vamos a usar una tabla ya creada llamada customers (clientes/as), que está en la base de datos tienda.*/

USE tienda;

/*EJERCICIO 1
Selecciona el ID, nombre, apellidos de las empleadas y el ID de cada cliente asociado a ellas, usando CROSS JOIN.*/
SELECT employees.employee_number, employees.first_name, employees.last_name, customers.customer_number 
FROM employees
CROSS JOIN customers;
-- WHERE employees.employee_number = customers.sales_rep_employee_number >> Porque esto no está en la solución?


/*EJERCICIO 2
Selecciona el ID, nombre, apellidos de las empleadas, para aquellas con más de 8 clientes, usando CROSS JOIN.*/
SELECT e.employee_number, e.first_name, e.last_name
FROM employees AS e
CROSS JOIN customers AS c
WHERE e.employee_number = c.sales_rep_employee_number -- Porque aquí hay este WHERE y no lo hay en el ejercicio anterior? 
GROUP BY e.employee_number
HAVING COUNT(c.customer_number) > 8; -- En la solución hay el DISTINCT: HAVING COUNT(DISTINCT customers.customer_number) > 8;
-- Duda: El resultado es igual, es mas o menos correcto usar el DISTINCT en este caso? 


/*EJERCICIO 3
Selecciona el nombre y apellidos de las empleadas que tienen clientes de más de un país, usando CROSS JOIN.*/
SELECT e.first_name, e.last_name -- , COUNT(DISTINCT customers.country) AS PaisesClientes
FROM employees AS e
CROSS JOIN customers AS c
WHERE e.employee_number = c.sales_rep_employee_number
GROUP BY c.sales_rep_employee_number -- employees.employee_number, employees.first_name, employees.last_name
HAVING COUNT(DISTINCT c.country) > 1;
-- Me faltó poner el DISTINCT en el COUNT, esto cambia el resultado. Por lo demás, el resultado es igual. Mi consulta está mas o menos correcta que la solución?


/*EJERCICIO 4
Selecciona el ID, nombre, apellidos de las empleadas y el ID de cada cliente asociado a ellas, usando INNER JOIN.*/
SELECT e.employee_number, e.first_name, e.last_name, c.customer_number 
FROM employees AS e
INNER JOIN customers AS c
ON e.employee_number = c.sales_rep_employee_number; -- La solución usa WHERE en lugar de ON. Porque? Hay diferencia? El resultado es el mismo.


/*EJERCICIO 5
Selecciona el ID, nombre, apellidos de las empleadas, para aquellas con más de 8 clientes, usando INNER JOIN.*/
SELECT e.employee_number, e.first_name, e.last_name
FROM employees AS e
INNER JOIN customers AS c
ON e.employee_number = c.sales_rep_employee_number
GROUP BY c.sales_rep_employee_number -- Agrupar por c.sales_rep o por e.employee_number es lo mismo ya que las 2 columnas son iguales, esto es correcto?
HAVING COUNT(c.customer_number) > 8; -- Aquí el Distinct sirve para no contar el mismo cliente mas de una vez, esto es correcto?
-- La solución termina así:
-- GROUP BY employees.employee_number
-- HAVING COUNT(DISTINCT customers.customer_number) > 8;
-- El resultado es el mismo, mi consulta está mas o menos correcta que la solución? Porque? 


/*EJERCICIO 6
Selecciona el nombre y apellidos de las empleadas que tienen clientes de más de un país, usando INNER JOIN.*/
SELECT e.first_name, e.last_name -- , COUNT(DISTINCT customers.country) AS PaisesClientes 
FROM employees AS e
INNER JOIN customers AS c
ON e.employee_number = c.sales_rep_employee_number
GROUP BY c.sales_rep_employee_number 
HAVING COUNT(DISTINCT c.country) > 1; -- Aquí se usa el DISTINCT para no contar el mismo Pais mas de una vez, esto es correcto?


/*EJERCICIO 7
Selecciona el ID, nombre, apellidos de todas las empleadas y el ID de cada cliente asociado a ellas (si es que lo tienen).*/
SELECT e.employee_number, e.first_name, e.last_name, c.customer_number 
FROM employees AS e
LEFT JOIN customers AS c
ON e.employee_number = c.sales_rep_employee_number;


/*EJERCICIO 8
Selecciona el ID de todos los clientes, y el nombre, apellidos de las empleadas que llevan sus pedidos (si es que las hay).*/
SELECT c.customer_number, e.first_name, e.last_name
FROM employees AS e
RIGHT JOIN customers AS c
ON e.employee_number = c.sales_rep_employee_number;


/*EJERCICIO 9
Selecciona el ID, nombre, apellidos de las empleadas, para aquellas con más de 8 clientes, usando LEFT JOIN.*/
SELECT e.employee_number, e.first_name, e.last_name, COUNT(c.customer_number) AS cant_clientes -- Aquí lo puse sin el COUNT() y me saltó error por eso.
FROM employees AS e
LEFT JOIN customers AS c
ON e.employee_number = c.sales_rep_employee_number
GROUP BY e.employee_number -- Agrupar por c.sales_rep o por e.employee_number es lo mismo ya que las 2 columnas son iguales, esto es correcto?
HAVING COUNT(c.customer_number)> 8; -- Aquí no hace falta el Distinct porque el customer_number en la tabla customers ya es un dato unico que no se repite, esto es correcto?


/*EJERCICIO 10
Selecciona el ID, nombre, apellidos de las empleadas, para aquellas con más de 8 clientes, usando RIGHT JOIN.*/
SELECT e.employee_number, e.first_name, e.last_name -- , COUNT(customers.customer_number) AS cant_clientes >> Esto aquí es opcional, porque antes no era? 
FROM employees AS e -- FROM customers
RIGHT JOIN customers AS c -- RIGHT JOIN employees
ON e.employee_number = c.sales_rep_employee_number
GROUP BY e.employee_number -- Agrupar por c.sales_rep o por e.employee_number es lo mismo ya que las 2 columnas son iguales, esto es correcto?
HAVING COUNT(c.customer_number) > 8; -- Aquí no hace falta el Distinct porque el customer_number en la tabla customers ya es un dato unico que no se repite, esto es correcto?
-- Duda con el FROM y el RIGHT JOIN, el resultado de la consulta es casi igual en las 2 opciones. Entender el porque de cada opción.


/*EJERCICIO 11
Selecciona el nombre y apellidos de las empleadas que tienen clientes de más de un país, usando LEFT JOIN.*/
SELECT e.first_name, e.last_name, COUNT(DISTINCT c.country) AS PaisesClientes
FROM employees AS e
LEFT JOIN customers AS c
ON e.employee_number = c.sales_rep_employee_number
GROUP BY e.employee_number -- Agrupar por c.sales_rep o por e.employee_number es lo mismo ya que las 2 columnas son iguales, esto es correcto?
HAVING COUNT(DISTINCT c.country)> 1;

