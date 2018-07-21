import hashlib
import hmac

key = "8oe0i89o7es243t5s234"			# bytes literal conversion necessary
message = 'Body text for the hash.'	# hmac does not digest Unicode characters

key_as_bytes = key.encode()
print(type(key_as_bytes)) # ensure it is byte representation
key_decoded = key_as_bytes.decode()
print(type(key_decoded)) # ensure it is string representation


print(key, message)

print(hashlib.algorithms_available)		# all algorithms list

# Generate the hash.
signature = hmac.new(
	key.encode(),
	message.encode(),
	hashlib.sha1
).hexdigest()

print(len(signature))
print(signature)