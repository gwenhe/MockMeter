if 1 == 0:
    from app.schemas.mock import RequestSchema, ResponseSchema
    from app.core.exception import JSONResponseMock

    request: RequestSchema = None
    response: ResponseSchema = None

import requests

json_dict = request.json_dict
comm = json_dict['comm']
data = json_dict['data']

prcscd = comm.get('prcscd')
order_no = data.get('ORDERNO')
idno = data.get('IDNO')
name = data.get('NAME')

url = 'http://127.0.0.1:8000/mock/http/1' + '/jc/' + prcscd
res_dict = requests.post(url=url, json=request.json_dict).json()
if order_no:
    res_dict['data']['ORDERNO'] = order_no

raise JSONResponseMock(content=res_dict)
