import easygui as g
import os.path

file = g.fileopenbox()
file_name = os.path.basename(file)
f = open(file)
F = list(f)
g.textbox('文件【%s】的内容如下：'%file_name,'显示文件内容',text = F)
answer = g.choicebox('检测到文件内容发生改变，请选择以下操作：','警告',choices = ['覆盖保存','放弃保存','另存为...'])

if answer == '覆盖保存':
    f.close()
elif answer == '另存为...':
    path = g.filesavebox(default = file)
    F_2 = open(path, 'w')
    F_2.writelines(F)
    F_2.close()
    
