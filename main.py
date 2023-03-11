import get_data
import draw

luogu_id = 670766 #luogu_id

datas = get_data.Get_datas(luogu_id)
draw.show_fig(datas[0] , datas[1])