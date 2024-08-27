##ENCODER AND DECODER

#OUTPUT ENCODING

import base64                           #Encoding is used for. write some sentence,num or any extra chars
message ="i love you"
message_in_bytes=bytes(message,"utf-8")
encode_message = base64.b64encode(message_in_bytes)
print(f"Encode: {encode_message}")

#INPUT DECODNG
message =input("input>>    ")
message_in_bytes=bytes(message,"utf-8")
decode_message = base64.b64decode(message_in_bytes)
print(f"Decode:{decode_message}")