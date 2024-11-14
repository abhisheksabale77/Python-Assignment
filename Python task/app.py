import tkinter as tk
from tkinter import messagebox

students = []
total_sessions = 1 

def add_student():
    name = entry_name.get()
    age = entry_age.get()
    grade = entry_grade.get()

    if not (name and age and grade):
        messagebox.showerror("Input Error", "All fields are required.")
        return

    for student in students:
        if student["name"] == name and student["age"] == age:
            messagebox.showerror("Duplicate Student", "This student already exists.")
            return

    student = {"name": name, "age": age, "grade": grade, "sessions_attended": 0, "lectures_present": 0}
    students.append(student)
    
    messagebox.showinfo("Success", "Student added successfully.")
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_grade.delete(0, tk.END)
    view_students()

def view_students():
    student_listbox.delete(0, tk.END)  

    for index, student in enumerate(students):
        attendance_percentage = (student["lectures_present"] / total_sessions * 100) if total_sessions > 0 else 0
        student_listbox.insert(
            tk.END,
            f"ID: {index}, Name: {student['name']}, Age: {student['age']}, "
            f"Grade: {student['grade']}, Total Sessions: {total_sessions}, "
            f"Sessions Attended: {student['lectures_present']}, "
            f"Attendance %: {attendance_percentage:.2f}%"
        )

def start_new_session():
    global total_sessions
    total_sessions += 1 

    for student in students:
        student["attendance"] = "Absent"  

    view_students()

    messagebox.showinfo("New Session", f"New session started. Total sessions: {total_sessions}.")

def mark_present():
    selected_items = student_listbox.curselection()  
    if not selected_items:
        messagebox.showerror("Error", "Please select at least one student to mark as Present.")
        return

    for item in selected_items:
        student = students[item]
        student["attendance"] = "Present"
        student["lectures_present"] += 1
    
    messagebox.showinfo("Success", "Selected students marked as Present for the current session.")
    view_students()


def mark_absent():
    selected_items = student_listbox.curselection() 
    if not selected_items:
        messagebox.showerror("Error", "Please select at least one student to mark as Absent.")
        return

    for item in selected_items:
        student = students[item]
        student["attendance"] = "Absent"
    
    messagebox.showinfo("Success", "Selected students marked as Absent for the current session.")
    view_students()

def remove_student():
    try:
        selected_item = student_listbox.curselection()[0] 
        student = students.pop(selected_item)  
        
        messagebox.showinfo("Success", f"Student {student['name']} removed successfully.")
        view_students()
    except IndexError:
        messagebox.showerror("Error", "Please select a student to remove.")


root = tk.Tk()
root.title("College Attendance System")


frame_form = tk.Frame(root)
frame_form.pack(pady=10)

tk.Label(frame_form, text="Name").grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(frame_form)
entry_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Age").grid(row=1, column=0, padx=5, pady=5)
entry_age = tk.Entry(frame_form)
entry_age.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Grade").grid(row=2, column=0, padx=5, pady=5)
entry_grade = tk.Entry(frame_form)
entry_grade.grid(row=2, column=1, padx=5, pady=5)

btn_add = tk.Button(root, text="Add Student", command=add_student)
btn_add.pack(pady=5)

btn_new_session = tk.Button(root, text="Start New Session", command=start_new_session)
btn_new_session.pack(pady=5)

btn_present = tk.Button(root, text="Mark as Present", command=mark_present)
btn_present.pack(pady=5)

btn_absent = tk.Button(root, text="Mark as Absent", command=mark_absent)
btn_absent.pack(pady=5)

btn_remove = tk.Button(root, text="Remove Selected Student", command=remove_student)
btn_remove.pack(pady=5)


student_listbox = tk.Listbox(root, width=100, selectmode=tk.MULTIPLE)
student_listbox.pack(pady=10)


view_students()

root.mainloop()
