import binascii
import urllib.parse
import requests
import random
import datetime
from tqdm import tqdm

random_upload = False
random_id = True


def random_key():
    return ''.join(random.sample('0123456789ABCDEF', 8))

def random_peer_id(hash):
    random.seed(int(hash, 16))
    return "-qB4630-" + ''.join(random.sample('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', 12))

def send_request(url):
    response = requests.get(url, headers={"User-Agent": "qBittorrent/4.6.3"})
    return response.status_code

def run(tracker_url,info_hash_hex,upload):
    for i in tqdm(info_hash_hex, desc="Processing info hashes"):
        info_hash_bytes = binascii.unhexlify(i)
        info_hash_urlencoded = urllib.parse.quote(info_hash_bytes)

        send_upload = upload
        
        if random_upload:
            send_upload += int(i, 16) % (1024 * 1024 * 1024 ) # GiB

        if random_id:
            peer_id = random_peer_id(i)
        else:
            peer_id = "-qB4630-zts35vNrAlpg"
        
        url=tracker_url + f"&info_hash={info_hash_urlencoded}&peer_id={peer_id}&port=34567&uploaded={send_upload}&downloaded=0&left=0&corrupt=0&key={random_key()}&event=completed&numwant=200&compact=1&no_peer_id=1&supportcrypto=1&redundant=0"
        code = send_request(url)
        tqdm.write(f"Hash: {i}  res.code: {code} upload: {upload / (1024 * 1024 * 1024):.3f}GiB")
    
now = datetime.datetime.now()
date = now.strftime('%Y-%m-%d')
time = now.strftime('%H-%M-%S')
print("=====================================")
print(f"{date} {time}\n")

tracker_url = "https://www.pt1111.xxx/announce.php?passkey=deadbeefdeadbeefdeadbeefdeadbeef"
info_hash_hex = [
    # 示例 hash
    "deadbeefdeadbeefdeadbeefdeadbeefdeadbeef",
    "1234567890abcdef1234567890abcdef12345678",
    "abcdef1234567890abcdef1234567890abcdef12",
    "1234567890abcdef1234567890abcdef12345678",
]
run(tracker_url,info_hash_hex,0)


tracker_url = "https://www.pt2222.xxx/announce.php?passkey=deadbeefdeadbeefdeadbeefdeadbeef"
info_hash_hex = [
    # 示例 hash
    "deadbeefdeadbeefdeadbeefdeadbeefdeadbeef",
    "1234567890abcdef1234567890abcdef12345678",
    "abcdef1234567890abcdef1234567890abcdef12",
    "1234567890abcdef1234567890abcdef12345678",
]
run(tracker_url,info_hash_hex,0)
