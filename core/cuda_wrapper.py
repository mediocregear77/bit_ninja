# core/cuda_wrapper.py
# PyCUDA interface to compiled cuda_kernel.cu

import pycuda.autoinit
import pycuda.driver as cuda
from pycuda.compiler import SourceModule
import numpy as np
import os

# Load CUDA kernel source
KERNEL_PATH = os.path.join(os.path.dirname(__file__), "cuda_kernel.cu")

with open(KERNEL_PATH, "r") as f:
    kernel_code = f.read()

mod = SourceModule(kernel_code, no_extern_c=True)

# Bind kernels
verify_kernel = mod.get_function("schnorr_batch_verify")
entropy_kernel = mod.get_function("entropy_score_kernel")
hash_kernel = mod.get_function("hash_kernel")

# GPU wrapper functions
def verify_signatures(pubkeys, msgs, sigs):
    count = len(pubkeys)
    assert count == len(msgs) == len(sigs)

    pubkeys_gpu = cuda.mem_alloc(pubkeys.nbytes)
    msgs_gpu = cuda.mem_alloc(msgs.nbytes)
    sigs_gpu = cuda.mem_alloc(sigs.nbytes)
    results_gpu = cuda.mem_alloc(count)

    cuda.memcpy_htod(pubkeys_gpu, pubkeys)
    cuda.memcpy_htod(msgs_gpu, msgs)
    cuda.memcpy_htod(sigs_gpu, sigs)

    verify_kernel(pubkeys_gpu, msgs_gpu, sigs_gpu, results_gpu, np.int32(count),
                  block=(256, 1, 1), grid=(int((count + 255) / 256), 1))

    results = np.empty(count, dtype=np.bool_)
    cuda.memcpy_dtoh(results, results_gpu)

    return results

def score_entropy(seed, count):
    output = np.zeros(count, dtype=np.float32)
    entropy_gpu = cuda.mem_alloc(output.nbytes)

    entropy_kernel(entropy_gpu, np.uint64(seed), np.int32(count),
                   block=(256, 1, 1), grid=(int((count + 255) / 256), 1))

    cuda.memcpy_dtoh(output, entropy_gpu)
    return output

def hash_batch(inputs):
    count = inputs.shape[0]
    hashes = np.zeros_like(inputs)

    inputs_gpu = cuda.mem_alloc(inputs.nbytes)
    hashes_gpu = cuda.mem_alloc(hashes.nbytes)

    cuda.memcpy_htod(inputs_gpu, inputs)

    hash_kernel(inputs_gpu, hashes_gpu, np.int32(count),
                block=(256, 1, 1), grid=(int((count + 255) / 256), 1))

    cuda.memcpy_dtoh(hashes, hashes_gpu)
    return hashes
