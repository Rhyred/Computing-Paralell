<div align="center">

# 🚀 Sequential vs Parallel Computing 🔥

![Python](https://img.shields.io/badge/Python-3.x-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-success.svg?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)
![Parallel](https://img.shields.io/badge/Computing-Parallel-red.svg?style=for-the-badge&logo=lightning)

### 💻 Demonstrasi Komputasi Sequential & Parallel Menggunakan Python

</div>

---

## 📑 Table of Contents

- [📋 Overview](#-overview)
- [✨ Features](#-features)
- [📁 Struktur Project](#-struktur-project)
- [🚀 Quick Start](#-quick-start)
- [🔍 Penjelasan Detail](#-penjelasan-detail)
- [📊 Perbandingan Performance](#-perbandingan-performance)
- [💡 Konsep &amp; Best Practices](#-konsep--best-practices)
- [🛠️ Tech Stack](#️-tech-stack)
- [📚 Referensi](#-referensi)
- [👤 Author](#-author)

---

## 📋 Overview

<div align="center">

```
┌─────────────────────────────────────────────────────────────┐
│  Proyek ini mendemonstrasikan perbedaan fundamental antara │
│  komputasi SEQUENTIAL (berurutan) dan PARALLEL (paralel)   │
│  menggunakan studi kasus sederhana: perkalian matrix        │
└─────────────────────────────────────────────────────────────┘
```

</div>

Program ini membandingkan **dua pendekatan** berbeda dalam menyelesaikan masalah yang sama:

| 🔄 Sequential            | ⚡ Parallel           |
| ------------------------ | --------------------- |
| Eksekusi berurutan       | Eksekusi bersamaan    |
| Single Process           | Multiple Processes    |
| Simple & Straightforward | Complex tapi Scalable |

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🔸 Sequential Computing
```
┌──────────────────────┐
│  Hitung tiap elemen  │
│  hasil secara urut   │
└──────────────────────┘
```
✅ Mudah dipahami  
✅ Low overhead  
✅ Deterministik  

</td>
<td width="50%">

### 🔸 Parallel Computing
```
┌──────────────────────┐
│  Process row-0       │
│  Process row-1       │
│   (Concurrent)       │
└──────────────────────┘
```
✅ High performance  
✅ Scalable  
✅ Multi-core optimized  

</td>
</tr>
</table>

---

## 📁 Struktur Project

```
📦 Wokspaces
 ┣ 📜 sequential.py     # Sequential matrix multiplication
 ┣ 📜 paralel.py        # Parallel matrix multiplication with multiprocessing
 ┗ 📜 readme.md         # You're here! 📍
```

<details>
<summary>🔍 Click untuk melihat detail file</summary>

- **sequential.py**: Implementasi perkalian matrix secara serial dengan nested loop
- **paralel.py**: Implementasi parallel matrix multiplication per baris dengan `multiprocessing`
- **readme.md**: Dokumentasi lengkap project

</details>

---

## 🚀 Quick Start

### 📌 Prerequisites

```bash
✓ Python 3.x installed
✓ Terminal/Command Prompt
```

### 🔸 Running Sequential

```bash
# Navigate to project directory
# Run sequential program
python sequential.py
```

**📤 Expected Output:**

```
Sequential Matrix Multiplication
A = [[1, 2, 3], [4, 5, 6]]
B = [[7, 8], [9, 10], [11, 12]]
Result = [[58, 64], [139, 154]]
```

### 🔸 Running Parallel

```bash
# Run parallel program
python paralel.py
```

**📤 Expected Output:**

```
Parallel Matrix Multiplication
A = [[1, 2, 3], [4, 5, 6]]
B = [[7, 8], [9, 10], [11, 12]]
Process row-0: [58, 64]
Process row-1: [139, 154]
Result = [[58, 64], [139, 154]]
```

---

## 🔍 Penjelasan Detail

### 🔵 Sequential Computing (`sequential.py`)

**💡 Cara Kerja:**

- ✔️ Menggunakan **nested loop** untuk menghitung setiap elemen matrix hasil
- ✔️ Semua perhitungan dikerjakan berurutan dalam satu proses
- ✔️ Cocok untuk baseline pembanding sebelum versi paralel

**📝 Key Points:**

```python
for i in range(rows_a):
    for j in range(cols_b):
        for k in range(cols_a):
            result[i][j] += matrix_a[i][k] * matrix_b[k][j]
```

---

### 🔴 Parallel Computing (`paralel.py`)

```
        ┌─────────────────┐
        │   Main Process  │
        └────────┬────────┘
                 │
        ┌────────┴────────┐
        │                 │
   ┌────▼────┐      ┌────▼────┐
   │Row 0    │      │Row 1    │
   │[58, 64] │      │[139,154]│
   │Done     │      │Done     │
   └────┬────┘      └────┬────┘
        │                 │
        └────────┬────────┘
                 │
           ┌─────▼─────┐
         │Queue: rows│
           └─────┬─────┘
                 │
          ┌──────▼──────┐
        │Final Matrix │
          └─────────────┘
```

**💡 Cara Kerja:**

- ✔️ Menggunakan **`multiprocessing` module**
- ✔️ Membagi task per baris matrix A ke **proses independen**
- ✔️ Komunikasi via **Queue**
- ✔️ `join()` untuk sinkronisasi

**📝 Key Components:**

```python
for i, row in enumerate(matrix_a):
    process = Process(target=multiply_row, args=(i, row, matrix_b, q))
    processes.append(process)
    process.start()

for process in processes:
    process.join()
```

---

## 📊 Perbandingan Performance

<table>
<thead>
<tr>
<th>Aspek</th>
<th>⚪ Sequential</th>
<th>🔴 Parallel</th>
</tr>
</thead>
<tbody>
<tr>
<td><b>⏱️ Time Complexity</b></td>
<td>O(m × n × k)</td>
<td>≈ O((m × n × k)/p) <i>p=processes</i></td>
</tr>
<tr>
<td><b>💾 Memory</b></td>
<td>Low</td>
<td>Higher (multiple processes)</td>
</tr>
<tr>
<td><b>🔧 Complexity</b></td>
<td>Simple</td>
<td>Complex</td>
</tr>
<tr>
<td><b>🎯 Best For</b></td>
<td>Small datasets</td>
<td>Large datasets</td>
</tr>
<tr>
<td><b>🖥️ CPU Usage</b></td>
<td>Single core</td>
<td>Multiple cores</td>
</tr>
</tbody>
</table>

---

## 💡 Konsep & Best Practices

### Kapan Menggunakan Sequential?

```
✅ GUNAKAN SEQUENTIAL JIKA:

-  Dataset kecil (overhead parallel > benefit)
-  Task saling bergantung (dependency tinggi)
-  Resource terbatas (single-core system)
-  Simplicity first (maintainability penting)
```

### Kapan Menggunakan Parallel?

```
✅ GUNAKAN PARALLEL JIKA:

-  Dataset besar (benefit > overhead)
-  Task independen (no dependency)
-  Multi-core available (utilize all cores)
-  Performance critical (speed matters)
```

### Keuntungan Parallel Computing

<div align="center">

| Icon | Benefit                   | Description                               |
| :--: | ------------------------- | ----------------------------------------- |
|  ⚡  | **Speed**           | Eksekusi lebih cepat untuk large datasets |
|  🔄  | **Scalability**     | Mudah menambah workers/processes          |
| 🖥️ | **CPU Utilization** | Maksimalkan penggunaan multi-core         |
|  📊  | **Throughput**      | Handle lebih banyak task simultaneously   |

</div>

---

## 🛠️ Tech Stack

<div align="center">

|                                                  Technology                                                  | Purpose            | Version |
| :-----------------------------------------------------------------------------------------------------------: | ------------------ | :------: |
|          ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white)          | Main Language      |   3.x   |
| ![Multiprocessing](https://img.shields.io/badge/-Multiprocessing-FF6B6B?style=flat&logo=python&logoColor=white) | Parallel Execution | Built-in |
|           ![Queue](https://img.shields.io/badge/-Queue-4ECDC4?style=flat&logo=buffer&logoColor=white)           | IPC Mechanism      | Built-in |

</div>

### 📦 Dependencies

```bash
# No external dependencies required!
# All modules are Python built-ins:
- multiprocessing  # For parallel computing
- queue            # For inter-process communication
```

---

## 📚 Referensi

<div align="center">

### 🎓 Mata Kuliah

**IFB-206 Komputasi Paralel & Sistem Terdistribusi**
📖 Tugas - Sequential vs Parallel Computing

</div>

### 📖 Learning Resources

- 📘 [Python Multiprocessing Documentation](https://docs.python.org/3/library/multiprocessing.html)
- 📙 [Parallel Computing Concepts](https://en.wikipedia.org/wiki/Parallel_computing)
- 📕 [Process vs Thread](https://stackoverflow.com/questions/200469/what-is-the-difference-between-a-process-and-a-thread)

### 🔗 Related Topics

```
🎯 Concurrency    🔄 Distributed Systems    ⚡ High Performance Computing
```

---

## 📝 Notes & Tips

<details>
<summary>💡 Click untuk informasi tambahan</summary>

### ⚠️ Important Notes:

- **Queue untuk IPC**: Program parallel menggunakan `Queue` untuk komunikasi antar proses
- **join() untuk Sinkronisasi**: Method `join()` memastikan semua child processes selesai sebelum main process lanjut
- **Small Dataset Caveat**: Untuk dataset kecil (seperti demo ini), sequential bisa lebih cepat karena overhead dari process creation

### Tips untuk Development:

1. **Testing**: Gunakan `time.time()` untuk measure execution time
2. **Debugging**: Parallel debugging lebih sulit, use logging extensively
3. **Scalability**: Test dengan dataset berbeda untuk find optimal number of processes

</details>

---

## 👤 Author

<div align="center">

### 🎓 Student Information

**Robi Rizki Permana**
 NIM: `152024141`

---

<table>
<tr>
<td align="center">
<img src="https://img.icons8.com/color/96/000000/python.png" width="60px"/><br/>
<sub><b>Python Developer</b></sub>
</td>
<td align="center">
<img src="https://img.icons8.com/color/96/000000/parallel-tasks.png" width="60px"/><br/>
<sub><b>Parallel Computing</b></sub>
</td>
<td align="center">
<img src="https://img.icons8.com/color/96/000000/code.png" width="60px"/><br/>
<sub><b>Algorithm Design</b></sub>
</td>
</tr>
</table>

---

### 📬 Connect

[![GitHub](https://img.shields.io/badge/-GitHub-181717?style=flat&logo=github)](https://github.com)
[![Email](https://img.shields.io/badge/-Email-D14836?style=flat&logo=gmail&logoColor=white)](mailto:robigold9@gmail.com)

</div>

---

<div align="center">

---

```
┌────────────────────────────────────────────┐
│  © 2026 Komputasi Paralel & Distributed    │
│     Systems - Informatika ITENAS           │
└────────────────────────────────────────────┘
```

</div>
