# -*- coding: UTF-8 -*-

import os

## Function: Calculate total credit
def cal_total_credit(course_credit,grade_point,total_credit,grade,revamp):
  if grade in ['EX','P','W','I','G']:
    return total_credit
  elif grade == 'F':
    if grade_point == 'N/A':
      return total_credit
    else:
      total_credit_new = total_credit + int(course_credit)
      return total_credit_new
  else:
    total_credit_new = total_credit + int(course_credit)
    return total_credit_new


## Function: Calculate GPA (Grade Point Average)
def cal_GPA(course_credit,grade_point,total_credit,grade,revamp):
  if grade in ['EX','P','W','I','G']:
    return total_credit
  elif grade == 'F':
    if grade_point == 'N/A':
      return total_credit
    else:
      total_credit_new = total_credit + int(course_credit)*float(grade_point)
      return total_credit_new
  else:
    total_credit_new = total_credit + int(course_credit)*float(grade_point)
    return total_credit_new


## Function: Calculate GPA (Grade Point Average)
def input_var(leading_words, choiceA, choiceA_words, choiceB, choiceB_words):
  var_value = input(leading_words)
  while var_value != choiceA and var_value != choiceB:
    var_value = input('输入有误。'+leading_words)
  if var_value == choiceA:
    print(choiceA_words)
  elif var_value == choiceB:
    print(choiceB_words)
  return var_value


## Function: Data preprocessing
def preproc(input_file_name,char_encoding):
  TorF = input_var('是否在任选课中剔除双学位和辅修课程：\
            \n\t剔除请输入T，保留请输入F，以回车结尾\n', \
            \
            'T','已选择剔除双学位和辅修课程\n', \
            \
            'F','已选择保留双学位和辅修课程\n')
  
  fail = input_var('是否保留已重修通过科目中的挂科记录：\
            \n\t保留请输入T，剔除请输入F，以回车结尾\n', \
            \
            'T','已选择保留已重修通过科目中的挂科记录\n', \
            \
            'F','已选择剔除已重修通过科目的挂科记录\n')
  
  ## write to "__temp.txt"
  with open(input_file_name,'r', encoding=char_encoding) as inp, \
    open('__temp.txt','a', encoding=char_encoding) as oup:
    title = inp.readline()
    title_col = title.rstrip().split('\t')
    ## Detect the data completeness
    try:
      student_id    = title_col.index('学号')
      student_name  = title_col.index('姓名')
      teach_class   = title_col.index('教学班级')
      course_name   = title_col.index('课程名')
      course_order  = title_col.index('课序号')
      grade         = title_col.index('成绩')
      grade_point   = title_col.index('绩点成绩')
      exam_time     = title_col.index('考试时间')
      course_credit = title_col.index('学分')
      course_type   = title_col.index('课程属性')
      revamp_line   = title_col.index('重修补考标志')
      degree_type   = title_col.index('特殊课程标记')
    except:
      print('数据不完整。请将必要数据粘贴到txt文件中使用，并至少包含如下信息：\
         \n\t学号，姓名，教学班级，课程名，课序号，成绩，绩点成绩，考试时间，\
         \n\t学分，课程属性，重修补考标志，特殊课程标记等\n')
      os.system('pause')
      exit()
    oup.write(title)
    lines = inp.readlines()
    total_line = []

    ## Establish the dictionary
    # Point "student_id+course_order" to the last exam_time
    revamp_dict = {}
    for j in lines:
      i = j.rstrip().split('\t')
      total_line.append(j)
      if i[revamp_line] =='重修':
        if i[student_id]+i[course_order] in revamp_dict.keys():
          if int(i[exam_time]) > int(revamp_dict[i[student_id]+i[course_order]]):
            revamp_dict[i[student_id]+i[course_order]]= i[exam_time]
        else:
          revamp_dict[i[student_id]+i[course_order]] = i[exam_time]
    
    final_line = []
    if TorF == 'F':
      final_line = total_line
    else:
      ## Delete Dual Degree Courses
      # According to student_id + course_order
      for i in total_line:
        j = i.rstrip().split('\t')
        if j[degree_type] == '第一学位课程':
          final_line.append(i)
    
    final_line2 = []
    if fail =='T':
      final_line2 = final_line
    else:
      for i in final_line:
        j = i.rstrip().split()
        ## Save all the passing courses and the last one in revamped courses
        if j[student_id]+j[course_order] not in revamp_dict.keys():
          final_line2.append(i)
        elif j[exam_time] == revamp_dict[j[student_id]+j[course_order]]:
          final_line2.append(i)
    for j in final_line2:    
      oup.write(j)
        

## Function: Process and output the GPA
def mainproc(output_file_name,char_encoding):
  ## Read cleaned "__temp.txt" and calculate GPA
  with open('__temp.txt', 'r', encoding=char_encoding) as inp, \
    open(output_file_name, 'w', encoding=char_encoding) as summary:
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
    revamp_line   = title_col.index('重修补考标志')
    degree_type   = title_col.index('特殊课程标记')

    stu_course_list = inp.readlines()

    student_id_n = []
    student_name_n = []
    teach_class_n = []
    bixiu_credits = []
    bixiu_grade_points = []
    xianxuan_credits = []
    xianxuan_grade_points = []
    renxuan_credits = []
    renxuan_grade_points = []
    bixian_GPA = []
    bixianren_GPA = []
    bixianren_credits=[]
    bixianren_grade_points = []

    j = 0
    for i in stu_course_list:
      i = i.rstrip().split('\t')
      if i[student_id] not in student_id_n:
        student_id_n.append(i[student_id])
        student_name_n.append(i[student_name])
        teach_class_n.append(i[teach_class])
        bixiu_credits.append(0)
        bixiu_grade_points.append(0)
        xianxuan_credits.append(0)
        xianxuan_grade_points.append(0)
        renxuan_credits.append(0)
        renxuan_grade_points.append(0)
        bixianren_credits.append(0)
        j = j +1
        print(str(j)+student_name_n[j-1])
      poc = student_id_n.index(i[student_id])
      if '体疗' in i[course_name]:
        bixianren_credits[poc] = bixianren_credits[poc]+1
        renxuan_credits[poc] = renxuan_credits[poc]+1
        renxuan_grade_points[poc] = renxuan_grade_points[poc]+0.8
        print('含有体疗课程')
        continue        
      if i[course_type] == '必修':
        if i[grade] not in['F','W','I']:
          bixianren_credits[poc] = bixianren_credits[poc]+int(i[course_credit])
        bixiu_credits[poc] = cal_total_credit(i[course_credit],i[grade_point],bixiu_credits[poc],i[grade],i[revamp_line])
        bixiu_grade_points[poc] = cal_GPA(i[course_credit],i[grade_point],bixiu_grade_points[poc],i[grade],i[revamp_line])
      elif i[course_type] == '限选':
        if i[grade] not in['F','W','I']:
          bixianren_credits[poc] = bixianren_credits[poc]+int(i[course_credit])
        xianxuan_credits[poc] = cal_total_credit(i[course_credit],i[grade_point],xianxuan_credits[poc],i[grade],i[revamp_line])
        xianxuan_grade_points[poc] = cal_GPA(i[course_credit],i[grade_point],xianxuan_grade_points[poc],i[grade],i[revamp_line])
      else:
        if i[grade] not in['F','W','I']:
          bixianren_credits[poc] = bixianren_credits[poc]+int(i[course_credit])
        renxuan_credits[poc] = cal_total_credit(i[course_credit],i[grade_point],renxuan_credits[poc],i[grade],i[revamp_line])
        renxuan_grade_points[poc] = cal_GPA(i[course_credit],i[grade_point],renxuan_grade_points[poc],i[grade],i[revamp_line])

    print("总统计人数为："+str(j)+"\n")

    summary.write('学号\t姓名\t教学班级\t总完成学分\t必修限选平均学分绩\t必修限选平均学分绩排名\t所有课程平均学分绩\t所有成绩平均学分绩排名\t总学分绩\t总学分绩排名\t非PF学分\n')
    for g in range(0,j):
      if bixiu_credits[g]+xianxuan_credits[g]==0:
        bixian_GPA.append(0)
      else:
        bixian_GPA.append((bixiu_grade_points[g]+xianxuan_grade_points[g])/(bixiu_credits[g]+xianxuan_credits[g]))
      if bixiu_credits[g]+xianxuan_credits[g]+renxuan_credits[g]==0:
        bixianren_GPA.append(0)
      else:
        bixianren_GPA.append((bixiu_grade_points[g]+xianxuan_grade_points[g]+renxuan_grade_points[g])/(bixiu_credits[g]+xianxuan_credits[g]+renxuan_credits[g]))
      bixianren_grade_points.append(bixiu_grade_points[g]+xianxuan_grade_points[g]+renxuan_grade_points[g])
    for g in range(0,j):
      summary.write(str(student_id_n[g])+"\t"+str(student_name_n[g])+"\t"+str(teach_class_n[g])+"\t"+str(bixianren_credits[g])+"\t"+str(round(bixian_GPA[g],3))+'\t' \
                    +str(sorted(bixian_GPA,reverse = True).index(bixian_GPA[g])+1)+'\t'+str(round(bixianren_GPA[g],3))+'\t'+str(sorted(bixianren_GPA,reverse = True).index(bixianren_GPA[g])+1)+'\t' \
                    +str(round(bixianren_grade_points[g],3))+'\t'+str(sorted(bixianren_grade_points,reverse = True).index(bixianren_grade_points[g])+1)+'\t'+str(bixiu_credits[g]+xianxuan_credits[g]+renxuan_credits[g])+'\n')
  os.remove('__temp.txt') 


## Main process
print("亲爱的用户，欢迎您试用“李导帮你算成绩”程序2.1版本 \
     \n感谢您对本程序的支持 \
     \n如有程序运行错误，欢迎微信联系作者李天奇：litq_94 \
     \n一键生成成绩排名-尽享假期生活\n\n")
char_encoding = input_var('请选择文本文件采用的字符编码方案（依照 Windows 记事本编码模式）：\
            \n\tUTF-8编码请输入utf-8，ANSI编码请输入ansi（为记事本默认存储编码），以回车结尾\n', \
            \
            'utf-8','已选择UTF-8编码方案\n', \
            \
            'ansi','已选择ANSI编码方案\n')
input_file_name = input("请输入你要进行成绩排序的 txt 文件名称（不必带后缀名），回车键结束\n")
output_file_name = input("请输入你想要写入排序结果的 txt 文件名称（不必带后缀名），回车键结束\n")
preproc(input_file_name+'.txt',char_encoding)
mainproc(output_file_name+'.txt',char_encoding)
print("排名计算已结束，可以在文件中进行查看。\n 欢迎您下次使用。如果进一步需求，欢迎微信联系原作者李天奇：litq_94")
os.system('pause')
