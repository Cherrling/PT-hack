import binascii
import urllib.parse
import requests
import random
import datetime

random_upload = True
random_peer_id = True

def random_key():
    return ''.join(random.sample('0123456789ABCDEF', 8))

def random_peer_id(hash):
    random.seed(int(hash, 16))
    return "-qB4630-" + ''.join(random.sample('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', 12))


def send_request(url):
    response = requests.get(url, headers={"User-Agent": "qBittorrent/4.6.3"})
    print(response.status_code)


def run(tracker_url,info_hash_hex,upload):
    for i in info_hash_hex:
        info_hash_bytes = binascii.unhexlify(i)
        info_hash_urlencoded = urllib.parse.quote(info_hash_bytes)

        send_upload = upload
        
        if random_upload:
            send_upload += int(i, 16) % (1024 * 1024 * 1024 ) # GiB
        print(i)
        print(f"{upload / (1024 * 1024 * 1024):.3f}GiB")

        if random_peer_id:
            peer_id = random_peer_id(i)
        else:
            peer_id = "-qB4630-zts35vNrAlpg"
        
        url=tracker_url + f"&info_hash={info_hash_urlencoded}&peer_id={peer_id}&port=34567&uploaded={send_upload}&downloaded=0&left=0&corrupt=0&key={random_key()}&event=completed&numwant=200&compact=1&no_peer_id=1&supportcrypto=1&redundant=0"
        print(url)
        send_request(url)
    
now = datetime.datetime.now()
date = now.strftime('%Y-%m-%d')
time = now.strftime('%H-%M-%S')
print("=====================================")
print(f"{date} {time}\n")

tracker_url = "https://www.pt1111.xxx/announce.php?passkey=deadbeefdeadbeefdeadbeefdeadbeef"
info_hash_hex = [
    # 示例 hash
    "deadbeefdeadbeefdeadbeefdeadbeefdeadbe",
    "1234567890abcdef1234567890abcdef12345678",
    "abcdef1234567890abcdef1234567890abcdef12",
    "1234567890abcdef1234567890abcdef12345678",
]
run(tracker_url,info_hash_hex,0)


tracker_url = "https://www.pt2222.xxx/announce.php?passkey=deadbeefdeadbeefdeadbeefdeadbeef"
info_hash_hex = [
    # 示例 hash
    "deadbeefdeadbeefdeadbeefdeadbeefdeadbe",
    "1234567890abcdef1234567890abcdef12345678",
    "abcdef1234567890abcdef1234567890abcdef12",
    "1234567890abcdef1234567890abcdef12345678",
]
run(tracker_url,info_hash_hex,0)
