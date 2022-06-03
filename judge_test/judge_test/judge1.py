import os

from django.shortcuts import render

from django.http import HttpResponse, FileResponse


import xlwt
import datetime


def get_txt_data(file_name):
    with open(file_name, "r") as f:
        data = f.read()
        data = data.split("----------")
        data = [d for d in data if d]
    return data


def edit_info(data):
    result = [["unicode", "character", "hint-top", "hint-bottom", "hint-left", "hint-right"]]
    for d in data:
        # '\n両 / 4E21:\n⬆︎@769.0 / ⬇︎@-81.0\n⬅︎@107.0 / ⮕@896.0\n'
        d = d.replace("\n", "")
        d = d.split(":")
        word, unicode_value = d[0].split("/")
        word = word.strip()
        unicode_value = "uni" + unicode_value.strip()
        delete_char = ["⬆︎@", "⬇︎@", "⮕@"]
        for char in delete_char:
            d[1] = d[1].replace(char, "")
        d[1] = d[1].replace("⬅︎@", " / ")
        d[1] = d[1].split(" / ")
        temp = [word, unicode_value]
        temp.extend(d[1])
        print(temp)
        result.append(temp)

    return result


def write_rows(datas, response):
    nowt = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('sheet1')
    row = 0
    for data_in_row in datas:
        row += 1
        for index, data in enumerate(data_in_row):
            worksheet.write(row, index, data)
    workbook.save(response)


def upload_file(request):
    # 请求方法为POST时,进行处理;
    if request.method == "POST":
        # 获取上传的文件,如果没有文件,则默认为None;
        File = request.FILES.get("myfile", None)
        if File is None:
            return HttpResponse("no files for upload!")
        else:
            nowt = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            file_name = f"{nowt}.txt"
            # 打开特定的文件进行二进制的写操作;
            with open(file_name, 'wb') as f:
                # 分块写入文件;
                f.write(File.read())
            data = get_txt_data(file_name)
            os.remove(file_name)
            data = edit_info(data)
            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename=%s' % ("wordData%s.xls" % nowt)
            write_rows(data, response)
            return response
    else:
        return render(request, 'judge1.html')