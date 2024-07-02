-- SELECT * FROM tienda.customers;
-- CREATE SCHEMA ejercicios_2;
/*USE ejercicios_2;

-- Ejercicio 1
CREATE TABLE Empleadas (
	id_empleada INT, 
	salario FLOAT, -- DECIMAL(10, 2) >> Usar DECIMAL(10, 2) en lugar de FLOAT para garantizar la precisión en valores monetarios. 10, 2 significa que el número puede tener hasta 10 dígitos en total, con 2 de ellos después del punto decimal.
	nombre VARCHAR(100), 
	apellido VARCHAR(100), 
	pais VARCHAR(100)
);

-- Ejercicio 2
CREATE TABLE Personas2 (
    id INT NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    nombre VARCHAR(255),
    edad INT CHECK (edad > 16),
    ciudad varchar(255) DEFAULT 'Madrid'
);

-- Ejercicio 3
ALTER TABLE Empleadas
ADD PRIMARY KEY (id_empleada);

CREATE TABLE empleadas_en_proyectos (
    id_empleada INT,
    id_proyecto INT,
    PRIMARY KEY (id_empleada, id_proyecto),  -- Clave primaria compuesta
    FOREIGN KEY (id_empleada) REFERENCES Empleadas(id_empleada) ON DELETE CASCADE  -- Clave foránea con eliminación en cascada
);

CREATE SCHEMA creacion_tienda;
USE creacion_tienda;

-- Ejercicio 4
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(255),
    country VARCHAR(100)
);

-- Ejercicio 5
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    last_name VARCHAR(255),
    first_name VARCHAR(255),
    title VARCHAR(100),
    birth_date DATE,
    hire_date DATE,
    country VARCHAR(100)
);


-- Ejercicio 6
CREATE TABLE new_employees (
    employee_id INT PRIMARY KEY,
    last_name VARCHAR(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    title VARCHAR(100),
    birth_date DATE,
    hire_date DATE,
    country VARCHAR(100)
);

CREATE TABLE new_customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(255) NOT NULL,
    country VARCHAR(100),
    credit_limit DECIMAL(10, 2) CHECK (credit_limit >= 0),
    employee_id INT,
    FOREIGN KEY (employee_id) REFERENCES new_employees(employee_id) ON DELETE SET NULL
);

-- BONUS
CREATE TABLE Clientes (
    id_cliente INT PRIMARY KEY,
    nombre_cliente VARCHAR(255) NOT NULL
);

CREATE TABLE Articulos (
    id_articulo INT PRIMARY KEY,
    articulo_marca VARCHAR(255) NOT NULL,
    precio_unitario DECIMAL(10, 2) NOT NULL
);

CREATE TABLE Pedidos (
    id_pedido INT PRIMARY KEY,
    id_cliente INT,
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente)
);


CREATE TABLE Detalles_de_Pedido (
    id_pedido INT,
    id_articulo INT,
    cantidad INT NOT NULL,
    PRIMARY KEY (id_pedido, id_articulo),
    FOREIGN KEY (id_pedido) REFERENCES Pedidos(id_pedido),
    FOREIGN KEY (id_articulo) REFERENCES Articulos(id_articulo)
);




*/












