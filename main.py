import get_data
import draw.draw as draw , os
import draw.circle_corner as cie
from config.config import Read

def startWork():
    config = Read.read_config()
    luogu_id = config["Your_luogu_id"]
    radii = config["png_radii"] # 圆角大小

    print('正在获取数据')
    datas = get_data.Get_datas(luogu_id)
    print('正在生成图标')
    path = draw.show_fig(datas[0] , datas[1])
    cie.work(path , radii)
    os.system(path)

if __name__ == "__main__":
    startWork()