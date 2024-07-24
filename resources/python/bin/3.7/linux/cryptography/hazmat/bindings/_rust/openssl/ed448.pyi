# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.

from cryptography.hazmat.primitives.asymmetric import ed448

class Ed448PrivateKey: ...
class Ed448PublicKey: ...

def generate_key() -> ed448.Ed448PrivateKey: ...
def from_private_bytes(data: bytes) -> ed448.Ed448PrivateKey: ...
def from_public_bytes(data: bytes) -> ed448.Ed448PublicKey: ...
