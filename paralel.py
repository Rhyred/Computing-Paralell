from multiprocessing import Process, Queue

def partial_sum(start, end, q, pid):
    """
    Fungsi ini akan dieksekusi oleh masing-masing proses.
    Menghitung jumlah dari 'start' sampai 'end'.
    """
    s = sum(range(start, end + 1))
    print(f"Process {pid}: sum({start} to {end}) = {s}")
    
    # Masukkan hasil perhitungan ke dalam Queue agar bisa diambil di main program
    q.put(s)


if __name__ == "__main__":
    print("Parallel Computation:")
    
    # Membuat Queue untuk menyimpan hasil dari tiap proses
    q = Queue()
    
    # Mendefinisikan proses 1 dan proses 2
    # target: fungsi yang akan dijalankan
    # args: argumen yang dikirim ke fungsi (start, end, queue, process_id)
    p1 = Process(target=partial_sum, args=(1, 3, q, 1))
    p2 = Process(target=partial_sum, args=(4, 5, q, 2))
    
    # Memulai proses (menjalankan fungsi partial_sum secara bersamaan)
    p1.start()
    p2.start()
    
    # Menunggu kedua proses selesai sebelum melanjutkan baris kode di bawahnya
    p1.join()
    p2.join()
    
    # Mengambil hasil dari Queue (Sum1 dan Sum2) lalu menjumlahkannya
    final_sum = 0
    while not q.empty():
        final_sum += q.get()
        
    print(f"Final Parallel Sum = {final_sum}")