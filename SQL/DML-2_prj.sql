-- Inserting values into the employees table
-- Inserting values into the employees table
INSERT INTO employees (first_name, last_name, email, phone)
VALUES
    ('John', 'Doe', 'john.doe@example.com', '+1234567890'),
    ('Jane', 'Smith', 'jane.smith@example.com', '+9876543210'),
    ('Michael', 'Johnson', 'michael.johnson@example.com', '+1122334455'),
    ('Emily', 'Brown', 'emily.brown@example.com', '+9988776655');


INSERT INTO trainers (emp_id, certification_status, specialization)
SELECT 
    emp_id, 	
    'Certified', 
    CASE 
        WHEN emp_id = 1 THEN 'Strength Training'
        WHEN emp_id = 2 THEN 'Yoga'
        WHEN emp_id = 3 THEN 'Cardio'
        WHEN emp_id = 4 THEN 'CrossFit'
        ELSE 'Unknown' 
    END
FROM employees
WHERE emp_id IN (1, 2, 3, 4);

INSERT INTO admins (emp_id, role)
SELECT 
    emp_id, 
    CASE 
        WHEN first_name = 'John' THEN 'Room Booking Manager'
        WHEN first_name = 'Jane' THEN 'Equipment Manager'
        WHEN first_name = 'Michael' THEN 'Class Scheduler'
        WHEN first_name = 'Emily' THEN 'Billing Manager'
        WHEN first_name = 'Admin' THEN 'System Administrator'  
        ELSE 'Unknown'  
    END
FROM employees
WHERE first_name IN ('John', 'Jane', 'Michael', 'Emily', 'Admin');

INSERT INTO rooms (room_name, capacity)
VALUES
    ('Room A', 20),
    ('Room B', 15),
    ('Room C', 30),
    ('Room D', 25);
	
INSERT INTO equipment (equipment_name, is_good)
VALUES
    ('Treadmill', true),
    ('Dumbbells', true),
    ('Elliptical Machine', false),
    ('Exercise Bike', true);
	
INSERT INTO exercises (exercise_name)
VALUES
    ('Push-ups'),
    ('Squats'),
    ('Running'),
    ('Plank');
	
INSERT INTO classes (class_name, trainers_id, capacity, start_time, end_time, class_date)
VALUES
    ('Yoga Class', (SELECT trainer_id FROM trainers WHERE specialization = 'Yoga' LIMIT 1), 20, '10:00:00', '11:00:00', '2024-04-15'),
    ('HIIT Workout', (SELECT trainer_id FROM trainers WHERE specialization = 'Cardio' LIMIT 1), 15, '12:00:00', '13:00:00', '2024-04-15'),
    ('Zumba Fitness', (SELECT trainer_id FROM trainers WHERE specialization = 'CrossFit' LIMIT 1), 25, '14:00:00', '15:00:00', '2024-04-15'),
    ('Pilates Class', (SELECT trainer_id FROM trainers WHERE specialization = 'Strength Training' LIMIT 1), 18, '16:00:00', '17:00:00', '2024-04-15');


INSERT INTO bookings (member_id, room_id, booking_date, start_time, end_time, purpose, status)
SELECT 
    m.member_id, 
    b.room_id, 
    b.booking_date::date,  
    b.start_time::time, 
    b.end_time::time, 
    b.purpose, 
    b.status
FROM 
    (
        VALUES
            (1, 1, '2024-04-15', '10:00:00', '11:00:00', 'Yoga session', 'Confirmed'),
            (2, 2, '2024-04-15', '12:00:00', '13:00:00', 'HIIT workout', 'Pending'),
            (3, 3, '2024-04-15', '14:00:00', '15:00:00', 'Zumba class', 'Confirmed'),
            (4, 4, '2024-04-15', '16:00:00', '17:00:00', 'Pilates session', 'Pending')
    ) AS b(member_id, room_id, booking_date, start_time, end_time, purpose, status)
INNER JOIN members m ON b.member_id = m.member_id;


INSERT INTO assigns (trainer_id, member_id, assignment_date)
SELECT 
    t.trainer_id, 
    m.member_id, 
    a.assignment_date::date
FROM 
    (
        VALUES
            (1, 1, '2024-04-10'),
            (2, 2, '2024-04-11'),
            (3, 3, '2024-04-12'),
            (4, 4, '2024-04-13')
    ) AS a(trainer_id, member_id, assignment_date)
INNER JOIN trainers t ON a.trainer_id = t.trainer_id
INNER JOIN members m ON a.member_id = m.member_id;

INSERT INTO takes (member_id, class_id, is_personal_training)
SELECT 
    m.member_id, 
    t.class_id, 
    t.is_personal_training
FROM 
    (
        VALUES
            (1, 1, false),
            (2, 2, true),	
            (3, 3, false),
            (4, 4, true)
    ) AS t(member_id, class_id, is_personal_training)
INNER JOIN members m ON t.member_id = m.member_id;


INSERT INTO admin_manages (admin_id, room_id, equipment_id, booking_id)
SELECT 
    a.admin_id,
    CASE 
        WHEN a.role = 'Room Booking Manager' THEN 1
        WHEN a.role = 'Equipment Manager' THEN 2
        WHEN a.role = 'Class Scheduler' THEN 3
        WHEN a.role = 'Billing Manager' THEN 4
        WHEN a.role = 'System Administrator' THEN 5
        ELSE NULL
    END AS room_id,
    CASE 
        WHEN a.role = 'Equipment Manager' THEN 1
        WHEN a.role = 'Room Booking Manager' THEN 2
        WHEN a.role = 'Class Scheduler' THEN 3
        WHEN a.role = 'Billing Manager' THEN 4
        WHEN a.role = 'System Administrator' THEN 5
        ELSE NULL
    END AS equipment_id,
    b.booking_id
FROM 
    admins a
JOIN 
    bookings b ON a.role IN ('Room Booking Manager', 'Equipment Manager', 'Class Scheduler', 'Billing Manager', 'System Administrator')
WHERE a.role IN ('Room Booking Manager', 'Equipment Manager', 'Class Scheduler', 'Billing Manager', 'System Administrator');
	
	
INSERT INTO billing (member_id, amount, payment_status)
SELECT 
    m.member_id, 
    data.amount, 
    data.payment_status
FROM 
    (
        VALUES
            (1, 50.00, 'Paid'),
            (2, 75.00, 'Pending'),
            (3, 100.00, 'Paid'),
            (4, 60.00, 'Pending')
    ) AS data(member_id, amount, payment_status)
INNER JOIN members m ON data.member_id = m.member_id;