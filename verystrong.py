'''
from Crypto.Cipher import AES
from hashlib import sha256
import os

# 암호화된 플래그 (이 값은 실제 코드 실행에서 얻어야 합니다)
encrypted_flag = bytes.fromhex("292b47e88e0863b1b48ddaeb974b192399afd8c835403cb429882bb3e5bf3083d83c7e35")

# 예시로 입력할 값들 (사용자가 제공해야 함)
mask = "0x0000000000000000"  # 비트 마스크
message = "67697665206d652074686520666c6167"  # 원하는 메시지의 헥스 표현

# 메시지를 AES로 암호화하는 함수
def encrypt_message(key, nonce, message):
    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
    return cipher.encrypt(bytes.fromhex(message))

# 키와 nonce를 랜덤으로 생성하는 대신 이 값들을 재사용합니다.
key = os.urandom(16)  # 실제 코드에서 사용된 키
suuuuper_secure_seed_of_nonce = 12345678901234567890  # 예시의 nonce seed

# 원래 nonce 계산
nonce = sha256(str(suuuuper_secure_seed_of_nonce).encode()).digest()[:12]

# 입력한 mask에 따라 nonce2를 계산
mask_int = int(mask, 16)
nonce2 = sha256(str(suuuuper_secure_seed_of_nonce & mask_int).encode()).digest()[:12]

# 입력한 메시지 암호화
encrypted_message = encrypt_message(key, nonce2, message)

# 원래 플래그 복구
recovered_flag = bytes(a ^ b for a, b in zip(encrypted_flag, encrypted_message))

# 플래그 출력
print("Recovered flag:", recovered_flag.decode('utf-8', errors='ignore'))

# 복구된 플래그가 특정 포맷인지 확인하는 함수
def is_flag_format(possible_flag):
    return possible_flag.startswith("flag{") and possible_flag.endswith("}")

# 예시의 복구된 플래그
possible_flag = "vp34A'8s"

# 플래그 형식 확인
if is_flag_format(possible_flag):
    print("Valid flag found:", possible_flag)
else:
    print("Not a valid flag. Further attempts needed.")
'''
import os
from Crypto.Cipher import AES
from hashlib import sha256

# 이미 알고 있는 값들
key = os.urandom(16)  # 이 키는 본인의 키로 바꿔야 합니다
suuuuper_secure_seed_of_nonce = int.from_bytes(os.urandom(16), 'big')
nonce = sha256(str(suuuuper_secure_seed_of_nonce).encode()).digest()[:12]

# 암호화된 플래그와 메시지를 입력받는 부분
encrypted_flag = bytes.fromhex('YOUR_ENCRYPTED_FLAG_HERE')  # 암호화된 플래그 값
encrypted_message = bytes.fromhex('YOUR_ENCRYPTED_MESSAGE_HERE')  # 암호화된 메시지 값

# 플래그 찾기 자동화
def find_flag(encrypted_flag, encrypted_message):
    for mask in range(0, 2**64):  # 마스크 값을 조정
        nonce2 = sha256(str(suuuuper_secure_seed_of_nonce & mask).encode()).digest()[:12]
        
        # 암호화된 메시지를 복호화
        cipher = AES.new(key, AES.MODE_CTR, nonce=nonce2)
        decrypted_message = cipher.decrypt(encrypted_message)

        # 암호화된 플래그를 복호화
        flag_candidate = xor(decrypted_message, encrypted_flag)

        # 플래그 포맷 확인
        if is_flag_format(flag_candidate):
            print(f"Possible flag found: {flag_candidate}")
            return flag_candidate

    print("No valid flag found.")
    return None

def xor(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])

def is_flag_format(possible_flag):
    return possible_flag.startswith(b"flag{") and possible_flag.endswith(b"}")

# 플래그 찾기 실행
find_flag(encrypted_flag, encrypted_message)