import hashlib
import os
import time

# ---------------------------------------------------
# How does bitcoins mining work? - Simplified example
# ---------------------------------------------------
block_transaction = b"User1;User2;10BTC"

# Decorator used to caculate the run time of a function
def timer(func):
    t1 = time.clock()
    func()
    t2 = time.clock()
    dif_1 = t2-t1
    print("La fonction {} met {} secondes pour s'exécuter".format(func.__name__, dif_1))

@timer
def mining():
    global nonces_valid
    # A nonces is a unique number to solve the mathematical problem
    nonces = 0
    for i in range(200000):
        nonces += 1
        nonces_bytes = bytes(nonces)
        # Use of the hash function SHA 256
        proof_of_work = hashlib.sha256(block_transaction + nonces_bytes).hexdigest()
        # The mathematical problem to solve
        if proof_of_work[0:3]=="000":
            print(proof_of_work)
            print(nonces)
            print("Congratulations! You have won a bitcoin!")
            nonces_valid = nonces
            break

@timer
def check_valid():
    nonces_bytes = bytes(nonces_valid)
    proof_of_work = hashlib.sha256(block_transaction + nonces_bytes).hexdigest()
    if proof_of_work[0:3]=="000":
        print("La transaction est valide")
