import sqlite3

# 连接数据库（如果文件不存在会自动创建）
conn = sqlite3.connect("school.db")
cursor = conn.cursor()


# 创建表
def create_tables():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS student (
            name TEXT NOT NULL,
            sex TEXT CHECK(sex IN ('Male', 'Female')) NOT NULL,
            age INTEGER CHECK(age > 0),
            studentID TEXT PRIMARY KEY,
            score REAL CHECK(score >= 0)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS teacher (
            name TEXT NOT NULL,
            sex TEXT CHECK(sex IN ('Male', 'Female')) NOT NULL,
            age INTEGER CHECK(age > 0),
            department TEXT NOT NULL,
            teacherID TEXT PRIMARY KEY,
            course TEXT NOT NULL,
            salary REAL CHECK(salary >= 0)
        )
    """)
    conn.commit()
    print("Tables created successfully.")


# 插入数据
def insert_data():
    # 插入学生信息
    cursor.executemany("""
        INSERT INTO student (name, sex, age, studentID, score)
        VALUES (?, ?, ?, ?, ?)
    """, [
        ("Alice", "Female", 20, "S001", 85.5),
        ("Bob", "Male", 22, "S002", 90.0),
        ("Jack", "Male", 24, "S003", 80.0)
    ])
    # 插入教师信息
    cursor.executemany("""
        INSERT INTO teacher (name, sex, age, department, teacherID, course, salary)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, [
        ("Dr. Smith", "Male", 40, "Mathematics", "T001", "Calculus", 8000),
        ("Ms. Johnson", "Female", 35, "Physics", "T002", "Quantum Mechanics", 7500),
        ("Dr. Mike", "Male", 43, "CS", "T003", "Network", 10000)
    ])
    conn.commit()
    print("Data inserted successfully.")


# 查询数据
def query_data():
    print("Student Information:")
    for row in cursor.execute("SELECT * FROM student"):
        print(row)
    print("\nTeacher Information:")
    for row in cursor.execute("SELECT * FROM teacher"):
        print(row)


# 修改数据
def update_data():
    # 更新学生成绩
    cursor.execute("UPDATE student SET score = ? WHERE studentID = ?", (95.0, "S001"))
    # 更新教师薪水
    cursor.execute("UPDATE teacher SET salary = ? WHERE teacherID = ?", (8500, "T002"))
    conn.commit()
    print("Data updated successfully.")


# 删除数据
def delete_data():
    # 删除指定学生
    cursor.execute("DELETE FROM student WHERE studentID = ?", ("S002",))
    # 删除指定教师
    cursor.execute("DELETE FROM teacher WHERE teacherID = ?", ("T001",))
    conn.commit()
    print("Data deleted successfully.")


# 主程序
if __name__ == "__main__":
    create_tables()  # 创建表
    insert_data()    # 插入数据
    print("\nBefore update:")
    query_data()     # 查询数据
    update_data()    # 修改数据
    print("\nAfter update:")
    query_data()     # 查询数据
    delete_data()    # 删除数据
    print("\nAfter deletion:")
    query_data()     # 查询数据

# 关闭数据库连接
conn.close()
