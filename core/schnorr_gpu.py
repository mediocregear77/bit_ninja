# core/schnorr_gpu.py
# High-level interface for GPU-accelerated Schnorr signature verification

import numpy as np
from core.cuda_wrapper import verify_signatures

class SchnorrGPUVerifier:
    def __init__(self):
        self.key_len = 32  # Assuming 256-bit keys/messages/sigs

    def prepare_inputs(self, pubkeys, msgs, sigs):
        assert len(pubkeys) == len(msgs) == len(sigs), "Input length mismatch"

        count = len(pubkeys)
        pubkeys_arr = np.zeros((count, self.key_len), dtype=np.uint8)
        msgs_arr = np.zeros((count, self.key_len), dtype=np.uint8)
        sigs_arr = np.zeros((count, self.key_len), dtype=np.uint8)

        for i in range(count):
            pubkeys_arr[i] = np.frombuffer(pubkeys[i], dtype=np.uint8)
            msgs_arr[i] = np.frombuffer(msgs[i], dtype=np.uint8)
            sigs_arr[i] = np.frombuffer(sigs[i], dtype=np.uint8)

        return pubkeys_arr, msgs_arr, sigs_arr

    def verify_batch(self, pubkeys, msgs, sigs):
        pub_arr, msg_arr, sig_arr = self.prepare_inputs(pubkeys, msgs, sigs)
        results = verify_signatures(pub_arr, msg_arr, sig_arr)
        return results.tolist()
