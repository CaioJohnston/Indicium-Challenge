USE indicium;

CREATE TABLE IF NOT EXISTS categories (

	category_id SMALLINT NOT NULL,
	category_name VARCHAR(15) NOT NULL,
    description TEXT,
    picture LONGBLOB

);

CREATE TABLE IF NOT EXISTS customer_customer_demo (
    customer_id CHAR(5) NOT NULL,
    customer_type_id CHAR(5) NOT NULL
);

CREATE TABLE IF NOT EXISTS customer_demographics (
    customer_type_id CHAR(5) NOT NULL,
    customer_desc TEXT
);

CREATE TABLE IF NOT EXISTS customers (
    customer_id CHAR(5) NOT NULL,
    company_name VARCHAR(40) NOT NULL,
    contact_name VARCHAR(30),
    contact_title VARCHAR(30),
    address VARCHAR(60),
    city VARCHAR(15),
    region VARCHAR(15),
    postal_code VARCHAR(10),
    country VARCHAR(15),
    phone VARCHAR(24),
    fax VARCHAR(24)
);


CREATE TABLE IF NOT EXISTS employees (
    employee_id SMALLINT NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    first_name VARCHAR(10) NOT NULL,
    title VARCHAR(30),
    title_of_courtesy VARCHAR(25),
    birth_date DATE,
    hire_date DATE,
    address VARCHAR(60),
    city VARCHAR(15),
    region VARCHAR(15),
    postal_code VARCHAR(10),
    country VARCHAR(15),
    home_phone VARCHAR(24),
    extension VARCHAR(4),
    photo LONGBLOB,
    notes TEXT,
    reports_to SMALLINT,
    photo_path VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS employee_territories (
    employee_id TEXT,
    territory_id TEXT
);


CREATE TABLE IF NOT EXISTS orders (
    order_id SMALLINT NOT NULL,
    customer_id CHAR(5),
    employee_id SMALLINT,
    order_date DATE,
    required_date DATE,
    shipped_date DATE,
    ship_via SMALLINT,
    freight FLOAT,
    ship_name VARCHAR(40),
    ship_address VARCHAR(60),
    ship_city VARCHAR(15),
    ship_region VARCHAR(15),
    ship_postal_code VARCHAR(10),
    ship_country VARCHAR(15)
);


CREATE TABLE IF NOT EXISTS products (
    product_id smallint NOT NULL,
    product_name character varying(40) NOT NULL,
    supplier_id smallint,
    category_id smallint,
    quantity_per_unit character varying(20),
    unit_price real,
    units_in_stock smallint,
    units_on_order smallint,
    reorder_level smallint,
    discontinued integer NOT NULL
);

CREATE TABLE IF NOT EXISTS region (
    region_id SMALLINT NOT NULL,
    region_description character varying(10) NOT NULL
);


CREATE TABLE IF NOT EXISTS shippers (
    shipper_id SMALLINT NOT NULL,
    company_name VARCHAR(40) NOT NULL,
    phone VARCHAR(24)
);

CREATE TABLE IF NOT EXISTS suppliers (
    supplier_id SMALLINT NOT NULL,
    company_name VARCHAR(40) NOT NULL,
    contact_name VARCHAR(30),
    contact_title VARCHAR(30),
    address VARCHAR(60),
    city VARCHAR(15),
    region VARCHAR(15),
    postal_code VARCHAR(10),
    country VARCHAR(15),
    phone VARCHAR(24),
    fax VARCHAR(24),
    homepage TEXT
);

CREATE TABLE IF NOT EXISTS territories (
    territory_id VARCHAR(20) NOT NULL,
    territory_description TEXT NOT NULL,
    region_id SMALLINT NOT NULL
);


CREATE TABLE IF NOT EXISTS us_states (
    state_id SMALLINT NOT NULL,
    state_name VARCHAR(100),
    state_abbr CHAR(2),
    state_region VARCHAR(50)
);

CREATE TABLE order_details (
    order_id INT,
    product_id INT,
    unit_price DECIMAL(10, 2),
    quantity INT,
    discount DECIMAL(4, 2)
);
