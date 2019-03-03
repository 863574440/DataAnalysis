from njupt import Zhengfang

lingmacker = Zhengfang("B17041529", "186hjs")
score = lingmacker.list_exam_scores()

for i in score:
    li = []
    if i["学年"] == "2018-2019":
        li.append("课程名称：" + str(i.get("课程名称")))
        li.append("学分：" + str(i.get("学分")))
        li.append("成绩：" + str(i.get("成绩")))
        li.append("绩点：" + str(i.get("绩点")))

        print("%-40s%-9s%-9s%-9s" % tuple(li))
