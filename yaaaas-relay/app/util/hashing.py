import hashlib


def derive_address_from_pubkey(pubkey: str):
    s = hashlib.sha3_256()
    s.update(pubkey)
    return s.digest()
