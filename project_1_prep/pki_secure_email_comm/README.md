# Implementing PKI for Secure Email Communication using OpenSSL 

I already had OpenSSL installed on my system, so I skipped the installation step.

## 2. Charlie (CA) Sets Up a Certificate Authority (CA)

This step went smoothly. I followed the commands in the assignment. Setting up a CA cert is crucial for the rest of the process, because it will be used to sign the certificates of the users.

## 3. Alice and Bob Generate Their Key Pairs and Certificate Signing Requests (CSR)

For this step, specifically for generating the CSR, OpenSSL asked me to enter information about who I'm creating the key pair for. For both Alice and Bob I kept most of the information the same, but for the common name, I entered the name of the person I was creating the key pair for. This step went smoothly as well. The key pairs and CSR files are needed so that each user can verify, encrypt, and decrypt messages from the other user.

## 4. Charlie (CA) Signs Alice and Bob’s Certificates

This step went well. For both certs that I signed, I got the `Certificate request self-signature ok` message, with information about each cert.

## 5. Alice Encrypts a Message for Bob

On this step, I accidentally used double quotes around the message, which caused an error. After fixing that, and using single quotes, the step went well.

## 6. Bob Decrypts Alice’s Message

The decryption went fine. I was able to decrypt Alice's message with no errors.

## 7. Bob Signs a Response Message for Alice

The signing also went well. Didn't get any output, but when I used `cat` to view the contents of the signed message, I could see that it worked based on the `BEGIN PKCS7` and `END PKCS7` lines.

## 8. Alice Verifies Bob’s Signed Message

I actually ran into an error while verifying Bob's signed message. I got the error `Error reading S/MIME message`. I assumed this was because the `-outform` argument from the previous step was set to PEM. Once I removed the `-outform PEM` argument, the verification succeeded.