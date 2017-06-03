#
#
#
import hashlib
import base64
m = hashlib.sha256()

# initial input fields
data = 'Data'
nonce = 0;
# first attempt to create a hash with leading zeros
m.update(data + str(nonce))
hash = base64.b64encode(m.digest());
print(hash);
# subsequent attempts to create a hash with three leading zeros
while not(hash.startswith('000')):
    nonce+=1;
    m.update(data + str(nonce));
    hash = base64.b64encode(m.digest());
print(hash)
print(str(nonce))





