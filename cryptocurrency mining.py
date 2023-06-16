from hashlib import sha256
import time

MAX_NONCE = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()  # Fixed typo: changed 'hexidigest()' to 'hexdigest()'

def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0' * prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"YAY! Successfully mined BITCOINS with nonce value: {nonce}")
            return new_hash
    
    raise BaseException(f"Couldn't find correct hash after trying {MAX_NONCE} nonces.")

if __name__ == '__main__':
    transactions = '''
    Dav->Nira->20,
    davis->niranjan->45
    '''
    difficulty = 7  # Reduced difficulty for faster demonstration
    
    start = time.time()

    print("Start mining")
    try:
        new_hash = mine("Block #19", transactions, '0x5395a3c42a585356147b1f2e01b206957f1d4bd2069fa2a44cb8691f96c963fb', difficulty)
        total_time = str((time.time() - start))
        print(f"End mining. Mining took: {total_time} seconds")
        print(new_hash)
    except BaseException as e:
        print(str(e))
