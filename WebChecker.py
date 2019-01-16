#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests
import argparse


def check(domain, resource):
    url = (domain + "/" + resource) if domain[-1] != "/" else (domain + resource)
    
    r = requests.get(url)

    if r.status_code == requests.codes.ok:
        print("[+] " + resource  + " is found")
        return True
    elif r.status_code != 404:
        print("[?] " + resource  + " may exist (" + str(r.status_code)+ ")")
    else:
        print("[-] " + resource  + " not found")

    return False

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='The Checker for Web')
    parser.add_argument('--domain', type=str,
            default='http://127.0.0.1/', dest='domain',
            help='the domain you insterested in')

    domain = parser.parse_args().domain


    # robots.txt
    if check(domain, "robots.txt"):
        url = (domain + "/robots.txt") if domain[-1] != "/" else (domain + "robots.txt")
        r = requests.get(url)
        print(r.text)
    # static/ js/ css/ img/
    check(domain, "static/")
    check(domain, "js/")
    check(domain, "css/")
    check(domain, "img/")

    # upload/ uploads/ 
    check(domain, "upload/")
    check(domain, "uploads/")
    # file/ files/
    check(domain, "file/")
    check(domain, "files/")
    # tmp/ temp/
    check(domain, "tmp/")
    check(domain, "temp/")

    # phpinfo.php
    check(domain, "phpinfo.php")
    # WEB-INF/
    check(domain, "WEB-INF/")

    # .DS_Store
    check(domain, ".DS_Store")
    # .git/
    # check(domain, ".git")
    check(domain, ".git/HEAD")
    # .hg/
    check(domain, ".hg/")
    # .svn/
    check(domain, ".svn/")
    # ../
    check(domain, "../")

    # login/ login.php
    check(domain, "login/")
    check(domain, "login.php")

    # admin/ admin.php
    check(domain, "admin/")
    check(domain, "admin.php")
    # admin-console/
    check(domain, "admin-console/")
    # web-console/
    check(domain, "web-console/")
    # phpMyAdmin/ phpmyadmin/ pma/
    check(domain, "phpMyAdmin/")
    check(domain, "phpmyadmin/")
    check(domain, "pma")

