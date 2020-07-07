# README

This is a simple GPA calculator for Students in Tsinghua University.

## Structure

* `bin`：编译好的可执行程序 `GPAcalculator_vX.Y.Z.exe` （X.Y.Z 为当前版本号）
* `test`：编写程序时的测试文件，包括输入文件 `input.txt` 与输出文件 `output.txt`
* `build, dist`：编译过程中生成的工程文件，其中可执行程序位于 `dist` 内

## Before use

### Input file

输入文件要求为 `.txt` 文本文件，需要将表格中的必要数据粘贴到该文本文件，其中必要数据指如下信息：学号，姓名，教学班级，课程名，课序号，成绩，绩点成绩，考试时间，学分，课程属性，重修补考标志，特殊课程标记。

### Compile and Run

本程序有两种使用方法：

* 直接运行（推荐）：打开命令行或双击左键直接运行已编译好的可执行程序 `GPAcalculator.exe`
* 先编译再运行：打开命令行运行 `Shell` 脚本 `run.sh`，编译好的可执行程序将被置于 `dist` 文件夹内

注意，输入/输出文件的相对路径应以**可执行程序的所在路径**为基准。

## Definition

### Course-related Variables

* course_credit：课程学分(Course Credit)
* course_name：课程名(Course Name)
* course_type：课程属性(Course Type)
* course_id：课程号(Course ID)
* course_order：课序号(Course ID Order)
* bixian_*：必修+限选
* bixianren_*：必修+限选+任选

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
