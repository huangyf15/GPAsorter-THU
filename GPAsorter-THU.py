#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
"""GPA-sorter-THU
* course-related variables
  * course_credit：课程学分(Course Credit)
  * course_name：课程名(Course Name)
  * course_type：课程属性(Course Type)
  * course_id：课程号(Course ID)
  * course_order：课序号(Course ID Order)
  * bixian_*：必修+限选
  * bixianren_*：必修+限选+任选
* student-related variables
  * student_id：学号(Student ID)
  * student_name：学生姓名(Student Name)
  * teach_class：教学班级(Teaching Class)
  * exam_time：考试时间(Exam Time)
  * revamp_mark：重修补考标志(Revamp Mark)
  * degree_type：特殊课程标记(Degree Type)
  * grade：单一课程等级成绩(Grade)
  * grade_point: 单一课程绩点成绩(Grade Point)
  * *_credits：某一类型课程总学分(Total Credit)
  * *_grade_points：某一类型课程总学分绩(Total Grade Point)
  * *_GPA：某一类型课程平均学分绩(Grade Point Average)
"""

import os

def main():
  """main procedure
  """
  # Print leading words
  print("\n亲爱的用户，欢迎您试用“李导帮你算成绩”程序，感谢您对本程序的支持！ \
      \n\n如有程序运行错误，欢迎微信联系程序原作者或在 GitHub 项目提交新的 issue\
      \n- 程序原作者：李天奇（微信号 litq_94）\
      \n- 项目 GitHub 网址：https://github.com/huangyf15/GPAsorter-THU \
      \n\n--- 一键生成成绩排名-尽享愉快假期生活 --- \n")
  print("--------------------- Input information ---------------------")
  # Input necessary info
  input_file_name = input('\n- 请输入你要进行成绩排序的 txt 输入文件名称，回车键结束 \
              \n\t（不能带后缀名；输入文件默认位于可执行程序所在文件夹，也可选择另行前缀相对路径）\n')
  output_file_name = input('\n- 请输入你想要写入排序结果的 txt 输出文件名称，回车键结束 \
              \n\t（不能带后缀名；输出文件默认位于可执行程序所在文件夹，也可选择另行前缀相对路径）\n')
  char_encoding = input_var('\n- 请选择文本文件采用的字符编码方案（依照 Windows 记事本对编码模式的命名方式）：\
              \n\tUTF-8 编码请输入 utf-8，ANSI 编码请输入 ansi（为记事本默认存储编码），以回车结尾 \
              \n\t默认：UTF-8 编码，直接回车即可\n', \
              \
              'utf-8','已选择 UTF-8 编码方案\n', \
              \
              'ansi','已选择 ANSI 编码方案\n')
  # Calculate and sort
  preproc(input_file_name+'.txt',char_encoding)
  cal_and_sort(output_file_name+'.txt',char_encoding)
  print("排名计算已结束，可以在 txt 输出文件中进行查看。欢迎您下次使用！\
        \n\n如有进一步需求，欢迎微信联系原作者或在 GitHub 项目提交新的 issue：\
        \n- 程序原作者：李天奇（微信号 litq_94）\
        \n- 项目 GitHub 网址：https://github.com/huangyf15/GPAsorter-THU\n")


def cal_total_credit(course_credit,grade_point,total_credit,grade,flag_exclude_pass):
  """calculate total credit
  
  Returns: 
    total credit
  """
  if grade in ['EX','W','I','G']:
    return total_credit
  elif grade == 'P':
    if flag_exclude_pass == 'T':
      return total_credit
    else:
      total_credit_new = total_credit + int(course_credit)
      return total_credit_new
  elif grade == 'F':
    if grade_point == 'N/A':
      return total_credit
    else:
      total_credit_new = total_credit + int(course_credit)
      return total_credit_new
  else:
    total_credit_new = total_credit + int(course_credit)
    return total_credit_new


def cal_GPA(course_credit,grade_point,grade_points,grade):
  """calculate GPA (Grade Point Average)
  
  Returns: 
    total grade point, i.e. GPA
  """
  if grade in ['EX','P','W','I','G']:
    return grade_points
  elif grade == 'F':
    if grade_point == 'N/A':
      return grade_points
    else:
      grade_points_new = grade_points + int(course_credit)*float(grade_point)
      return grade_points_new
  else:
    grade_points_new = grade_points + int(course_credit)*float(grade_point)
    return grade_points_new


def input_var(leading_words, choiceA, choiceA_words, choiceB, choiceB_words):
  """detect the input string variables

  Returns:
    legal string value (choiceA or choiceB)
  """
  var_value = input(leading_words)
  while var_value != "" and var_value != choiceA and var_value != choiceB:
    var_value = input('输入有误。'+leading_words)
  if var_value == "":
    var_value = choiceA
  if var_value == choiceA:
    print(choiceA_words)
  elif var_value == choiceB:
    print(choiceB_words)
  return var_value


def preproc(input_file_name,char_encoding):
  """preprocess the data

  Write the preprocessed data to a temporary file.
  """
  # Print leading words
  print("----------------------- Preprocessing -----------------------")
  # Input Flags
  flag_exclude_double_degree = input_var('\n- 是否在任选课中剔除双学位和辅修课程：\
                          \n\t剔除请输入 T，保留请输入 F，以回车结尾 \
                          \n\t默认：T（剔除双学位和辅修课程），直接回车即可\n', \
                          \
                          'T','已选择剔除双学位和辅修课程\n', \
                          \
                          'F','已选择保留双学位和辅修课程\n')
  
  flag_exclude_fail_revamp = input_var('\n- 是否剔除已重修通过科目中的挂科记录：\
                          \n\t剔除请输入 T，保留请输入 F，以回车结尾 \
                          \n\t默认：T（剔除已重修通过科目中的挂科记录），直接回车即可\n', \
                          \
                          'T','已选择剔除已重修通过科目中的挂科记录\n', \
                          \
                          'F','已选择保留已重修通过科目的挂科记录\n')
  
  # Write to "__temp.txt"
  with open(input_file_name,'r', encoding=char_encoding) as inp, \
    open('__temp.txt','a', encoding=char_encoding) as oup:
    title = inp.readline()
    title_col = title.rstrip().split('\t')

    # Detect the data completeness
    try:
      student_id    = title_col.index('学号')
      student_name  = title_col.index('姓名')
      teach_class   = title_col.index('教学班级')
      course_name   = title_col.index('课程名')
      course_id     = title_col.index('课程号')
      grade         = title_col.index('成绩')
      grade_point   = title_col.index('绩点成绩')
      exam_time     = title_col.index('考试时间')
      course_credit = title_col.index('学分')
      course_type   = title_col.index('课程属性')
      revamp_mark   = title_col.index('重修补考标志')
      degree_type   = title_col.index('特殊课程标记')
    except:
      print('数据不完整。请将必要数据粘贴到txt文件中使用，并至少包含如下信息：\
         \n\t学号，姓名，教学班级，课程号，课程名，成绩，绩点成绩，考试时间，\
         \n\t学分，课程属性，重修补考标志，特殊课程标记等\n')
      os.system('pause')
      exit()
    oup.write(title)
    lines = inp.readlines()
    total_line = []

    # Establish the dictionary: Point "student_id+course_id" to the last exam_time
    revamp_dict = {}
    for j in lines:
      i = j.rstrip().split('\t')
      total_line.append(j)
      if i[revamp_mark] =='重修':
        if i[student_id]+i[course_id] in revamp_dict.keys():
          if int(i[exam_time]) > int(revamp_dict[i[student_id]+i[course_id]]):
            revamp_dict[i[student_id]+i[course_id]]= i[exam_time]
        else:
          revamp_dict[i[student_id]+i[course_id]] = i[exam_time]
    
    # Delete Dual Degree Courses according to "student_id+course_id"
    final_line = []
    if flag_exclude_double_degree == 'F':
      final_line = total_line
    else:
      for i in total_line:
        j = i.rstrip().split('\t')
        if j[degree_type] == '第一学位课程':
          final_line.append(i)
    
    # Save all the passing courses and the last one in revamped courses
    final_line2 = []
    if flag_exclude_fail_revamp =='F':
      final_line2 = final_line
    else:
      for i in final_line:
        j = i.rstrip().split()
        if j[student_id]+j[course_id] not in revamp_dict.keys():
          final_line2.append(i)
        elif j[exam_time] == revamp_dict[j[student_id]+j[course_id]]:
          final_line2.append(i)
    for j in final_line2:    
      oup.write(j)


def cal_and_sort(output_file_name,char_encoding):
  """calculate and output GPA

  Read data from the temporary file, calculate and sort students' GPA.
  """
  # Print leading words
  print("----------------------- Main process -----------------------")
  # Input Flags
  flag_exclude_pass = input_var('\n- 是否在计算 GPA 时剔除已通过科目中的 P/F 课程：\
                        \n\t剔除请输入 T（一般选择剔除），保留请输入 F，以回车结尾 \
                        \n\t默认：T（剔除已通过科目中的 P/F 课程），直接回车即可\n', \
                        \
                        'T','已选择剔除已通过科目中的 P/F 课程\n', \
                        \
                        'F','已选择保留已通过科目中的 P/F 课程\n')
  
  # Read cleaned "__temp.txt" and calculate GPA
  with open('__temp.txt', 'r', encoding=char_encoding) as inp, \
    open(output_file_name, 'w', encoding=char_encoding) as oup:
    title = inp.readline()
    title_col = title.rstrip().split()

    student_id    = title_col.index('学号')
    student_name  = title_col.index('姓名')
    teach_class   = title_col.index('教学班级')
    course_name   = title_col.index('课程名')
    grade         = title_col.index('成绩')
    grade_point   = title_col.index('绩点成绩')
    course_credit = title_col.index('学分')
    course_type   = title_col.index('课程属性')
    revamp_mark   = title_col.index('重修补考标志')
    degree_type   = title_col.index('特殊课程标记')

    stu_course_list = inp.readlines()

    student_id_n   = []
    student_name_n = []
    teach_class_n  = []

    bixian_GPA             = []
    bixian_credits         = []
    bixian_grade_points    = []
    bixianren_GPA          = []
    bixianren_credits      = []
    bixianren_grade_points = []
    if flag_exclude_pass == 'T':
      bixianren_credits_incP = []
      string_exclude_pass = '（不计入P课程）'
    else:
      string_exclude_pass = '（计入P课程）'

    # Calculate credits and grade points
    j = 0
    for i in stu_course_list:
      i = i.rstrip().split('\t')
      if i[student_id] not in student_id_n:
        student_id_n.append(i[student_id])
        student_name_n.append(i[student_name])
        teach_class_n.append(i[teach_class])
        bixian_credits.append(0)
        bixian_grade_points.append(0)
        bixianren_credits.append(0)
        bixianren_grade_points.append(0)
        bixianren_credits_incP.append(0)
        j = j + 1
        print(str(j)+' '+student_name_n[j-1])
      poc = student_id_n.index(i[student_id])
      if '体疗' in i[course_name]:
        bixianren_credits[poc] = bixianren_credits[poc] + 1
        if flag_exclude_pass == 'T':
          bixianren_credits_incP[poc] = bixianren_credits_incP[poc] + 1
        bixianren_grade_points[poc] = bixianren_grade_points[poc] + 0.8 * 1.3
        print('含有体疗课程')
        continue        
      if i[course_type] in ['必修','限选']:
        bixian_credits[poc] = cal_total_credit(i[course_credit],i[grade_point],bixian_credits[poc],i[grade],flag_exclude_pass)
        bixian_grade_points[poc] = cal_GPA(i[course_credit],i[grade_point],bixian_grade_points[poc],i[grade])
      if flag_exclude_pass == 'T':
        bixianren_credits_incP[poc] = cal_total_credit(i[course_credit],i[grade_point],bixianren_credits_incP[poc],i[grade],'F')
      bixianren_credits[poc] = cal_total_credit(i[course_credit],i[grade_point],bixianren_credits[poc],i[grade],flag_exclude_pass)
      bixianren_grade_points[poc] = cal_GPA(i[course_credit],i[grade_point],bixianren_grade_points[poc],i[grade])
    print("总统计人数为："+str(j)+"\n")

    # Calculate GPA
    for g in range(0,j):
      if bixian_credits[g]==0:
        bixian_GPA.append(0)
      else:
        bixian_GPA.append(bixian_grade_points[g]/bixian_credits[g])
      if bixianren_credits[g]==0:
        bixianren_GPA.append(0)
      else:
        bixianren_GPA.append(bixianren_grade_points[g]/bixianren_credits[g])

    # Write to the output file
    if flag_exclude_pass == 'T':
      oup.write('学号\t姓名\t教学班级\t必限总学分'+string_exclude_pass+'\t必限总绩\t必限GPA\tRank-必限GPA'+\
                    '\t必限任总学分'+string_exclude_pass+'\t必限任总绩\t必限任GPA\tRank-必限任GPA'+\
                    '\t必限任总学分（计入P课程）\n')
      for g in range(0,j):
        oup.write(str(student_id_n[g])+'\t'+str(student_name_n[g])+'\t'+str(teach_class_n[g])+ \
            '\t'+str(bixian_credits[g])+'\t'+str(round(bixian_grade_points[g],3))+ \
            '\t'+str(round(bixian_GPA[g],3))+'\t'+str(sorted(bixian_GPA,reverse = True).index(bixian_GPA[g])+1)+ \
            '\t'+str(bixianren_credits[g])+'\t'+str(round(bixianren_grade_points[g],3))+ \
            '\t'+str(round(bixianren_GPA[g],3))+'\t'+str(sorted(bixianren_GPA,reverse = True).index(bixianren_GPA[g])+1)+ \
            '\t'+str(bixianren_credits_incP[g])+'\n')
    else:
      oup.write('学号\t姓名\t教学班级\t必限总学分'+string_exclude_pass+'\t必限总绩\t必限GPA\tRank-必限GPA'+\
                    '\t必限任总学分'+string_exclude_pass+'\t必限任总绩\t必限任GPA\tRank-必限任GPA\n')
      for g in range(0,j):
        oup.write(str(student_id_n[g])+'\t'+str(student_name_n[g])+'\t'+str(teach_class_n[g])+ \
            '\t'+str(bixian_credits[g])+'\t'+str(round(bixian_grade_points[g],3))+ \
            '\t'+str(round(bixian_GPA[g],3))+'\t'+str(sorted(bixian_GPA,reverse = True).index(bixian_GPA[g])+1)+ \
            '\t'+str(bixianren_credits[g])+'\t'+str(round(bixianren_grade_points[g],3))+ \
            '\t'+str(round(bixianren_GPA[g],3))+'\t'+str(sorted(bixianren_GPA,reverse = True).index(bixianren_GPA[g])+1)+ \
            '\n')
  
  os.remove('__temp.txt') 


if __name__ == '__main__':
  main()
  os.system('pause')
