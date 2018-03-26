import requests

def get_captcha(filename):
    filename = str(filename)
    r = requests.get('http://210.37.0.22/CheckCode.aspx?', stream=True)

    with open(filename+'.bmp', 'wb') as f:
        for chuck in r.iter_content(chunk_size=1024):
            if chuck:
                f.write(chuck)


if __name__ == '__main__':
    for i in range(1,100):
        get_captcha(i)
