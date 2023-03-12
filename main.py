import get_data
import draw , os
import circle_corner as cie

# luogu_id = '000001' #luogu_id 670766
luogu_id = '670766'
radii = 30 # 圆角大小

print('正在获取数据')
datas = get_data.Get_datas(luogu_id)
print('正在生成图标')
path = draw.show_fig(datas[0] , datas[1])
cie.work(path , radii)
os.system(path)