import requests

def main():
    post_data = {'name': 'Testimies', 'password': 'asdasd'}
    r = requests.post("http://127.0.0.1:5000/register", json = post_data)
    print(r.status_code)
    print(r.text)

if __name__ == '__main__':
    main()
