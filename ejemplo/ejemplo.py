def add_numbers(a, b):
    return a + b

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0

def generate_coverage_report():
    # Genera un reporte de cobertura usando la biblioteca de cobertura
    # Por ejemplo, utiliza Coverage.py: https://coverage.readthedocs.io/
    import coverage

    cov = coverage.Coverage()
    cov.start()

    # Ejecuta tus pruebas aquí
    test_add_numbers()

    cov.stop()
    cov.save()
    cov.report()

if __name__ == "__main__":
    generate_coverage_report()
