import os
from mnemonic import Mnemonic
from bip_utils import Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes
from colorama import Fore, Style, init

init(autoreset=True)

def generate_sol():
    print(f"{Fore.CYAN}{Style.BRIGHT}=== SOLANA WALLET GENERATOR ==={Style.RESET_ALL}")
    try:
        count = int(input(f"{Fore.YELLOW}How many SOL wallets? {Fore.WHITE}"))
    except: return

    mnemo = Mnemonic("english")
    file_path = os.path.join(os.path.dirname(__file__), "solwallet.txt")

    with open(file_path, "a", encoding="utf-8") as f:
        for i in range(1, count + 1):
            words = mnemo.generate(strength=128)
            seed_bytes = Bip39SeedGenerator(words).Generate()
            
            # Solana için özelleştirilmiş Bip44 sınıfı
            bip44_mst_ctx = Bip44.FromSeed(seed_bytes, Bip44Coins.SOLANA)
            address = bip44_mst_ctx.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0).PublicKey().ToAddress()
            
            header = f"{Fore.GREEN}{Style.BRIGHT}--- SOL Wallet #{i} ---"
            seed_text = f"{Fore.BLUE}{Style.BRIGHT}Seed Phrase: {Fore.WHITE}{words}"
            addr_text = f"{Fore.MAGENTA}{Style.BRIGHT}SOL Address: {Fore.YELLOW}{address}"
            
            print(f"\n{header}\n{seed_text}\n{addr_text}")
            f.write(f"SOL Wallet #{i}\nSeed: {words}\nAddress: {address}\n{'-'*50}\n")
            f.flush()
    print(f"\n{Fore.CYAN}{Style.BRIGHT}Success! Saved to: {Fore.WHITE}solwallet.txt")

if __name__ == "__main__":
    generate_sol()