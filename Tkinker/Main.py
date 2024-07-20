import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class Barang:
    def __init__(self, kode, nama, deskripsi, kategori, jumlah, tanggal_masuk):
        self.kode = kode
        self.nama = nama
        self.deskripsi = deskripsi
        self.kategori = kategori
        self.jumlah = jumlah
        self.tanggal_masuk = tanggal_masuk

class Inventaris:
    def __init__(self):
        self.daftar_barang = []

    def tambah_barang(self, barang):
        self.daftar_barang.append(barang)

    def keluar_barang(self, kode, jumlah):
        for barang in self.daftar_barang:
            if barang.kode == kode:
                if barang.jumlah >= jumlah:
                    barang.jumlah -= jumlah
                    if barang.jumlah == 0:
                        self.daftar_barang.remove(barang)
                    return True
                else:
                    return False
        return None

    def buat_laporan(self):
        laporan = "Laporan Inventaris:\n"
        laporan += f"{'Kode':<6} | {'Nama Barang':<20} | {'Jumlah':<7} | {'Kategori':<12}\n"
        laporan += "-" * 50 + "\n"
        for barang in self.daftar_barang:
            laporan += f"{barang.kode:<6} | {barang.nama:<20} | {barang.jumlah:<7} | {barang.kategori:<12}\n"
        return laporan

def tambah_barang_window(inventaris):
    def tambah_barang():
        kode = kode_entry.get()
        nama = nama_entry.get()
        deskripsi = deskripsi_entry.get()
        kategori = kategori_entry.get()
        try:
            jumlah = int(jumlah_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Jumlah harus berupa angka")
            return
        tanggal_masuk = tanggal_masuk_entry.get()

        barang = Barang(kode, nama, deskripsi, kategori, jumlah, tanggal_masuk)
        inventaris.tambah_barang(barang)
        messagebox.showinfo("Info", f"Barang {nama} telah ditambahkan.")
        tambah_barang_win.destroy()

    tambah_barang_win = tk.Toplevel()
    tambah_barang_win.title("Tambah Barang")

    tk.Label(tambah_barang_win, text="Kode").grid(row=0, column=0)
    kode_entry = tk.Entry(tambah_barang_win)
    kode_entry.grid(row=0, column=1)

    tk.Label(tambah_barang_win, text="Nama").grid(row=1, column=0)
    nama_entry = tk.Entry(tambah_barang_win)
    nama_entry.grid(row=1, column=1)

    tk.Label(tambah_barang_win, text="Deskripsi").grid(row=2, column=0)
    deskripsi_entry = tk.Entry(tambah_barang_win)
    deskripsi_entry.grid(row=2, column=1)

    tk.Label(tambah_barang_win, text="Kategori").grid(row=3, column=0)
    kategori_entry = tk.Entry(tambah_barang_win)
    kategori_entry.grid(row=3, column=1)

    tk.Label(tambah_barang_win, text="Jumlah").grid(row=4, column=0)
    jumlah_entry = tk.Entry(tambah_barang_win)
    jumlah_entry.grid(row=4, column=1)

    tk.Label(tambah_barang_win, text="Tanggal Masuk").grid(row=5, column=0)
    tanggal_masuk_entry = tk.Entry(tambah_barang_win)
    tanggal_masuk_entry.grid(row=5, column=1)
    tanggal_masuk_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))

    tk.Button(tambah_barang_win, text="Tambah", command=tambah_barang).grid(row=6, column=0, columnspan=2)

def keluar_barang_window(inventaris):
    def keluar_barang():
        kode = kode_entry.get()
        try:
            jumlah = int(jumlah_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Jumlah harus berupa angka")
            return

        result = inventaris.keluar_barang(kode, jumlah)
        if result is True:
            messagebox.showinfo("Info", f"{jumlah} unit barang dengan kode {kode} telah dikeluarkan.")
        elif result is False:
            messagebox.showwarning("Peringatan", "Jumlah yang diminta melebihi jumlah yang tersedia.")
        else:
            messagebox.showwarning("Peringatan", "Barang dengan kode tersebut tidak ditemukan.")
        keluar_barang_win.destroy()

    keluar_barang_win = tk.Toplevel()
    keluar_barang_win.title("Keluarkan Barang")

    tk.Label(keluar_barang_win, text="Kode").grid(row=0, column=0)
    kode_entry = tk.Entry(keluar_barang_win)
    kode_entry.grid(row=0, column=1)

    tk.Label(keluar_barang_win, text="Jumlah").grid(row=1, column=0)
    jumlah_entry = tk.Entry(keluar_barang_win)
    jumlah_entry.grid(row=1, column=1)

    tk.Button(keluar_barang_win, text="Keluarkan", command=keluar_barang).grid(row=2, column=0, columnspan=2)

def lihat_barang_window(inventaris):
    lihat_barang_win = tk.Toplevel()
    lihat_barang_win.title("Lihat Barang")

    if len(inventaris.daftar_barang) == 0:
        tk.Label(lihat_barang_win, text="Tidak ada barang di inventaris.").pack()
    else:
        tree = ttk.Treeview(lihat_barang_win, columns=("Kode", "Nama", "Deskripsi", "Kategori", "Jumlah", "Tanggal Masuk"), show='headings')
        tree.heading("Kode", text="Kode")
        tree.heading("Nama", text="Nama")
        tree.heading("Deskripsi", text="Deskripsi")
        tree.heading("Kategori", text="Kategori")
        tree.heading("Jumlah", text="Jumlah")
        tree.heading("Tanggal Masuk", text="Tanggal Masuk")

        for barang in inventaris.daftar_barang:
            tree.insert("", "end", values=(barang.kode, barang.nama, barang.deskripsi, barang.kategori, barang.jumlah, barang.tanggal_masuk))

        tree.pack(fill=tk.BOTH, expand=True)

def buat_laporan_window(inventaris):
    buat_laporan_win = tk.Toplevel()
    buat_laporan_win.title("Buat Laporan")

    laporan = inventaris.buat_laporan()
    text_widget = tk.Text(buat_laporan_win, height=20, width=80)
    text_widget.insert(tk.END, laporan)
    text_widget.pack()

def main():
    inventaris = Inventaris()

    root = tk.Tk()
    root.title("Sistem Manajemen Inventaris")

    menu_frame = tk.Frame(root)
    menu_frame.pack(pady=20)

    tk.Button(menu_frame, text="Tambah Barang", command=lambda: tambah_barang_window(inventaris)).pack(fill=tk.X)
    tk.Button(menu_frame, text="Keluarkan Barang", command=lambda: keluar_barang_window(inventaris)).pack(fill=tk.X)
    tk.Button(menu_frame, text="Lihat Barang", command=lambda: lihat_barang_window(inventaris)).pack(fill=tk.X)
    tk.Button(menu_frame, text="Buat Laporan", command=lambda: buat_laporan_window(inventaris)).pack(fill=tk.X)
    tk.Button(menu_frame, text="Keluar", command=root.quit).pack(fill=tk.X)

    root.mainloop()

if __name__ == "__main__":
    main()
