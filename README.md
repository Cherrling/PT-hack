# PT-hack

填入 tracker 链接，passkey 和 种子的 hash 即可，定时十分钟运行一次

对于部分 tracker ，不同种子使用不同 passkey ，需要自己为每个hash配置一次站点链接和 passkey

## 新增 torrent2hash 脚本

批量从种子中提取 hash 信息

将种子放入 `torrents` 文件夹中，运行 `python torrent2hash.py`

hash 信息将保存在 `hash.json` 文件中，填入脚本中即可