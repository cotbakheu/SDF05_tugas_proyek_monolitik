# Refactor: Pemisahan Domain, Storage, dan CLI

## Bagaimana dependency berubah setelah kode dipisahkan

Awalnya seluruh kode berada dalam satu file (`app.py`) yang mencampur
aturan validasi user, logic baca/tulis file, dan logic CLI.

Sesudah kode dipisah menjadi struktur folder berikut:

```
src/user/
├── domain/
│   ├── rules.py
│   └── ports.py
├── services/
│   └── user_service.py
├── adapters/
│   └── file_storage.py
└── cli.py
```

Fungsi masing-masing folder:

- **`domain/`** — aturan bisnis inti.
  - `rules.py` berisi validasi nama & email.
  - `ports.py` berisi kontrak storage (`Loader`/`Saver`) yang dibutuhkan oleh
    service.
- **`services/`** — untuk fungsi (`create_user`, `list_users`).
- **`adapters/`** — untuk write dan read data ke file JSON (`file_storage.py`).
- **`cli.py`** — interface cli.

## Alasan pembagian module, arah dependency, dan manfaat struktur akhir

| Module                     | Tanggung jawab                        | Alasan dipisah                                                 |
| -------------------------- | ------------------------------------- | -------------------------------------------------------------- |
| `domain/rules.py`          | Aturan bisnis (validasi nama & email) | Untuk validasi user.                                           |
| `domain/ports.py`          | Kontrak storage (`Loader`/`Saver`)    | Mendefinisikan data apa yang dibutuhkan service dari storage.  |
| `services/user_service.py` | Fungsi (`create_user`, `list_users`)  | Menyatukan aturan bisnis dengan storage.                       |
| `adapters/file_storage.py` | Implementasi read/write file JSON     | Menyimpan atau mengambil data user yang disimpan di file JSON. |
| `cli.py`                   | Antarmuka pengguna + composition root | Implementasi fungsi modul user.                                |

Manfaat dari struktur akhir ini:

- **Mudah diuji** — aturan bisnis di `domain/rules.py` bisa ditest dan `services/user_service.py` bisa diuji dengan data mock sesuai dengan
  (`Loader`/`Saver`).
- **Mudah diganti** — jika storage berpindah dari file JSON ke database, cukup
  membuat adapter baru yang memenuhi tipe di `ports.py`; `domain/` dan
  `services/` tidak perlu diubah sama sekali.
- **Tanggung jawab jelas** — setiap module punya satu alasan untuk berubah,
  sehingga perubahan di satu bagian (misalnya format penyimpanan) tidak
  merembet ke bagian lain (misalnya aturan validasi).

## Cara menjalankan

Install project dalam mode editable terlebih dahulu (diperlukan karena
struktur `src/` layout):

```bash
pip install -e .
```

Menjalankan aplikasi CLI:

```bash
python3 -m user.cli
```

Menjalankan test:

```bash
python3 -m pytest test/unit/test_rules.py
```
