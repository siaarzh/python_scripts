import requests
import re

def retrieve_file_object(url):
    '''
    Retrieves attached file names from URL and returns a GET request result

    :param url: URL source of presumed downloadable content
    :return:    tuple (result, filename)
        WHERE
        requests.models.Response result
        str filename is the name of the attachment with extension
    '''
    result = requests.get(url, verify=False, stream=True)
    try:
        cont_disp = urllib.parse.unquote(result.headers["content-disposition"])
        if re.search("UTF-8''(.*);", cont_disp) != None:
            filename = re.findall("UTF-8''(.*);", cont_disp)[0]
        else:
            filename = re.findall('filename="(.+)"', cont_disp)[0]
    except:
        filename = None

    return result, filename
	

#====================================================
# TEST HERE:

url = "http://kgd.gov.kz/mobile_api/services/taxpayers_unreliable_exportexcel"
url2 = url + "/PSEUDO_COMPANY/KZ_ALL/fileName/list_PSEUDO_COMPANY_KZ_ALL.xlsx"
url_root = "http://stat.gov.kz"

sub_urls = ["/getImg?id=ESTAT116572",  # Общий классификатор видов экономической деятельности
            "/getImg?id=ESTAT116569",  # Классификатор продукции по видам экономической деятельности
            "/getImg?id=ESTAT245918",  # Классификатор административно-территориальных объектов
            "/getImg?id=ESTAT181313",  # Номенклатура видов экономической деятельности
            "/getImg?id=WC16200004875",  # Кодификатор улиц Республики Казахстан
            "/getImg?id=ESTAT093569"]

urls = [url_root + x for x in sub_urls]
urls.append(url2)

def list_urls():
    link = "http://stat.gov.kz/faces/publicationsPage/publicationsOper/homeNumbersBusinessRegisters/homeNumbersBusinessRegistersReestr"
    html = requests.get(link).text
    soup = BeautifulSoup(html, 'lxml')
    urls = soup.find("div", attrs={"id": "pt1:r1:0:j_id__ctru0pc3:pgl4"}).find_all("a", href=re.compile("ESTAT"))
    urls = [url.get('href') for url in urls]
    return urls

urls2 = [url_root + x for x in list_urls()]
urls = urls+urls2

urls.append("http://djangobook.com/the-django-book/")

print(type('As'))

for url in urls:
    result, fname = get_file_object(url)
    print(type(result))
    try:
        print(urllib.parse.unquote(result.headers["content-disposition"]))
    except:
        print('No attachment')
    print(fname)