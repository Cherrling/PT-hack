import os
import json
import hashlib
import bencode

def get_torrent_hash(torrent_file):

    data = open(torrent_file, 'rb').read()
    metadata = bencode.bdecode(data)
    info_bts = bencode.bencode(metadata['info'])
    info_hash = hashlib.sha1(info_bts).hexdigest()
    return info_hash

def main(seed_dir, output_file):
    seed_dir = os.path.abspath(seed_dir)
    torrent_files = []
    
    for root, _, files in os.walk(seed_dir):
        for file in files:
            if file.lower().endswith('.torrent'):
                full_path = os.path.join(root, file)
                relative_path = os.path.relpath(full_path, start=seed_dir)
                torrent_files.append((full_path, relative_path))
                
    print(f"Found {len(torrent_files)} torrent files in {seed_dir}")
    result = []
    
    for full_path, relative_path in torrent_files:
        file_hash = get_torrent_hash(full_path)
        if file_hash is not None:
            result.append(file_hash)
        else:
            print(f"Warning: Could not get hash for {relative_path}")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=4, ensure_ascii=False)
    
    print(f"Successfully exported {len(result)} hashes to {output_file}")

if __name__ == '__main__':

    main('torrents/','hash.json')