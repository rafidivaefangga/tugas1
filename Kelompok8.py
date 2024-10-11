def menara_hanoi(n, asal, tujuan, perantara):
    if n == 1:
        print(f"Pindahkan cakram {n} dari {asal} ke {tujuan}")
        return
    menara_hanoi(n-1, asal, perantara, tujuan)
    print(f"Pindahkan cakram {n} dari {asal} ke {tujuan}")
    menara_hanoi(n-1, perantara, tujuan, asal)

# Memulai permainan dengan 3 cakram dari Tiang A ke Tiang C
n = 3
menara_hanoi(n, 'A', 'C', 'B')





