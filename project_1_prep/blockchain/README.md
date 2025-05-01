# Implementing Blockchain Technology using OpenSSL
Harrison Coutee - COMP 324 - March 25, 2025

## 1. Install OpenSSL

I already had OpenSSL installed, so I skipped this step.

## 2. Create the Genesis Block

This step went smoothly, I followed the commands in the assignment and successfully wrote the first block, and generated the sha256 for it. The hash was `4ad9c94b957fa924a5bcb01d310ab613220160e4503aacf1de032677bcf23351`.

## 3. Bob Adds a New Transaction

In this step, I recorded Bob's transaction, combined it with the genesis block hash, and generated a hash for the new block. The hash for block 2 was `7c728cd94736630651929ddd0ed4697e77c366b8b1669d3e9a3e77c8ae4f7bff`.

## 4. Charlie Adds Another Transaction

This step was basically the same as the last step, except this time I recorded Charlie's transaction, combined it with block 2's hash, and generated a hash for the new block. The hash for block 3 was `7fe7b653d143961feb44fc807611c7a792ffd6309dd62c56810034a490b00a04`.

## 5. David Verifies Blockchain Integrity

I successfully verified the blockchain integrity by checking the hashes of each block, and they were all correct!

```bash
# openssl dgst -sha256 block1.txt
SHA2-256(block1.txt)= 4ad9c94b957fa924a5bcb01d310ab613220160e4503aacf1de032677bcf23351
# cat block1_hash.txt
SHA2-256(block1.txt)= 4ad9c94b957fa924a5bcb01d310ab613220160e4503aacf1de032677bcf23351
# openssl dgst -sha256 block2.txt
SHA2-256(block2.txt)= 7c728cd94736630651929ddd0ed4697e77c366b8b1669d3e9a3e77c8ae4f7bff
# cat block2_hash.txt
SHA2-256(block2.txt)= 7c728cd94736630651929ddd0ed4697e77c366b8b1669d3e9a3e77c8ae4f7bff
# openssl dgst -sha256 block3.txt
SHA2-256(block3.txt)= 7fe7b653d143961feb44fc807611c7a792ffd6309dd62c56810034a490b00a04
# cat block3_hash.txt
SHA2-256(block3.txt)= 7fe7b653d143961feb44fc807611c7a792ffd6309dd62c56810034a490b00a04
```
