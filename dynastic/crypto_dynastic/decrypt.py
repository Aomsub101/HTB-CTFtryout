"""reverse"""

def to_identity_map(a) -> int:
    """
    Leave some notes
    """
    return ord(a) - 0x41


def from_identity_map(a) -> str:
    """
    Leave some notes
    """
    return chr(a % 26 + 0x41)


def decrypt(message) -> str:
    """
    Leave some notes
    """
    dm = ""
    for ch,i in enumerate(message):
        if not ch.isalpha():
            dm += ch
        else:
            chi = to_identity_map(ch)
            dm += from_identity_map(chi - i)

    return 'HTB{' + dm + '}'

ENCRYPED_MESSAGE = "DJF_CTA_SWYH_NPDKK_MBZ_QPHTIGPMZY_KRZSQE?!_ZL_CN_PGLIMCU_YU_KJODME_RYGZXL"
decrypted_message = decrypt(ENCRYPED_MESSAGE)

print(f"decrypted message: {decrypted_message}")
