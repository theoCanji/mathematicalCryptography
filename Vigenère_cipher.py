lookup_letters = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9,
"k": 10, "l": 11, "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18,
"t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25}

lookup_nums = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i', 9:'j',
10:'k', 11:'l', 12:'m', 13:'n', 14:'o', 15:'p', 16:'q', 17:'r', 18:'s', 19:'t',
20:'u', 21:'v', 22:'w', 23:'x', 24:'y', 25:'z'}

def encrypt(message: str, key:str) -> str:
    encryption = ""
    for i in range(len(message)): 
        key_char = key[i%len(key)] #find correct char in the key

        key_value = lookup_letters[key_char] #look up its corresponding number 

        message_value = lookup_letters[message[i]] #find the message's corresponding number

        shift_by = key_value + message_value #add the two
        
        shifted_char = lookup_nums[shift_by%26] #look up the shifted value in dictionary
        
        new_string = encryption + shifted_char #append to the string
        encryption = new_string
    return encryption


def decrypt(message: str, key:str) -> str:
    message = message.lower()
    encryption = ""
    for i in range(len(message)): 
        key_char = key[i%len(key)] #find correct char in the key

        key_value = lookup_letters[key_char] #look up its corresponding number 

        message_value = lookup_letters[message[i]] #find the message's corresponding number

        shift_by = message_value - key_value #add the two
        
        shifted_char = lookup_nums[shift_by%26] #look up the shifted value in dictionary
        
        new_string = encryption + shifted_char #append to the string
        encryption = new_string
    return encryption

print(ord("a")) #output: 
print(ord("z"))

print(encrypt("hellotowhomeverisdecryptingthisihopethatitdoesnotproveverydifficultandthatyourmethodendsupworkingiamnotsureifthismessageislongenoughbutithinkthatitprobablyisgoodnow", "hi")) #output: "vjjxqjvjqjvjqjvjqj"
print(decrypt("omstvbveowtmcmyqzllkygwbpvnboqzqowwmaphbpbkwlauwaxywcmcmygkqmnpkbtaiulaphbfwbztmapvllvkabxdwyspvnqhuuwaabzlqmboqzulazinmpaswuolvvcnpicaqappvrboiaqaxywiiitfqzovwkvve", "hi"))