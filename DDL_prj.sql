---------------
--implemntation of project ddl

--Club Members Table
CREATE TABLE members (
    member_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    age INT NOT NULL,
    sex VARCHAR(10) NOT NULL,
    height DECIMAL(4, 2) NOT NULL,
    weight DECIMAL(5, 2) NOT NULL,
    bmi DECIMAL(4, 2),
    workout_duration DECIMAL(5,2),
    body_fat DECIMAL(4, 2),
    calories_burned INT,
    calories_consumed INT,
    steps INT,
    distance DECIMAL(5, 2),
    subscription_status VARCHAR(20) NOT NULL,
    membership_type VARCHAR(50) NOT NULL,
    payment_method VARCHAR(50)

);

-- Exercises Table
--exercise routines
CREATE TABLE exercises (
    exercise_id SERIAL PRIMARY KEY,
    exercise_name VARCHAR(100) NOT NULL
   
);

-- Employees Table
--trainer and admin are employees
CREATE TABLE employees (
    emp_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(15) NOT NULL
);

-- Trainer Table
CREATE TABLE trainers (
    trainer_id SERIAL PRIMARY KEY,
    emp_id INT REFERENCES employees(emp_id) NOT NULL,
    certification_status VARCHAR(50),
    specialization VARCHAR(100)
);

-- Admin Table
--manages rooms
--manages equipment
--admin 'updates' classe scheduling
CREATE TABLE admins (
    admin_id SERIAL PRIMARY KEY,
    emp_id INT REFERENCES employees(emp_id) NOT NULL,
    role VARCHAR(50) NOT NULL
);

-- Rooms Table (for Room Booking Management)
CREATE TABLE rooms (
    room_id SERIAL PRIMARY KEY,
    room_name VARCHAR(100) NOT NULL,
    capacity INT NOT NULL

);

-- Bookings Table
CREATE TABLE bookings (
    booking_id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(member_id) NOT NULL,  
    room_id INT REFERENCES rooms(room_id) NOT NULL,  
    booking_date DATE NOT NULL,  
    start_time TIME NOT NULL, 
    end_time TIME NOT NULL, 
    purpose VARCHAR(100),  
    status VARCHAR(20) NOT NULL  

);

-- Equipment Table (for Equipment Maintenance Monitoring)
CREATE TABLE equipment (
    equipment_id SERIAL PRIMARY KEY,
    equipment_name VARCHAR(100) NOT NULL,
   is_good BOOLEAN DEFAULT true NOT NULL -- Indicates whether the equipment is in good condition
);

-- Classes Table
CREATE TABLE classes (
    class_id SERIAL PRIMARY KEY,
    class_name VARCHAR(100) NOT NULL,
    trainers_id INT REFERENCES trainers(trainer_id) NOT NULL,
    capacity INT NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    class_date DATE NOT NULL
   
);

--[trainer 'assigns' exerceise routines to members, exercise routines are attributes of 'assigns' table, 
 --and the assigns table has pK of both member & trainer]

 -- Assigns Table
CREATE TABLE assigns (
    assign_id SERIAL PRIMARY KEY,
    trainer_id INT REFERENCES trainers(trainer_id) NOT NULL,
    member_id INT REFERENCES members(member_id) NOT NULL,
    assignment_date DATE NOT NULL
  
);

-- Takes Table
CREATE TABLE takes (
    take_id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(member_id) NOT NULL,
    class_id INT REFERENCES classes(class_id) NOT NULL,
    is_personal_training BOOLEAN DEFAULT false -- Indicates if it's a personal training session
  
);


-- Billing Table (for Billing and Payment Processing)
CREATE TABLE billing (
    bill_id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(member_id) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_status VARCHAR(20) NOT NULL

);


CREATE TABLE admin_manages (
    admin_id INT REFERENCES admins(admin_id) NOT NULL,
    room_id INT REFERENCES rooms(room_id),
    equipment_id INT REFERENCES equipment(equipment_id),
    booking_id INT REFERENCES bookings(booking_id),
    PRIMARY KEY (admin_id, room_id, equipment_id, booking_id)
    
);



