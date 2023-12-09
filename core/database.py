import psycopg2


connection= psycopg2.connect(
    host= "localhost",
    database = "test_regs",
    user= "xeniya",
    password = "123",
    port= "5432",
)

def create_table():               # если cursor открыть   core
    with connection.cursor() as cursor:                       #автоматичесски открой и закрой поэтому пишем connection
        cursor.execute("CREATE TABLE IF NOT EXISTS users(\
                   id SERIAL PRIMARY KEY, \
                    user_id BIGINT,\
                    username VARCHAR(255) DEFAULT NULL,\
                    first_name VARCHAR(255) DEFAULT NULL,\
                    last_name VARCHAR(255) DEFAULT NULL,\
                   phone VARCHAR(255) DEFAULT NULL,\
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
        connection.commit()
    

def insert_users(user_id, username, first_name, last_name, phone,):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO users(\
                       user_id, username, first_name, last_name, phone)\
                       VALUES(%s,%s,%s,%s,%s)",
                       (user_id, username, first_name, last_name, phone))
        connection.commit()
        

def find_user(user_id):
    with connection.cursor() as cursor:
        cursor.execute(f"select user_id from users where user_id = {user_id}")

        user = cursor.fetchone()
        return user


def pull_user(user_id):
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * from users where user_id = {user_id}")
            user = cursor.fetchone()           
        u = f"""User Id: @{user[1]}
First name : {user[3]}
Last name : {user[4]}
Username : {user[2]}
Phone : {user[5]}"""         
        return u


def admin_get_users():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * from users")

        all_users = cursor.fetchall()

    info = ""
    

    for i in all_users:
        info += f"username: {i[2]}\nPhone: {i[5]}\n\n"
        
    return info



# def delete_p(del_id):
#     with connection.cursor() as cursor:
#         cursor.execute(f"SELECT * from users where user_id = {del_id}")
#         user = cursor.fetchone()  






#  def admin_get_users():
#     with connection.cursor() as cursor:
#         cursor.execute("SELECT * from users")

#         all_users = cursor.fetchall()
#     for i in all_users:
#         print(i[2])


#     #return all_users
# print(admin_get_users())       



#сам автоматически заполняет, вписывать не надо)  похож primary key. ЕСли не заполнять то базово curenttimestamp.
#connection (main py) тогда connection в create_table



