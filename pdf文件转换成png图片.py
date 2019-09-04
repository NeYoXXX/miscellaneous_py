import fitz
import requests
import os

def pdf_png(pdf_url, img_path):
    '''
    pdf文件转换成png图片
    :param pdf_url:pdf地址
    :param img_path:保存png文件路径
    :return:
    '''
    pdf_name = pdf_url.split('/')[-1]
    img_path_pdf = img_path + pdf_name
    #判断文件是否存在，若存在则不需要请求
    if not os.path.exists(img_path_pdf):
        request = requests.get(pdf_url)
        with open(img_path_pdf, 'wb') as f:
            f.write(request.content)

    doc = fitz.open(img_path_pdf)
    for pg in range(doc.pageCount):
        page = doc[pg]
        rotate = int(0)
        # 每个尺寸的缩放系数为2，这将为我们生成分辨率提高四倍的图像。
        zoom_x = 2.0
        zoom_y = 2.0
        trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
        pm = page.getPixmap(matrix=trans, alpha=False)
        pm.writePNG(img_path + '%s.png' % (pdf_name.split('.')[0]+str(pg)))


if __name__ == '__main__':
    pdf_png('http://139.159.200.198/nsdoc/ninstar_financial/business/1010101000000003000/chain_ledger/XET736vJ.pdf','/home/hzx/Desktop/temp/')
