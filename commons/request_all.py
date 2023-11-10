import requests

# 统一请求方式

class RequestAll:

    sess = requests.Session()

    def all_request(self, method, url, data, **kwargs):

        method = str(method).lower()
        res = None

        if method == 'get':
            res = RequestAll.sess.request(method=method, url=url, params=data, **kwargs)

        elif method == 'post':
            res = RequestAll.sess.request(method=method, url=url, data=data, **kwargs)

        else:
            print("请求方式不支持")

        print(res.text)
        return res


