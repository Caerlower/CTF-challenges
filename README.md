# AlgoBharat CTF Challenges

This repository contains solutions and code for the AlgoBharat CTF challenges. Below are details for each challenge, including tasks, specifications, and transaction proofs.

## CTF Challenge 1: Find the Hidden Flag in Global Storage

**Objective:**
Uncover a hidden clue stored in the global storage of a deployed smart contract. Once decrypted, the clue reveals a wallet address. You must then send 1 Algo token to this address programmatically.

**Smart Contract ID:**
```718383248```

**Receiver address(task):** ```2JAZQO6Z5BCXFMPVW2CACK2733VGKWLZKS6DGG565J7H5NH77JNHLIIXLY```
```
Terminal Output:
Address: K54ZTTHNDB567Q5J5T73CEJCT3Z3MB6VL35PJBIX57KGRWNGZZLH3BK7S4
Txn sent: https://testnet.explorer.perawallet.app/tx/G4Q2KDOFYKGUGVR2ZHUEFUI5G54GN643YH7PYORKNVVG37RDEDBQ
Txn Confirmed in round 44366158
```
<img width="901" alt="transaction1" src="https://github.com/user-attachments/assets/99acc45f-bd9a-451a-acc5-e0092712de12">

## CTF Challenge 2: Find the Hidden Flag in Encrypted Strings

**Objective:**
Uncover a hidden clue within six different strings using a substitution cipher technique. The decrypted clue will reveal an Asset ID that must be used to perform an NFT opt-in transaction.

**Asset ID(task):** ```720485937```
```
Address: K54ZTTHNDB567Q5J5T73CEJCT3Z3MB6VL35PJBIX57KGRWNGZZLH3BK7S4
Txn sent: https://testnet.explorer.perawallet.app/tx/YKJ3YO7ZHHTHABNFCBOE5FCZBBFHSQJNLMNH6SPC3HOVHZXQWQVQ
Txn Confirmed in round 44366801
```
<img width="887" alt="optintransaction" src="https://github.com/user-attachments/assets/100bb692-299b-499b-aed8-245a47055267">

## CTF Challenge 3: Encrypt and Send a Message

**Objective:**
- Find a key by matching the asset ID and the wallet address.
- Use this key to encrypt a message.
- Send an ALGO with the encrypted message as a note.

**Encrypt key(to find in step2):** ```ZA2Q5OBZZ```

**Message in encryption(task in step3 - to send this to wallet address):** ```c1404af15dfdf2dc8f28f43ee1e8efd3e9b44e294dfee0593defe3cf769025611```
```
Address: K54ZTTHNDB567Q5J5T73CEJCT3Z3MB6VL35PJBIX57KGRWNGZZLH3BK7S4
Txn sent: https://testnet.explorer.perawallet.app/tx/TGUAUOZ3HPQ7YPIHMU7MF7F4HW2ZQH4BZO3GGONY32YTXNBGU3VA
Txn Confirmed in round 44367961
```

<img width="850" alt="transaction3" src="https://github.com/user-attachments/assets/f1f37207-e3f8-41ed-bdf0-79c2d59bacda">


## CTF challenge-4




