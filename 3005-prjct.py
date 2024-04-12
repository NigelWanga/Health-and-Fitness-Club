import psycopg


# Function to connect to the PostgreSQL database
def connect_to_database():
    try:
        conn = psycopg.connect(database="Health and Fitness Club", user="postgres", password="postgres", host="localhost", port="5432")
        print("Opened database successfully\n")
        return conn
    except psycopg.Error as e:
        print("Error connecting to database:", e)
        return None


# Function for user registration
def user_registration(conn):
    try:
        with conn:
            with conn.cursor() as cur:
                # Prompt the user to input member information
                print("Enter first name: ", end="")
                first_name = input()
                print("Enter last name: ", end="")
                last_name = input()
                print("Enter email: ", end="")
                email = input()
                print("Enter phone: ", end="")
                phone = input()
                print("Enter age: ", end="")
                age = int(input())
                print("Enter sex: ", end="")
                sex = input()
                print("Enter height: ", end="")
                height = float(input())
                print("Enter weight: ", end="")
                weight = float(input())
                print("Enter BMI: ", end="")
                bmi = float(input())
                print("Enter workout duration: ", end="")
                workout_duration = float(input())
                print("Enter body fat: ", end="")
                body_fat = float(input())
                print("Enter calories burned: ", end="")
                calories_burned = int(input())
                print("Enter calories consumed: ", end="")
                calories_consumed = int(input())
                print("Enter steps: ", end="")
                steps = int(input())
                print("Enter distance: ", end="") 
                distance = float(input())
                print("Enter subscription status: ", end="")
                subscription_status = input()
                print("Enter membership type: ", end="")
                membership_type = input()
                print("Enter payment method: ", end="")
                payment_method = input()

                # Insert member information into the database
                cur.execute("INSERT INTO members (first_name, last_name, email, phone, age, sex, height, weight, bmi, workout_duration, body_fat, calories_burned, calories_consumed, steps, distance, subscription_status, membership_type, payment_method) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (first_name, last_name, email, phone, age, sex, height, weight, bmi, workout_duration, body_fat, calories_burned, calories_consumed, steps, distance, subscription_status, membership_type, payment_method))

        print("User registration successful!")
    except Exception as e:
        print("Error during user registration:", e)


# Function to view members
def view_members(conn):
    try:
        with conn:
            with conn.cursor() as cur:
                # Fetch all records from the 'members' table
                cur.execute("SELECT * FROM members")

                # Fetch all the rows
                rows = cur.fetchall()

                for row in rows:
                    print(f"""
                    Member ID: {row[0]}
                    First Name: {row[1]}
                    Last Name: {row[2]}
                    Email: {row[3]}
                    Phone: {row[4]}
                    Age: {row[5]}
                    Sex: {row[6]}
                    Height: {row[7]}
                    Weight: {row[8]}
                    BMI: {row[9]}
                    Workout Duration: {row[10]}
                    Body Fat: {row[11]}
                    Calories Burned: {row[12]}
                    Calories Consumed: {row[13]}
                    Steps: {row[14]}
                    Distance: {row[15]}
                    Subscription Status: {row[16]}
                    Membership Type: {row[17]}
                    Payment Method: {row[18]}
                    """)

    except Exception as e:
        print("Error during fetching members:", e)


#function to update member profile
def update_member_profile(conn):
    try:
        with conn:
            with conn.cursor() as cur:
                # Ask the user for their member ID
                member_id = input("Enter your member ID: ")

                # Ask the user for the information they want to update
                print("What information do you want to update?")
                print("1. Personal information")
                print("2. Fitness goals")
                print("3. Health metrics")
                option = input("Select an option: ")

                if option == '1':
                    # Update personal information
                    new_email = input("Enter your new email: ")
                    new_phone = input("Enter your new phone number: ")
                    cur.execute("UPDATE members SET email = %s, phone = %s WHERE member_id = %s", (new_email, new_phone, member_id))
                elif option == '2':
                    # Update fitness goals
                    new_goal = input("Enter your new fitness goal: ")
                    cur.execute("UPDATE members SET fitness_goal = %s WHERE member_id = %s", (new_goal, member_id))
                elif option == '3':
                    # Update health metrics
                    new_height = input("Enter your new height: ")
                    new_weight = input("Enter your new weight: ")
                    cur.execute("UPDATE members SET height = %s, weight = %s WHERE member_id = %s", (new_height, new_weight, member_id))
                else:
                    print("Invalid option. Please try again.")

                # Commit the changes
                conn.commit()

                print("Profile updated successfully!")

    except Exception as e:
        print("Error during profile update:", e)


# Function to schedule a class trainer
def schedule_class(conn):
    try:
        with conn:
            with conn.cursor() as cur:
                # Ask the trainer for their ID
                trainer_id = input("Enter your trainer ID: ")

                # Ask the trainer for the details of the class they want to schedule
                class_name = input("Enter the name of the class: ")
                class_date = input("Enter the date of the class (YYYY-MM-DD): ")
                start_time = input("Enter the start time of the class (HH:MM): ")
                end_time = input("Enter the end time of the class (HH:MM): ")
                capacity = input("Enter the capacity of the class: ")

                # Insert the class into the classes table
                cur.execute("INSERT INTO classes (class_name, trainers_id, capacity, start_time, end_time, class_date) VALUES (%s, %s, %s, %s, %s, %s)", (class_name, trainer_id, capacity, start_time, end_time, class_date))

                # Commit the changes
                conn.commit()

                print("Class scheduled successfully!")

    except Exception as e:
        print("Error during scheduling class:", e)


# Function to book a class - member
def book_class(conn):
    try:
        with conn:
            with conn.cursor() as cur:
                # Ask the member for their ID
                member_id = input("Enter your member ID: ")

                # Ask the member for the ID of the class they want to book
                class_id = input("Enter the ID of the class you want to book: ")

                # Insert the booking into the takes table
                cur.execute("INSERT INTO takes (member_id, class_id) VALUES (%s, %s)", (member_id, class_id))

                # Commit the changes
                conn.commit()

                print("Class booked successfully!")

    except Exception as e:
        print("Error during booking class:", e)


#function to view member profile - trainer views it
def view_member_profile(conn):
    try:
        with conn:
            with conn.cursor() as cur:
                # Ask the trainer for the name of the member
                member_name = input("Enter the name of the member: ")

                # Fetch the member's profile from the members table
                cur.execute("SELECT * FROM members WHERE first_name = %s OR last_name = %s", (member_name, member_name))
                member = cur.fetchone()

                if member is not None:
                    # Print the member's profile
                    print(f"""
                    Member ID: {member[0]}
                    First Name: {member[1]}
                    Last Name: {member[2]}
                    Email: {member[3]}
                    Phone: {member[4]}
                    Age: {member[5]}
                    Sex: {member[6]}
                    Height: {member[7]}
                    Weight: {member[8]}
                    BMI: {member[9]}
                    Workout Duration: {member[10]}
                    Body Fat: {member[11]}
                    Calories Burned: {member[12]}
                    Calories Consumed: {member[13]}
                    Steps: {member[14]}
                    Distance: {member[15]}
                    Subscription Status: {member[16]}
                    Membership Type: {member[17]}
                    Payment Method: {member[18]}
                    """)
                else:
                    print("No member found with that name.")

    except Exception as e:
        print("Error during fetching member profile:", e)


# Function to view classes
def view_classes(conn):
    try:
        with conn:
            with conn.cursor() as cur:
                # Fetch all records from the 'classes' table
                cur.execute("SELECT * FROM classes")

                # Fetch all the rows
                rows = cur.fetchall()

                for row in rows:
                    print(f"""
                    Class ID: {row[0]}
                    Class Name: {row[1]}
                    Trainers ID: {row[2]}
                    Capacity: {row[3]}
                    Start Time: {row[4]}
                    End Time: {row[5]}
                    Class Date: {row[6]}
                    """)

    except Exception as e:
        print("Error during fetching classes:", e)


# Function to manage room booking - admin
def manage_room_booking(conn):
    try:
        with conn:
            with conn.cursor() as cur:
                # Ask the admin for the details of the booking they want to manage
                booking_id = input("Enter the ID of the booking you want to manage (leave blank to create a new booking): ")
                member_id = input("Enter the ID of the member making the booking: ")
                room_id = input("Enter the ID of the room being booked: ")
                booking_date = input("Enter the date of the booking (YYYY-MM-DD): ")
                start_time = input("Enter the start time of the booking (HH:MM): ")
                end_time = input("Enter the end time of the booking (HH:MM): ")
                purpose = input("Enter the purpose or description of the booking: ")
                status = input("Enter the status of the booking (e.g., confirmed, canceled, pending): ")

                if booking_id:
                    # Update the booking in the bookings table
                    cur.execute("UPDATE bookings SET member_id = %s, room_id = %s, booking_date = %s, start_time = %s, end_time = %s, purpose = %s, status = %s WHERE booking_id = %s", (member_id, room_id, booking_date, start_time, end_time, purpose, status, booking_id))
                else:
                    # Insert the booking into the bookings table
                    cur.execute("INSERT INTO bookings (member_id, room_id, booking_date, start_time, end_time, purpose, status) VALUES (%s, %s, %s, %s, %s, %s, %s)", (member_id, room_id, booking_date, start_time, end_time, purpose, status))

                # Commit the changes
                conn.commit()

                print("Booking managed successfully!")

    except Exception as e:
        print("Error during managing booking:", e)


# Function to view rooms
def view_rooms(conn):
    try:
        with conn:
            with conn.cursor() as cur:
                # Fetch all records from the 'rooms' table
                cur.execute("SELECT * FROM rooms")

                # Fetch all the rows
                rows = cur.fetchall()

                for row in rows:
                    print(f"""
                    Room ID: {row[0]}
                    Room Name: {row[1]}
                    Capacity: {row[2]}
                    """)

                # Fetch all records from the 'bookings' table
                cur.execute("SELECT * FROM bookings")

                # Fetch all the rows
                rows = cur.fetchall()

                for row in rows:
                    print(f"""
                    Booking ID: {row[0]}
                    Member ID: {row[1]}
                    Room ID: {row[2]}
                    Booking Date: {row[3]}
                    Start Time: {row[4]}
                    End Time: {row[5]}
                    Purpose: {row[6]}
                    Status: {row[7]}
                    """)

    except Exception as e:
        print("Error during fetching rooms:", e)


# Function to view class bookings
def view_class_bookings(conn):
    try:
        with conn:
            with conn.cursor() as cur:
                # Fetch all records from the 'takes' table joined with the 'classes' and 'members' tables
                cur.execute("""
                SELECT takes.member_id, members.first_name, members.last_name, takes.class_id, classes.class_name, classes.start_time, classes.end_time, classes.class_date
                FROM takes
                INNER JOIN classes ON takes.class_id = classes.class_id
                INNER JOIN members ON takes.member_id = members.member_id
                """)

                # Fetch all the rows
                rows = cur.fetchall()

                for row in rows:
                    print(f"""
                    Member ID: {row[0]}
                    Member Name: {row[1]} {row[2]}
                    Class ID: {row[3]}
                    Class Name: {row[4]}
                    Start Time: {row[5]}
                    End Time: {row[6]}
                    Class Date: {row[7]}
                    """)

    except Exception as e:
        print("Error during fetching class bookings:", e)


# Function to view room bookings
def view_room_bookings(conn):
    try:
        with conn:
            with conn.cursor() as cur:
                # Fetch all records from the 'bookings' table joined with the 'rooms' table
                cur.execute("""
                SELECT bookings.booking_id, bookings.member_id, bookings.room_id, rooms.room_name, rooms.capacity, bookings.booking_date, bookings.start_time, bookings.end_time, bookings.purpose, bookings.status
                FROM bookings
                INNER JOIN rooms ON bookings.room_id = rooms.room_id
                """)

                # Fetch all the rows
                rows = cur.fetchall()

                for row in rows:
                    print(f"""
                    Booking ID: {row[0]}
                    Member ID: {row[1]}
                    Room ID: {row[2]}
                    Room Name: {row[3]}
                    Room Capacity: {row[4]}
                    Booking Date: {row[5]}
                    Start Time: {row[6]}
                    End Time: {row[7]}
                    Purpose: {row[8]}
                    Status: {row[9]}
                    """)

    except Exception as e:
        print("Error during fetching bookings:", e)


# Function to monitor equipment maintenance - admin
def monitor_equipment_maintenance(conn):
    try:
        with conn:
            with conn.cursor() as cur:
                # Fetch all records from the 'equipment' table
                cur.execute("SELECT * FROM equipment")

                # Fetch all the rows
                rows = cur.fetchall()

                for row in rows:
                    print(f"""
                    Equipment ID: {row[0]}
                    Equipment Name: {row[1]}
                    Is Good: {row[2]}
                    """)

    except Exception as e:
        print("Error during fetching equipment records:", e)


# Function to update class schedule - admin
def update_class_schedule(conn):
    try:
        with conn:
            with conn.cursor() as cur:
                # Ask the admin for the details of the class they want to update
                class_id = input("Enter the ID of the class you want to update: ")
                class_name = input("Enter the new name of the class: ")
                trainers_id = input("Enter the new ID of the trainers: ")
                capacity = input("Enter the new capacity of the class: ")
                start_time = input("Enter the new start time of the class (HH:MM): ")
                end_time = input("Enter the new end time of the class (HH:MM): ")
                class_date = input("Enter the new date of the class (YYYY-MM-DD): ")

                # Update the class in the classes table
                cur.execute("UPDATE classes SET class_name = %s, trainers_id = %s, capacity = %s, start_time = %s, end_time = %s, class_date = %s WHERE class_id = %s", (class_name, trainers_id, capacity, start_time, end_time, class_date, class_id))

                # Commit the changes
                conn.commit()

                print("Class schedule updated successfully!")

    except Exception as e:
        print("Error during updating class schedule:", e)


# Function to process payment - admin
def process_payment(conn):
    try:
        with conn:
            with conn.cursor() as cur:
                # Ask the admin for the details of the payment they want to process
                bill_id = input("Enter the ID of the bill you want to process: ")
                member_id = input("Enter the member ID: ")
                amount = input("Enter the amount to bill: ")
                payment_status = input("Enter the new payment status (Paid/Unpaid): ")

                # Update the payment status, member_id, and amount in the billing table
                cur.execute("UPDATE billing SET member_id = %s, amount = %s, payment_status = %s WHERE bill_id = %s", (member_id, amount, payment_status, bill_id))

                # Commit the changes
                conn.commit()

                print("Payment processed successfully!")

    except Exception as e:
        print("Error during processing payment:", e)


# Function to view payments
def view_payments(conn):
    try:
        with conn:
            with conn.cursor() as cur:
                # Fetch all records from the 'billing' table
                cur.execute("SELECT * FROM billing")

                # Fetch all the rows
                rows = cur.fetchall()

                if rows:
                    print("Fetched all payment records successfully!")
                    for row in rows:
                        print(f"""
                        Bill ID: {row[0]}
                        Member ID: {row[1]}
                        Amount: {row[2]}
                        Payment Status: {row[3]}
                        """)
                else:
                    print("No payment records found.")

    except Exception as e:
        print("Error during fetching payment records:", e)



# Function to display the dashboard
# Function to display the dashboard
def display_dashboard(conn):
    while True:
        print("1. User Registration")
        print("2. View Members")
        print("3. Update Profile")
        print("4. Schedule Class")
        print("5. View Member Profile")
        print("6. Book Class")
        print("7. View Classes")
        print("8. Manage Room Booking")
        print("9. View Rooms")
        print("10. View Room Bookings")
        print("11. View Class Bookings")
        print("12. Monitor Equipment Maintenance")
        print("13. Update Class Schedule")
        print("14. Process Payment")
        print("15. View Payments")
        print("0. Exit")

        option = input("Select an option: ")

        if option == '1':
            input("Press Enter to start user registration...")
            user_registration(conn)
        elif option == '2':
            view_members(conn)
        elif option == '3':
            update_member_profile(conn)
        elif option == '4':
            schedule_class(conn)
        elif option == '5':
            view_member_profile(conn)
        elif option == '6':
            book_class(conn)
        elif option == '7':
            view_classes(conn)
        elif option == '8':
            manage_room_booking(conn)
        elif option == '9':
            view_rooms(conn)
        elif option == '10':
            view_room_bookings(conn)
        elif option == '11':
            view_class_bookings(conn)
        elif option == '12':
            monitor_equipment_maintenance(conn)
        elif option == '13':
            update_class_schedule(conn)
        elif option == '14':
            process_payment(conn)
        elif option == '15':
            view_payments(conn)
        elif option == '0':
            break
        else:
            print("Invalid option. Please try again.")

# Connect to the PostgreSQL database
conn = connect_to_database()

# If connection is successful, display the dashboard
if conn:
    display_dashboard(conn)
