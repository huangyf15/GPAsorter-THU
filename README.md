# README

## Before use

### Path Intro

* `bin`：编译好的可执行程序 `GPAcalculator_vX.Y.Z.exe` （X.Y.Z 为当前版本号）
* `test`：编写程序时的测试文件，包括输入文件 `input.txt` 与输出文件 `output.txt`
* `build, dist`：编译过程中生成的工程文件，其中可执行程序位于 `dist` 内

### Input file

输入文件要求为 `.txt` 文本文件，需要将表格中的必要数据粘贴到该文本文件，其中必要数据指如下信息：学号，姓名，教学班级，课程名，课序号，成绩，绩点成绩，考试时间，学分，课程属性，重修补考标志，特殊课程标记。

### Compile and Run

本程序有两种使用方法：

#### 直接运行可执行程序（推荐）

* 打开 `bin` 文件夹，将其中编译好的可执行程序移动至需要的任意路径 `PATH`，运行前将输入文件置于 `.exe` 同一路径 `PATH` 下；
* 打开命令行，进入 `PATH` 路径，输入 `./GPAcalculator_vX.Y.Z` 即可（X.Y.Z 要换成当前版本号）即可；输出文件位于 `PATH` 路径下。

#### 先编译源码后运行程序

* 打开命令行中，在 `run.sh` 所在路径输入 `sh run.sh`，自动生成包含有可执行程序的 `dist` 文件夹；
* 将输入文件置于 `dist` 文件夹，继续运行程序，生成的输出文件位于 `dist` 文件夹中。

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
