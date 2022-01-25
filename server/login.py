import requests

def main():
    post_data = {'name': 'Testimies', 'password': 'asdasd'}
    r = requests.post("http://127.0.0.1:5000/login", json = post_data)
    print(r.status_code)

    if(r.status_code == 400):
        print(r.text)


    data = r.json()

    apikey = data['apikey']
    print(apikey)

    headers = {
        "apikey": apikey
    }

    r = requests.delete("http://127.0.0.1:5000/todo/3", headers = headers)
    print(r.status_code)
    print(r.text)

    post_data = {'todo': "tämä on uusi tehtävä apin ksssautta"}
    r = requests.post("http://127.0.0.1:5000/todos", json=post_data, headers = headers)
    print(r.status_code)
    print(r.text)

    r = requests.delete("http://127.0.0.1:5000/login", headers=headers)
    print(r.status_code)
    print(r.text)
if __name__ == '__main__':
    main()
