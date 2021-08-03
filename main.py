import requests
import os

addresses = ['192.168.1.102', '192.168.1.202']  # local ip addresses. Could be a single one, could be numerous.
domains = ['ya.ru', 'mail.ru', 'news.ru']  # list of desired domains
token = os.environ.get('PI_API')  # your pi-hole API token


def block(pi_list, pis, domain_list):
    for pi in pis:
        for item in domain_list:
            response = requests.get("http://" + str(pi) + "/admin/api.php?list=" + pi_list +
                                    "&add=" + item + "&auth=" + token)
            print(response.text)
    return


def unblock(pi_list, pis, domain_list):
    for pi in pis:
        for item in domain_list:
            response = requests.get("http://" + str(pi) + "/admin/api.php?list=" + pi_list +
                                    "&sub=" + item + "&auth=" + token)
            print(response.text)
    return


print(block('black', addresses, domains))
print(unblock('black', addresses, domains))
