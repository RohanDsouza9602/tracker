import hashlib

class Utils():
    
    @staticmethod  
    def md5_hash(input_string):
        md5_hash_object = hashlib.md5()
        md5_hash_object.update(input_string.encode("utf-8"))
        hash_result = md5_hash_object.hexdigest()
        return hash_result