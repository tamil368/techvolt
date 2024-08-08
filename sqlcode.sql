--#databse creation--

create databse smart_car_system;

--#signup table creation--

CREATE TABLE users (
  id INT AUTO_INCREMENT, 
  name VARCHAR(100) NOT NULL, 
  email VARCHAR(255) UNIQUE NOT NULL,
  phone VARCHAR(15) NOT NULL,
  password VARCHAR(255) NOT NULL,
  user_type VARCHAR(10) NOT NULL,
  PRIMARY KEY (id)
);
