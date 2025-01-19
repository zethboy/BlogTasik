import random

def judi_simulasi():
    print("=== Simulasi Risiko Perjudian ===")
    saldo = 100  
    taruhan = 10  
    peluang_menang = 0.2  
    putaran = 0

    print(f"Saldo awal Anda: Rp{saldo}")
    print(f"Peluang menang: {peluang_menang * 100}%")
    print(f"Taruhan per putaran: Rp{taruhan}")
    print("\n--- Mulai Simulasi ---")

    while saldo > 0:
        putaran += 1
        if random.random() < peluang_menang:
            kemenangan = taruhan * 2
            saldo += kemenangan
            print(f"Putaran {putaran}: Anda MENANG! Saldo bertambah Rp{kemenangan}. Saldo sekarang: Rp{saldo}")
        else:
            saldo -= taruhan
            print(f"Putaran {putaran}: Anda KALAH! Saldo berkurang Rp{taruhan}. Saldo sekarang: Rp{saldo}")

        if saldo < taruhan:
            print("\nSaldo Anda tidak cukup untuk melanjutkan permainan.")
            break


judi_simulasi()
