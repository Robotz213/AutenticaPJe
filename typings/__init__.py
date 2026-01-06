from typing import Literal

from cryptography.hazmat.primitives.asymmetric.dh import DHPrivateKey
from cryptography.hazmat.primitives.asymmetric.dsa import DSAPrivateKey
from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurvePrivateKey
from cryptography.hazmat.primitives.asymmetric.ed448 import Ed448PrivateKey
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey
from cryptography.hazmat.primitives.asymmetric.x448 import X448PrivateKey
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey

type PrivateKey = (
    DHPrivateKey
    | Ed25519PrivateKey
    | Ed448PrivateKey
    | RSAPrivateKey
    | DSAPrivateKey
    | EllipticCurvePrivateKey
    | X25519PrivateKey
    | X448PrivateKey
)

type Algoritmos = Literal["SHA256withRSA", "SHA1withRSA", "MD5withRSA"]
