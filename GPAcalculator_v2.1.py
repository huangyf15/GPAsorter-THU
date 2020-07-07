import os
# (i[xuefen],i[chengji],bixiu_num[poc],i[chengji_class],i[chongxiu])
##计算学分
def calCredits(fen,ji,num,classji,chong):
  if classji in ['EX','P','W','I','G']:
    return num
  elif classji == 'F':
    if ji == 'N/A':
      return num
    else:
      num_new = num + int(fen)
      return num_new
  else:
    num_new = num + int(fen)
    return num_new


# (i[xuefen],i[chengji],bixiu_num[poc],i[chengji_class],i[chongxiu])
##计算学分绩
def calGPA(fen,ji,num,classji,chong):
  if classji in ['EX','P','W','I','G']:
    return num
  elif classji == 'F':
    if ji == 'N/A':
      return num
    else:
      num_new = num + int(fen)*float(ji)
      return num_new
  else:
    num_new = num + int(fen)*float(ji)
    return num_new

    
##预处理数据
def preproc(wenjian_name):
  TorF = input('是否在任选课中剔除双学位和辅修课程：剔除双学位和辅修课程请输入T，保留双学位和辅修课程请输入F，以回车结尾\n')
  while TorF != 'T' and TorF != 'F':
    TorF = input('输入有误。请重新选择是否在任选课中剔除双学位课程：剔除双学位课程请输出T，保留双学位课程请输入F，以回车结尾\n')
  if TorF == 'T':
    print('已选择剔除双学位课程\n')
  elif TorF == 'F':
    print('已选择保留双学位课程\n')
        

  fail = input('是否剔除已重修通过科目中过去的挂科记录，保留过去挂科记录请输入T，剔除请输入F，以回车结尾\n')
  while fail != 'T' and fail != 'F':
    fail = input('输入有误。请重新选择是否剔除已重修通过科目中过去的挂科记录，保留过去挂科记录请输入T，剔除请输入F，以回车结尾\n')
  if fail == 'T':
    print('已选择保留过去挂科记录\n')
  elif fail == 'F':
    print('已选择剔除过去挂科记录\n')
  ##生成一个临时数据文件__temp.txt
  with open(wenjian_name,'r') as inp, open('__temp.txt','a') as oup:
    title = inp.readline()
    title_col = title.rstrip().split('\t')
    ##数据完整性检查
    try:
      num = title_col.index('学号')
      name = title_col.index('姓名')
      classname = title_col.index('教学班级')
      chengji_class = title_col.index('成绩')
      chengji = title_col.index('绩点成绩')
      xuefen = title_col.index('学分')
      time = title_col.index('考试时间')
      shuxing = title_col.index('课程属性')
      kenum = title_col.index('课序号')
      chongxiubiao = title_col.index('重修补考标志')
      xuewei = title_col.index('TSKCBJ')
    except:
      print('请将全部数据粘贴到txt文件中使用,至少包含学号，姓名，教学班级，成绩，绩点成绩，学分，课程属性，课程号，考试时间，重修补考标志和一二学位标志。\n')
      os.system('pause')
      exit()
    oup.write(title)
    lines = inp.readlines()
    line_num = 1
    total_line = []
    xuehao_kecheng = []
    chongxiu = {}
    for j in lines:
      i = j.rstrip().split('\t')

      xuehao_kecheng.append(i[num]+i[kenum])
      '''
      if len(i) ==13:
        i.append('1')
        j = j.rstrip()+'\t1\n'
      elif len(i)!=14:
        print('第'+str(line_num)+'数据发生错误，请检查后重新提交\n')
        os.system('pause')
        exit()
      '''
      total_line.append(j)
      #print(str(chongxiubiao))
      if i[chongxiubiao] =='重修':
        if i[num]+i[kenum] in chongxiu.keys():
          ##建立字典，将挂科课程的学号+课程号指向最后一门课程时间
          if int(i[time]) > int(chongxiu[i[num]+i[kenum]]):
            chongxiu[i[num]+i[kenum]]= i[time]
        else:
          chongxiu[i[num]+i[kenum]] = i[time]
    final_line = []
    if TorF == 'F':
      final_line=total_line
    else:
      ##根据学号+课程号去除双学位课程
      for i in total_line:
        j = i.rstrip().split('\t')
        if j[xuewei] == '第一学位课程':
          final_line.append(i)
    #print(final_line)
    final_line2 = []
    if fail =='T':
      final_line2 = final_line
    else:
      number = 0
      for i in final_line:
        j = i.rstrip().split()
        ##只将通过的课程和重修的最后一门课程保留在临时文件中
        if j[num]+j[kenum] not in chongxiu.keys():
          final_line2.append(i)
        elif j[time] == chongxiu[j[num]+j[kenum]]:
          final_line2.append(i)
    for j in final_line2:    
      oup.write(j)
        
        
def mainproc(shuchu_name):
  ##读取经过清洗的临时文件，计算学分绩
  with open('__temp.txt','r')as inp,open(shuchu_name,'a') as summary:
    title = inp.readline()

    title_col = title.rstrip().split()

    num = title_col.index('学号')
    name = title_col.index('姓名')
    classname = title_col.index('教学班级')
    chengji_class = title_col.index('成绩')
    chengji = title_col.index('绩点成绩')
    kename = title_col.index('课程名')
    xuefen = title_col.index('学分')
    shuxing = title_col.index('课程属性')
    chongxiu = title_col.index('重修补考标志')
    xuewei = title_col.index('TSKCBJ')

    chengji_total = inp.readlines()

    num_n = []
    name_n = []
    classname_n = []
    bixiu_num = []
    bixiu_total = []
    xianxuan_num = []
    xianxuan_total = []
    renxuan_num = []
    renxuan_total = []
    xuefen_total=[]
    xiuxian_aver = []
    all_aver = []
    xuefen_total=[]
    xiuxian_aver = []
    all_aver = []
    all_add = []

    j = 0
    for i in chengji_total:
      i = i.rstrip().split('\t')
      if i[num] not in num_n:
        num_n.append(i[num])
        name_n.append(i[name])
        classname_n.append(i[classname])
        bixiu_num.append(0)
        bixiu_total.append(0)
        xianxuan_num.append(0)
        xianxuan_total.append(0)
        renxuan_num.append(0)
        renxuan_total.append(0)
        xuefen_total.append(0)
        j = j +1
        print(str(j)+name_n[j-1])
      poc = num_n.index(i[num])
      if '体疗' in i[kename]:
        xuefen_total[poc] = xuefen_total[poc]+1
        renxuan_num[poc] = renxuan_num[poc]+1
        renxuan_total[poc] = renxuan_total[poc]+0.8
        print('含有体疗课程')
        continue        
      if i[shuxing] == '必修':
        if i[chengji_class] not in['F','W','I']:
          xuefen_total[poc] = xuefen_total[poc]+int(i[xuefen])
        bixiu_num[poc] = calCredits(i[xuefen],i[chengji],bixiu_num[poc],i[chengji_class],i[chongxiu])
        bixiu_total[poc] = calGPA(i[xuefen],i[chengji],bixiu_total[poc],i[chengji_class],i[chongxiu])
      elif i[shuxing] == '限选':
        if i[chengji_class] not in['F','W','I']:
          xuefen_total[poc] = xuefen_total[poc]+int(i[xuefen])
        xianxuan_num[poc] = calCredits(i[xuefen],i[chengji],xianxuan_num[poc],i[chengji_class],i[chongxiu])
        xianxuan_total[poc] = calGPA(i[xuefen],i[chengji],xianxuan_total[poc],i[chengji_class],i[chongxiu])
      else:
        if i[chengji_class] not in['F','W','I']:
          xuefen_total[poc] = xuefen_total[poc]+int(i[xuefen])
        renxuan_num[poc] = calCredits(i[xuefen],i[chengji],renxuan_num[poc],i[chengji_class],i[chongxiu])
        renxuan_total[poc] = calGPA(i[xuefen],i[chengji],renxuan_total[poc],i[chengji_class],i[chongxiu])

    print("总统计人数为："+str(j)+"\n")

    summary.write('学号\t姓名\t教学班级\t总完成学分\t必修限选平均学分绩\t必修限选平均学分绩排名\t所有课程平均学分绩\t所有成绩平均学分绩排名\t总学分绩\t总学分绩排名\t非PF学分\n')
    for g in range(0,j):
      if bixiu_num[g]+xianxuan_num[g]==0:
        xiuxian_aver.append(0)
      else:
        xiuxian_aver.append((bixiu_total[g]+xianxuan_total[g])/(bixiu_num[g]+xianxuan_num[g]))
      if bixiu_num[g]+xianxuan_num[g]+renxuan_num[g]==0:
        all_aver.append(0)
      else:
        all_aver.append((bixiu_total[g]+xianxuan_total[g]+renxuan_total[g])/(bixiu_num[g]+xianxuan_num[g]+renxuan_num[g]))
      all_add.append(bixiu_total[g]+xianxuan_total[g]+renxuan_total[g])
    for g in range(0,j):
      summary.write(str(num_n[g])+"\t"+str(name_n[g])+"\t"+str(classname_n[g])+"\t"+str(xuefen_total[g])+"\t"+str(round(xiuxian_aver[g],3))+'\t' \
                    +str(sorted(xiuxian_aver,reverse = True).index(xiuxian_aver[g])+1)+'\t'+str(round(all_aver[g],3))+'\t'+str(sorted(all_aver,reverse = True).index(all_aver[g])+1)+'\t' \
                    +str(round(all_add[g],3))+'\t'+str(sorted(all_add,reverse = True).index(all_add[g])+1)+'\t'+str(bixiu_num[g]+xianxuan_num[g]+renxuan_num[g])+'\n')
  os.remove('__temp.txt') 

print("亲爱的用户，欢迎您试用“李导帮你算成绩”程序2.1版本\n感谢您对本程序的支持\n如有程序运行错误，欢迎微信联系作者李天奇：litq_94\n一键生成成绩排名-尽享假期生活\n\n")
wenjian_name = input("请输入你要进行成绩排序的文件（需要同时输入文件后缀），回车键结束\n")
shuchu_name = input("请输入你想要写入的文件名称（为方便打开，建议您同时输入文件后缀），回车键结束\n")
preproc(wenjian_name)
mainproc(shuchu_name)



print("排名计算已结束，可以在文件中进行查看。\n 欢迎您下次使用。如果进一步需求，欢迎微信联系原作者李天奇：litq_94")
os.system('pause')
