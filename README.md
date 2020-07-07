# README

## Requirement

程序运行前，需将必要数据粘贴到 `.txt` 文件中并将其置于 `.exe` 同一文件夹下。所谓必要数据，是指至少包含学号，姓名，教学班级，课程名，课序号，成绩，绩点成绩，考试时间，学分，课程属性，重修补考标志，特殊课程标记等信息。

## Definition

### Course-related Variables

* course_credit：课程学分(Course Credit)
* course_name：课程名(Course Name)
* course_type：课程属性(Course Type)
* course_id：课程号(Course ID)
* course_order：课序号(Course ID Order)
* bixiu：必修
* xianxuan：限选
* renxuan：任选
* bixian：必修+限选
* bixianren：必修+限选+任选

### Student-related Variables

* student_id：学号(Student ID)
* student_name：学生姓名(Student Name)
* teach_class：教学班级(Teaching Class)
* course_exam_time：考试时间(Exam Time)
* revamp_line/revamp_dict：重修补考标志(Revamp Mark)
* degree_type：特殊课程标记(Degree Type)
* grade：单一课程等级成绩(Grade)
* grade_point: 单一课程绩点成绩(Grade Point)
* *_credits：某一类型课程总学分(Total Credit)
* *_grade_points：某一类型课程总学分绩(Total Grade Point)
* *_GPA：某一类型课程平均学分绩(Grade Point Average)

### Functions

* cal_total_credit：计算总学分(Total Credit)
* cal_GPA：计算平均学分绩(Grade Point Average)

## Notice

本程序的学分绩计算均基于非 P/F 课程进行。