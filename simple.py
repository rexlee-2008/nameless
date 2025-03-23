'''
import os
keys = [os.urandom(16) for _ in range(10)]
print(keys)
'''

def xor(x, y):
    return bytes([a ^ b for a, b in zip(x, y)])

def reverse_e(c, keys):
    left = c[:8]
    right = c[8:]
    # 키를 역순으로 사용하여 XOR 연산을 수행
    for key in reversed(keys):
        key_left = key[:8]
        key_right = key[8:]
        
        # XOR 연산을 역으로 수행
        right = xor(key_left, right)
        left = xor(left, key_right)
    
    return left + right

# 주어진 10개의 키
keys = [
    b';1\x12\xbc{Y\x15[\xe4G\xc7\xe6\x02\xd2J\xbd',
    b'\xa4\xcd\x8fI\x97a\x0c\xa9\xa5\x1c\xb8|N\x9f\xe4\xbe',
    b'\n\x88\xe5h\x8b\xbe6\xa22\xe3\x8d`\xa2\xf7\x9b\xa3',
    b'\x15k\xfe\x8e\x08\xb68\x84}\xdf\xa7\xa38C\x13\xfb',
    b'\xa3\x8c\xcf\x04\xe5s\x1d\xc4?\x15\xb9+X\xf0\xce(',
    b'\xe0\x91\xa1\xde+\x9fO%-\x10\xc4I\x1a\x98\xea\xcc',
    b'\x83\x94\x1b\xd9Q!RGTy\x0fPk\x89\xf8\xfe',
    b'\x8c\xa1\xed\x91h\xcav\xb0:\xd2\xac h\x162\xec',
    b'\xc1L\xe6\xffd&\xd0#N\xcf&\x94\x97\xe0\xd9O',
    b'U\x7fO\x8eD\xf7]\x95\xd4\x7f\xa3\xd1\xe3\xea\xd7"',
]
# 목표 메시지
target = b"give me the flag"

# 역 암호화를 통해 메시지를 찾음
found_message = reverse_e(target, keys)

print(f"Found message: {found_message.hex()}")
print(f"Found message (decoded): {found_message.decode(errors='ignore')}")


def e(x, keys):
    left = x[:8]
    right = x[8:]
    for key in keys:
        key_left = key[:8]
        key_right = key[8:]
        
        left, right = xor(key_left, right), xor(left, key_right)
    
    return left + right

# 복원된 메시지를 바탕으로 암호화
encrypted_message = e(found_message, keys)

print(f"Encrypted found message: {encrypted_message.hex()}")
print(f"Target message: {target.hex()}")

# 비교
if encrypted_message == target:
    print("Success! The found message encrypts to the target message.")
else:
    print("The found message does not match the target message.")

def find_flag(found_message, target_message, keys):
    # 목표 메시지를 바이트로 변환
    target_bytes = target_message.encode('utf-8') if isinstance(target_message, str) else target_message
    flag_length = len(target_bytes)
    
    # found_message와 target_bytes 길이가 같은지 확인
    if len(found_message) == flag_length:
        # 바이트를 하나씩 변경하여 target_bytes와 비교
        for i in range(flag_length):
            for j in range(256):  # 가능한 모든 바이트 값 시도
                modified_message = bytearray(found_message)
                modified_message[i] = j  # 특정 위치의 바이트 변경

                # 수정된 메시지로 암호화
                encrypted = e(bytes(modified_message), keys)

                # 암호화된 메시지가 목표 메시지와 일치하는지 확인
                if encrypted == target_bytes:
                    print(f"Found valid message: {modified_message.hex()}")
                    return modified_message  # 수정된 메시지 반환
    else:
        print("The found message length does not match the target message length.")
        return None

# 호출 예시
found_message = bytes.fromhex("8f10786bc369a3e02c6cd2d0de8a8d13")
target_message = "give me the flag"

result = find_flag(found_message, target_message, keys)
if result:
    print(f"Flag found: {result.decode('utf-8', errors='ignore')}")