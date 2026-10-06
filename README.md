# Minpro-2-DDP-MeminjamBarangDiLabKomputer
Sebuah sekolah masih menggunakan sistem peminjaman barang lab komputer secara analog (manual), sekolah tersebut ingin mengdigitalisasikan sistem meminjam barang tersebut.

# Flowchart
<img width="4052" height="2212" alt="mini project 2 drawio" src="https://github.com/user-attachments/assets/0a0d43a4-db3c-4f0b-a9df-1cc1969b06f2" />

Ada flowchart login, menu user sama menu admin. Saya bikin pisah karena jika digabung jadi 1 maka bakal jadi rumit untuk dirancang

# Penjelasan Program
Untuk penjelasan ini saya hanya memberi singkatnya saja

### Untuk login, saya memisahkan admin dan user sebagai 2 role, jadi jika admin login:
<img width="424" height="80" alt="Code_rCcyuPiG14" src="https://github.com/user-attachments/assets/03eaa8e4-92a4-4e5b-90c3-3ec8bb79f441" />

### Maka bakal muncul menu admin
<img width="341" height="147" alt="Code_IW4GTNkwzk" src="https://github.com/user-attachments/assets/a3b4645e-1aea-4573-a586-0349bf0cdb32" />

### Ceritanya sama dengan role user, tetapi yang muncul menu user
<img width="288" height="117" alt="Code_VBx0kkEAER" src="https://github.com/user-attachments/assets/1821237b-9d2f-466d-825c-c41ac1d660a1" />

### Jika username atau password salah, bakal mengulang lagi
<img width="367" height="48" alt="Code_lh7JCsOTs8" src="https://github.com/user-attachments/assets/d1c805d9-c51d-4eb2-868b-8f560a0a3ae4" />

### Untuk pilihannya sendiri, menu admin dan user sama tampilannya jika memilih opsi 1
<img width="367" height="423" alt="Code_YJQUvi9VcQ" src="https://github.com/user-attachments/assets/decbc961-d601-481a-817d-e2507034d6f5" />

## Menu Admin
### Jika ingin menambah barang
<img width="316" height="358" alt="Code_6qiIloVHsX" src="https://github.com/user-attachments/assets/359c8cdf-6525-490a-882d-5bfe3154ca60" />

### Sebaliknya
<img width="367" height="354" alt="Code_3AqDZAg1pA" src="https://github.com/user-attachments/assets/86f08c6a-b361-4409-bc25-0bc349c6faff" />

### Tapi jika ID barang tersebut tidak ditemukan (menghapus)/sudah ada (menambah, maka dia bakal kembali ke menu awal
<img width="448" height="87" alt="Code_IyMlegwGOX" src="https://github.com/user-attachments/assets/4db4a97b-1635-4c14-9521-dbedcdbfc3d2" />

<img width="411" height="258" alt="Code_YtNWda0yat" src="https://github.com/user-attachments/assets/e644bffc-4a2b-4598-b502-e2abc2a6b4a6" />


### Membuat barang tidak tersedia atau tersedia
Jika barang tersebut tidak tersedia, maka dia akan masuk ke tabel tidak tersedia dan sebaliknya
<img width="436" height="400" alt="Code_UyjPx4Iebi" src="https://github.com/user-attachments/assets/48b939ed-6340-45d4-90fd-f5febf17cb35" />

<img width="457" height="371" alt="Code_lMPxY1zWgY" src="https://github.com/user-attachments/assets/8d97d430-70da-4a78-9658-a616d0a9c73e" />

### Jika ID didalam kedua tabel tersebut tidak ada, maka dia kembali ke menu awal
<img width="494" height="87" alt="Code_PUGpDzJJo9" src="https://github.com/user-attachments/assets/9c9424ed-6659-49a6-bb9c-2557bb7917f2" />

### Manajmen User
Untuk manajmen user ada 3 opsi

<img width="219" height="110" alt="Code_ruwQx2mm5B" src="https://github.com/user-attachments/assets/db8bf78f-7437-4660-be8c-9a13234850c2" />

### Opsi 1: Menampilkan users yang ada
<img width="327" height="183" alt="Code_9ba8xItNL2" src="https://github.com/user-attachments/assets/ac9c3fda-8861-4563-856b-db6d513b70d1" />

### Opsi 2: Menambahkan user baru
<img width="324" height="224" alt="Code_RqJpkQSm4i" src="https://github.com/user-attachments/assets/fbab9f17-cbe4-4c19-974c-030281b83d8b" />

### Opsi 3: Menghapus user
<img width="406" height="175" alt="Code_SjSBrM5Aug" src="https://github.com/user-attachments/assets/832378a0-1e24-4403-a1d1-cbaf2d53333d" />

### Jika user tersebut tidak ada untuk dihapus, maka dia kembali ke menu awal
<img width="384" height="101" alt="Code_5bkrpWRihe" src="https://github.com/user-attachments/assets/a52e2bbc-6e68-4911-842c-4b3b73afe7dc" />

## Menu User
### Meminjam barang
<img width="407" height="284" alt="Code_AFx141P5F2" src="https://github.com/user-attachments/assets/608559f5-951e-4ef0-a868-c4b5bf644c68" />

### Mengembalikan barang
<img width="509" height="246" alt="Code_K8hszrbjXI" src="https://github.com/user-attachments/assets/c9a1b307-ba3c-4985-b4b3-1332a74cd4ec" />

### Jika barang tersebut tidak ada
<img width="458" height="83" alt="Code_3hpEotSl9D" src="https://github.com/user-attachments/assets/1192a2b5-ba29-417f-b985-4bb82da85d09" />

<img width="405" height="80" alt="Code_EahsPIpHc7" src="https://github.com/user-attachments/assets/d14f4b44-3e2b-4a44-818d-c0d3b43748d2" />

## Untuk keluar dari program, cukup mengetik "exit"
<img width="394" height="38" alt="Code_Rr4tdXkzaa" src="https://github.com/user-attachments/assets/822ef3e8-6db8-40d3-93eb-71cac7239dbe" />

(Untuk username buat login saya exclude 'exit' untuk mengantisipasi admin mengregistrasi user dengan nama tersebut)

# Fitur tambahan
### Setiap menu menglooping kembali, maka dia akan clear isi terminal dengan definisi ini diakhir
<img width="591" height="111" alt="image" src="https://github.com/user-attachments/assets/ded8135a-4136-44c8-91ee-5f10c4f6949f" />

<img width="458" height="65" alt="image" src="https://github.com/user-attachments/assets/d9437da6-426c-45a4-afa2-643716b25a87" />

### Untuk tabel sendiri sudah ditunjukan didalam penjelasan program
<img width="566" height="163" alt="image" src="https://github.com/user-attachments/assets/8f6fb640-936a-466e-9acb-21bf9851943f" />

