"""Modul perbaikan kode sesuai standar PEP 8."""


def fungsi_baik(angka_a, angka_b):
    """Menjumlahkan dua angka.

    Args:
        angka_a: Angka pertama.
        angka_b: Angka kedua.

    Returns:
        Hasil penjumlahan angka_a dan angka_b.
    """
    return angka_a + angka_b


def main():
    """Fungsi utama program."""
    hasil = fungsi_baik(10, 20)
    print(f"Hasil penjumlahan: {hasil}")


if __name__ == "__main__":
    main()
